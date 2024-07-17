from django.test import TestCase, SimpleTestCase
from django.urls import reverse

# Create your tests here.
class HomeTest(SimpleTestCase):
    def test_home_page_status(self):
        url = reverse('home')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_home_page(self):
        url = reverse('home')
        res = self.client.get(url)
        self.assertTemplateUsed(res, 'home.html')
        
class BookTest(TestCase):
    def test_book_page_status(self):
        url = reverse('book')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_book_page(self):
        url = reverse('book')
        res = self.client.get(url)
        self.assertTemplateUsed(res, 'book.html')


