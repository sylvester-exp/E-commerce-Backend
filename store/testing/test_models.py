from django.test import TestCase

from django.contrib.auth import get_user_model

User = get_user_model()


from store.models import Category, Product

class TestCategoriesModel(TestCase):
    
    def setUp(self):
        self.data1 = Category.objects.create(name ='django', slug ='django')

    def test_category_model_entry(self):

        data =self.data1
        self.assertTrue(isinstance(data, Category))
    
    def test_category_model_entry(self):

        data = self.data1
        self.assertEqual(str(data), 'django')

class TestProductsModel(TestCase):
    def setUp(self):
        Category.objects.create(name= 'django', slug = 'django')
        User.objects.create(email='admin@example.com', password='testpass')
        self.data1 = Product.objects.create(
            prod_title='django beginners', price='20.00', image='django',
            usage='education', subcategory='books'
)

        
    def test_products_model_entry(self):

        data = self.data1
        self.assertTrue(isinstance(data, Product))  
        self.assertEqual(str(data), 'django beginners') 


