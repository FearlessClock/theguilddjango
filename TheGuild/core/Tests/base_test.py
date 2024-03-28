from django.test import TestCase
from TheGuild.core.Models.CountryModel import Country
from TheGuild.core.Models.CharacterModel import Character
from django.contrib.auth.models import User
from rest_framework.test import APIClient,force_authenticate
from rest_framework.authtoken.models import Token

class TestAuthBase(TestCase):
    user = None
    country = None
    
    def setUp(self):
        self.country = Country.objects.create(id=5, name="Japan")
        self.user = User.objects.create_user("test", "test@email.com", "test")
        self.user.save()
        self.client = APIClient()
        token = Token.objects.get_or_create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token[0].key)