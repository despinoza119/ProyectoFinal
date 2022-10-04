from django.test import TestCase

# Create your tests here.

from AppCoder.models import Tenis

class TenisModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Tenis.objects.create(nombre_equipo='Rafael Nadal',altura='1,85m',nacimiento='1986-06-03',apodo='Rafa',pais='España')

    def test_nombre_equipo_label(self):
        tenis=Tenis.objects.get(nombre_equipo='Rafael Nadal')
        field_label = tenis._meta.get_field('nombre_equipo').verbose_name
        self.assertEquals(field_label,'nombre equipo')

    def test_nacimiento_label(self):
        tenis=Tenis.objects.get(nombre_equipo='Rafael Nadal')
        field_label = tenis._meta.get_field('nacimiento').verbose_name
        self.assertEquals(field_label,'nacimiento')

    def test_nombre_equipo_max_length(self):
        tenis=Tenis.objects.get(nombre_equipo='Rafael Nadal')
        max_length = tenis._meta.get_field('nombre_equipo').max_length
        self.assertEquals(max_length,40)
