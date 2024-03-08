from TheGuild.core.Models.CountryModel import Country
from TheGuild.core.Models.WorkshopModel import Workshop

from datetime import datetime, UTC

def TickCountry(countryID):
    country = Country.objects.get(id=countryID)
    secondsSinceLastUpdate = (datetime.now(UTC) - country.last_update).total_seconds()
    if secondsSinceLastUpdate > country.tick_in_seconds:
        country.last_update = datetime.now(UTC)
        country.tick = int((datetime.now(UTC) - country.country_start_date).total_seconds() / country.tick_in_seconds)
        country.save()
        
    print(str(secondsSinceLastUpdate))
    
    
    