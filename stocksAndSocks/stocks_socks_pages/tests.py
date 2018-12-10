from django.test import SimpleTestCase

class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        
    def test_socks_page_status_code(self):
        response = self.client.get('/socks/')
        self.assertEqual(response.status_code, 200)

    def test_stocks_page_status_code(self):
        response = self.client.get('/stocks/')
        self.assertEqual(response.status_code, 200)

    def test_purchase_page_status_code(self):
        response = self.client.get('/purchase/')
        self.assertEqual(response.status_code, 200)
