
from unicodedata import name
from django.test import TestCase, Client
from django.urls import reverse
from .models import Product
from django.shortcuts import  get_object_or_404
from .forms import ProductForm




# Create your tests here.

class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client(vendor=True)
        
        self.products_url = reverse('products')
        self.product_detail_url = reverse('product_detail', args=[1])
        self.add_product_url = reverse('add_product')
        self.product1 = Product.objects.create(
            name='Test Product',
            description='Test Description',
            price=10.00,
            image='test_image.jpg',
            PDF = 'test_pdf.pdf',
            Guitar_Pro_Unlocked = 'test_guitar_pro_unlocked.gp',
            rating=5,
            vendor = 'TestVendor',
            )


    def test_get_products_page(self):
        page = self.client.get("/products/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products/products.html")

    
    def test_get_product_details_page(self):
        
        response = self.client.get(self.product_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/product_details2.html")    

    
    def test_add_product_page(self):
        
        response = self.client.post(self.add_product_url, data={
            'name': 'Test Product2',
            'description': 'Test Description',
            'price': 10.00,
            'image': 'test_image.jpg',
            'Guitar_Pro_Unlocked': 'test_guitar_pro_unlocked.gp',
            
            'vendor': 'TestVendor',
            'PDF': 'test_pdf.pdf',
        })
        
        
        products = get_object_or_404(Product, pk=2)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.products_url)
        self.assertEqual(products.name, 'Test Product2')
        
    def test_edit_product(self):
        response = self.client.post(reverse('edit_product', args=[1]), data={
            'name': 'Test Product2',
            'description': 'Test Description',
            'price': 10.00,
            'image': 'test_image.jpg',
            'Guitar_Pro_Unlocked': 'test_guitar_pro_unlocked.gp',
            
            'vendor': 'TestVendor',
            'PDF': 'test_pdf.pdf',
        })
        
        products = get_object_or_404(Product, pk=1)
        self.assertEqual(response.status_code, 302)
        
        self.assertEqual(products.name, 'Test Product2')

