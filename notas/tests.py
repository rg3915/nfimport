from django.contrib.auth.models import AnonymousUser, User, Group
from django.test import RequestFactory, TestCase
from django.urls import reverse
from django.utils import timezone

from .forms import ProductForm
from .models import Nota, Product
from .views import product_list, product_create, nota_list, nota_create, nota_update


class NotasViewsTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='jacob', email='jacob@…', password='top_secret')
        self.group = Group.objects.create(name='Testes')
        self.group.user_set.add(self.user)

        # Nota
        self.nota = Nota.objects.create(description='Nota Teste', date=timezone.now(), dolar_dia=3.33)

        # Produto
        self.product = Product.objects.create(maquina_pt='Maquina teste',
                                              tipo_pt='tipo teste',
                                              modelo_pt='ZM-Teste',
                                              area_trabalho_pt='66x66',
                                              eixo_z_pt='22',
                                              cor_pt='Azul',
                                              faz_pt='Faz testes',
                                              voltagem_pt='110v',
                                              ncm='111.222.333')

    def test_product_list_anonimo(self):
        request = self.factory.get('/products')
        request.user = AnonymousUser()

        response = product_list(request)
        self.assertEqual(response.status_code, 302)

    def test_product_list_logado(self):
        request = self.factory.get('/products')
        request.user = self.user

        response = product_list(request)
        self.assertEqual(response.status_code, 200)

    def test_product_create_anonimo(self):
        request = self.factory.get('/products')
        request.user = AnonymousUser()

        response = product_create(request)
        self.assertEqual(response.status_code, 302)

    def test_product_create_logado(self):
        request = self.factory.get('/products')
        request.user = self.user

        response = product_create(request)
        self.assertEqual(response.status_code, 200)

    def test_product_create_form_is_valid(self):
        form_data = {'maquina_pt': 'Maquina teste',
                     'tipo_pt': 'tipo teste',
                     'modelo_pt': 'ZM-Teste',
                     'area_trabalho_pt': '66x66',
                     'eixo_z_pt': '22',
                     'cor_pt': 'Azul',
                     'faz_pt': 'Faz testes',
                     'voltagem_pt': '110v',
                     'ncm': '111.222.333'}
        form = ProductForm(data=form_data)
        self.assertEqual(form.is_valid(), True)

    def test_product_create_form_invalid(self):
        form_data = {'maquina_pt': '',
                     'tipo_pt': 'tipo teste'}

        form = ProductForm(data=form_data)
        self.assertEqual(form.is_valid(), False)

    def test_product_view_create(self):
        form_data = {'maquina_pt': 'Maquina teste',
                     'tipo_pt': 'tipo teste',
                     'modelo_pt': 'ZM-Teste',
                     'area_trabalho_pt': '66x66',
                     'eixo_z_pt': '22',
                     'cor_pt': 'Azul',
                     'faz_pt': 'Faz testes',
                     'voltagem_pt': '110v',
                     'ncm': '111.222.333'}

        self.client.force_login(self.user)
        response = self.client.post(reverse('product_create'), form_data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('product_list'))

    def test_product_view_update(self):
        product = self.product
        self.client.force_login(self.user)
        response = self.client.post(reverse('product_update', kwargs={'pk': product.id}),
                                    data={'maquina_pt': 'Maquina teste',
                                          'tipo_pt': 'tipo teste',
                                          'modelo_pt': 'ZM-Teste',
                                          'area_trabalho_pt': '77x77',
                                          'eixo_z_pt': '22',
                                          'cor_pt': 'Verde',
                                          'faz_pt': 'Faz testes',
                                          'voltagem_pt': '110v',
                                          'ncm': '111.222.333'})

        self.assertEqual(response.status_code, 302)
        product.refresh_from_db()
        self.assertEqual(product.area_trabalho_pt, '77x77')
        self.assertEqual(product.cor_pt, 'Verde')

    def test_product_view_update_invalid(self):
        product = self.product
        self.client.force_login(self.user)
        response = self.client.post(reverse('product_update', kwargs={'pk': product.id}),
                                    data={'maquina_pt': ''})

        self.assertEqual(response.status_code, 200)
        product.refresh_from_db()
        self.assertEqual(product.maquina_pt, 'Maquina teste')

    def test_notas_list_anonimo(self):
        request = self.factory.get('/notas')
        request.user = AnonymousUser()

        response = nota_list(request)
        self.assertEqual(response.status_code, 302)

    def test_notas_list_logado(self):
        request = self.factory.get('/notas')
        request.user = self.user

        response = nota_list(request)
        self.assertEqual(response.status_code, 200)

    def test_nota_create_anonimo(self):
        request = self.factory.get('/nota/add')
        request.user = AnonymousUser()

        response = nota_create(request)
        self.assertEqual(response.status_code, 302)

    def test_nota_create_logado(self):
        request = self.factory.get('/nota/add')
        request.user = self.user

        response = nota_create(request)
        self.assertEqual(response.status_code, 200)

    def test_nota_update_anonimo(self):
        request = self.factory.get('/nota/edit/')
        request.user = AnonymousUser()

        response = nota_update(request, pk=self.nota.pk)
        self.assertEqual(response.status_code, 302)

    def test_nota_update_logado(self):
        request = self.factory.get('/nota/edit/')
        request.user = self.user

        response = nota_update(request, pk=self.nota.pk)
        self.assertEqual(response.status_code, 200)
