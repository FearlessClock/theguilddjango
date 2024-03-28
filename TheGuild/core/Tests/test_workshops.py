from django.test import TestCase
import json
from TheGuild.core.Models.WorkshopModel import Workshop,Workshop_Recipe
from TheGuild.core.Models.GoodsModel import Recipe
from TheGuild.core.Models.CharacterModel import Character
from TheGuild.core.Models.CountryModel import GridPoint, Country
from TheGuild.core.Models.BuildingModel import Building
from TheGuild.core.Models.StorageModel import Storage
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .base_test import TestAuthBase

class WorkshopModelTest(TestAuthBase):
    def setUp(self):
        super().setUp()
        self.char = Character.objects.create(id=10,country=Country.objects.get(id=2), user=self.user, name='Tester', money=0)
        grid_point = GridPoint.objects.get(x=4,y=2, country=self.char.country )
        building = Building.objects.create(country=self.char.country, grid_point=grid_point, type="Tester", name="Shop Test")
        grid_point.has_building = True
        grid_point.save()
        storage = Storage.objects.create(number_of_storage_spaces=1)
        self.workshop = Workshop.objects.create(id=10, building=building, character=self.char, storage=storage)
        Workshop_Recipe.objects.create(
            workshop = self.workshop,
            recipe = Recipe.objects.get(id=1),
            is_available = True
        )
        
    def test_create_workshop(self):
        char = Character.objects.get(id=1)
        grid_point = GridPoint.objects.get(x=1,y=2, country=char.country )
        building = Building.objects.create(country=char.country, grid_point=grid_point, type="test", name="test")
        grid_point.has_building = True
        grid_point.save()
        storage = Storage.objects.create(number_of_storage_spaces=2)
        workshop = Workshop.objects.create(id=5, building=building, character=char, storage=storage)
        self.assertIs(workshop.id, 5)
        
    def test_detail_workshop(self):
        workshop = Workshop.objects.get(id=1)

        resp = self.client.get('/api/workshop/1/')
        self.assertIs(workshop.id, resp.json()["id"])
        
    def test_workshop_by_country(self):
        token = Token.objects.get_or_create(user=User.objects.get(username='AmusedSandpaper'))
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token[0].key)
        resp = self.client.get('/api/workshops/1/')
        self.assertIs(1, resp.json()[0]["id"])
        
    def test_workshop_not_in_country(self):
        token = Token.objects.get_or_create(user=User.objects.get(username='AmusedSandpaper'))
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token[0].key)
        resp = self.client.get('/api/workshops/3/')
        self.assertIs(0, len(resp.json()))
        
    def test_workshop_in_country_and_by_char(self):
        token = Token.objects.get_or_create(user=User.objects.get(username='AmusedSandpaper'))
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token[0].key)
        resp = self.client.get('/api/workshops/character/1/')
        self.assertIs(1, len(resp.json()))
        self.assertIs(1, resp.json()[0]["id"])
        
    def test_workshop_hire_employee(self):
        resp = self.client.post('/api/workshop/hire/', data={'workshopID':10}, format='json')
        self.assertIs(resp.status_code, 200)
        self.assertIs(resp.json()['success'], True)
        resp = self.client.post('/api/workshop/hire/', data={'workshopID':10}, format='json')
        self.assertIs(resp.json()['success'], False)
        
    def test_workshop_fire_employee(self):
        resp = self.client.delete('/api/workshop/hire/', data={'employeeID':1}, format='json')
        self.assertIs(resp.status_code, 200)
        self.assertIs(resp.json()['success'], True)
        resp = self.client.delete('/api/workshop/hire/', data={'workshopID':1}, format='json')
        self.assertIs(resp.json()['success'], False)
        
    def test_give_employee_job(self):
        resp = self.client.post('/api/workshop/hire/', data={'workshopID':10}, format='json')
        resp = self.client.post('/api/workshop/give-recipe/', data={'employeeID':1, 'recipeID':1}, format='json')
        self.assertIs(resp.json()['success'], True)
        
    def test_remove_employee_job(self):
        resp = self.client.post('/api/workshop/hire/', data={'workshopID':10}, format='json')
        resp = self.client.post('/api/workshop/give-recipe/', data={'employeeID':1, 'recipeID':1}, format='json')
        self.assertIs(resp.json()['success'], True)
        resp = self.client.delete('/api/workshop/give-recipe/', data={'employeeID':1}, format='json')
        self.assertIs(resp.json()['success'], True)
        
    def test_get_all_recipes(self):
        resp = self.client.get('/api/workshop/1/get-recipe/')
        self.assertIs(len(resp.json()), 2)