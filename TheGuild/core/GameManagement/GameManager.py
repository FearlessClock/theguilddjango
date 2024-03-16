from TheGuild.core.Models.CountryModel import Country
from TheGuild.core.Models.WorkshopModel import Workshop, Workshop_Recipe
from TheGuild.core.Models.StorageModel import Storage, Storage_Goods
from TheGuild.core.Models.EmployeeModel import Employee
from TheGuild.core.Models.GoodsModel import Recipe, Recipe_Goods

from datetime import datetime, UTC

def TickCountry(countryID):
    country = Country.objects.get(id=countryID)
    secondsSinceLastUpdate = (datetime.now(UTC) - country.last_update).total_seconds()
    if secondsSinceLastUpdate > country.tick_in_seconds:
        country.last_update = datetime.now(UTC)
        country.tick = int((datetime.now(UTC) - country.start_date).total_seconds() / country.tick_in_seconds)
        country.save()
        
    print(str(secondsSinceLastUpdate))

def UpdateWorkshop(workshop):
    secondsSinceLastUpdate = (datetime.now(UTC) - workshop.last_update).total_seconds()
    if secondsSinceLastUpdate > workshop.tick_in_seconds:
        workshop.last_update = datetime.now(UTC)
        workshop.tick = int((datetime.now(UTC) - workshop.start_date).total_seconds() / workshop.tick_in_seconds)
        employees = Employee.objects.filter(workshop_id=workshop.id).values()
        recipeIdsWorkedOn = []
        for employee in employees:
            workedOnRecipe = Workshop_Recipe.objects.get(recipe_id=employee["active_recipe_id"], workshop_id=workshop.id)
            if workedOnRecipe:
                found = False
                for i in range(len(recipeIdsWorkedOn)):
                    if recipeIdsWorkedOn[i][0] == workedOnRecipe.id:
                        recipeIdsWorkedOn[i] = (recipeIdsWorkedOn[i][0], recipeIdsWorkedOn[i][1]+1)
                        found= True
                if not found:
                    recipeIdsWorkedOn.append((workedOnRecipe.id, 1))
                
        for recipeWorkedOn in recipeIdsWorkedOn:
            recipe = Workshop_Recipe.objects.get(id=recipeWorkedOn[0])
            if not recipe.is_available: continue
            if not HasResources(workshop, recipe): 
                recipe.current_progress = 0
                recipe.last_update = datetime.now(UTC)
                recipe.save()
                continue
            ticksSinceLastUpdate = int((datetime.now(UTC) - recipe.last_update).total_seconds() / workshop.tick_in_seconds)
            recipe.current_progress += ticksSinceLastUpdate
            numberProducedInTime = int(recipe.current_progress / (recipe.recipe.construction_ticks/recipeWorkedOn[1]))
            numberReallyProduced = HowManyProduced(numberProducedInTime, workshop, recipe)
            if numberReallyProduced > 0:
                UpdateGoods(workshop, recipe, numberReallyProduced)
                if HasResources(workshop, recipe):
                    recipe.current_progress = recipe.current_progress % (recipe.recipe.construction_ticks/recipeWorkedOn[1])
                else: 
                    recipe.current_progress = 0
            recipe.last_update = datetime.now(UTC)
            recipe.save()
            print(numberReallyProduced)
        workshop.save()
        
def HasResources(workshop, workshop_recipe):
    recipe = workshop_recipe.recipe
    req_goods = Recipe_Goods.objects.filter(recipe_id=recipe.id)
    storage_goods = Storage_Goods.objects.filter(storage_id=workshop.storage.id)
    enough_resources = False
    for req_good in req_goods:
        for store_good in storage_goods:
            if(req_good.goods.id == store_good.goods_data.id):
                if(req_good.amount_required <= store_good.quantity):
                    enough_resources = True
                else:
                    enough_resources = False
                break
    return enough_resources

def HowManyProduced(amount, workshop, workshop_recipe):
    if amount == 0:
        return 0
    recipe = workshop_recipe.recipe
    required_goods_list = []
    owned_goods_list = []
    req_goods = Recipe_Goods.objects.filter(recipe_id=recipe.id)
    for req_good in req_goods:
        required_goods_list.append((req_good.goods.id, req_good.amount_required))
    storage_goods = Storage_Goods.objects.filter(storage_id=workshop.storage.id)
    for storage_good in storage_goods:
        owned_goods_list.append((storage_good.goods_data.id, storage_good.quantity))
        
    amount_produced = -1
    for reqed_good in required_goods_list:
        for owned_good in owned_goods_list:
            if reqed_good[0] == owned_good[0]:
                if amount_produced == -1: 
                    amount_produced = owned_good[1]/reqed_good[1]
                else: 
                    amount_produced = min(amount_produced, owned_good[1]/reqed_good[1])
                break
    return amount_produced

def UpdateGoods(workshop, workshop_recipe, amount):
    storage_goods = Storage_Goods.objects.get_or_create(storage_id = workshop.storage.id, goods_data_id=workshop_recipe.recipe.constructed_goods.id)
    storage_goods[0].quantity += amount
    storage_goods[0].save()
    
    req_goods = Recipe_Goods.objects.filter(recipe_id=workshop_recipe.recipe.id)
    storage_goods = Storage_Goods.objects.filter(storage_id=workshop.storage.id)
    for storage_good in storage_goods:
        for req_good in req_goods:
            if storage_good.goods_data.id == req_good.goods.id:
                storage_good.quantity -= req_good.amount_required * amount
                storage_good.save()