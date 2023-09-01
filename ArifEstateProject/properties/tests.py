from django.test import TestCase
from .models import Property

class PropertyModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Property.objects.create(title='Test Property', price=1000.0, description='This is a test property.')

    def test_title_label(self):
        property = Property.objects.get(id=1)
        field_label = property._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_price_label(self):
        property = Property.objects.get(id=1)
        field_label = property._meta.get_field('price').verbose_name
        self.assertEquals(field_label, 'price')

    def test_description_label(self):
        property = Property.objects.get(id=1)
        field_label = property._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_title_max_length(self):
        property = Property.objects.get(id=1)
        max_length = property._meta.get_field('title').max_length
        self.assertEquals(max_length, 200)

    def test_price_decimal_places(self):
        property = Property.objects.get(id=1)
        decimal_places = property._meta.get_field('price').decimal_places
        self.assertEquals(decimal_places, 2)

    def test_price_max_digits(self):
        property = Property.objects.get(id=1)
        max_digits = property._meta.get_field('price').max_digits
        self.assertEquals(max_digits, 10)

    def test_description_help_text(self):
        property = Property.objects.get(id=1)
        help_text = property._meta.get_field('description').help_text
        self.assertEquals(help_text, 'Enter a description for the property.')

    def test_property_string_representation(self):
        property = Property.objects.get(id=1)
        expected_output = f'{property.title} - Price: ${property.price:2f}'
        self.assertEquals(str(property), expected_output)
