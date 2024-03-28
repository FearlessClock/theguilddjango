from django.test import TestCase
import json
from TheGuild.core.Models.CountryModel import Country
from TheGuild.core.Models.CharacterModel import Character
from .base_test import TestAuthBase


class CountryModelTests(TestAuthBase):
    def test_create_country(self):
        country = Country.objects.create(id=7, name="Spain")
        self.assertIs(country.id, 7)
        self.assertIs(country.name, "Spain")
        
class CharacterModelTests(TestAuthBase):
    user = None
    country = None
    
    def test_create_character(self):
        char = Character.objects.create(id=5, name="James", user=self.user, country=self.country, money=100)
        self.assertIs(char.money, 100)
        self.assertIs(char.name, "James")
        
    def test_get_character_by_country(self):
        Character.objects.create(id=5, name="James", user=self.user, country=self.country, money=100)

        resp = self.client.get('/api/character/5/')
        self.assertIs(resp.status_code, 200)
        self.assertIs(resp.json()[0]['id'], 5)
        
    def test_get_character_by_country_no_chars(self):
        Character.objects.create(id=5, name="James", user=self.user, country=self.country, money=100)

        resp = self.client.get('/api/character/1/')
        self.assertIs(resp.status_code, 200)
        self.assertIs(len(resp.json()), 0)