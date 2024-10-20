from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import Menu
from .serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        #create the user and authenticate
        # Create a user and authenticate
        self.user = User.objects.create_user(username="theo", password="theo")
        self.client = APIClient()
        self.client.login(username="theo", password="theo")


        #create the menu items
        self.item1 = Menu.objects.create(ID=1,Title="Burger",Price=12.99,Inventory=3)
        self.item2 = Menu.objects.create(ID=2,Title="Pasta",Price=13.99,Inventory=5)
        self.item3 = Menu.objects.create(ID=3,Title="Salad",Price=8.99,Inventory=4)
    def test_getall(self):
        response = self.client.get('/restaurant/menu/items/')
        items = Menu.objects.all()
        serializer = MenuSerializer(items,many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)