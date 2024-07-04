from django.test import TestCase
from django.shortcuts import reverse

# Create your tests here.
class TestPages(TestCase):

    #home Page Test
    def test_home_page_by_url(self):
        respone = self.client.get('')
        self.assertEqual(respone.status_code, 200)
    
    def test_home_page_by_name(self):
        respone = self.client.get(reverse('home'))
        self.assertEqual(respone.status_code, 200)

    #About US Page Test
    def test_aboutus_page_by_url(self):
        respone = self.client.get('/aboutus/')
        self.assertEqual(respone.status_code, 200)

    def test_aboutus_page_by_name(self):
        respone = self.client.get(reverse('aboutus'))
        self.assertNotEqual(respone.status_code, 404)