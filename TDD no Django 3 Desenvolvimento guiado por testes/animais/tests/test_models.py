from django.test import TestCase, RequestFactory
from animais.models import Animal

class AnimalModelTestCase(TestCase):

    def setUp(self):
        self.animal = Animal.objects.create(
            nome_animal = 'leão',
            predador = 'Sim',
            venenoso = 'Não',
            domestico = 'Não',
        )
    
    def test_animal_cadastrado_com_caracteristicas(self):
        """Teste que verifica se o animal está cadastrado com suas respectivas características"""
        self.assertEqual(self.animal.nome_animal, 'leão')
        self.assertEqual(self.animal.predador, 'Sim')
        self.assertEqual(self.animal.venenoso, 'Não')
        self.assertEqual(self.animal.domestico, 'Não')