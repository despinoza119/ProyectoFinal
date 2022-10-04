from django.test import TestCase

# Create your tests here.

from AppCoder.models import Basket

class BasketModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Basket.objects.create(nombre_equipo='Boston Celtics',entrenador='Ime Udoka',fundacion='1955-09-30',apodo='No especifica',ubicacion='Boston (Massachusetts)')

    def test_nombre_equipo_label(self):
        basket=Basket.objects.get(nombre_equipo='Boston Celtics')
        field_label = basket._meta.get_field('nombre_equipo').verbose_name
        self.assertEquals(field_label,'nombre equipo')

    def test_fundacion_label(self):
        basket=Basket.objects.get(nombre_equipo='Boston Celtics')
        field_label = basket._meta.get_field('fundacion').verbose_name
        self.assertEquals(field_label,'fundacion')

    def test_nombre_equipo_max_length(self):
        basket=Basket.objects.get(nombre_equipo='Boston Celtics')
        max_length = basket._meta.get_field('nombre_equipo').max_length
        self.assertEquals(max_length,40)
