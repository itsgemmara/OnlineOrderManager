import random
import string
from rest_framework.test import APITestCase, APITransactionTestCase, APIClient, APIRequestFactory
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import Table, Category, Material, Menu, Order, Pay, Product
from .utils import test_model_object_creator

# --------------------------------------------database------------------------------------------------------------------


class ModelTestCase(APITransactionTestCase):

    reset_sequences = True

    def setUp(self):
        image_name = ''.join(random.choices(string.ascii_lowercase, k=5))
        self.char = 'test_char'
        self.text = 'test text'
        self.bool = False
        self.float = 2.5
        self.int = 55
        self.image = SimpleUploadedFile(
            name=f'{image_name}.jpg',
            content=open('Order/random.jpg', 'rb').read(),
            content_type='image/jpeg',
        )

    def test_table(self):
        obj = Table.objects.create(name='test_name', info='test info')
        self.assertEqual(1, obj.pk)
        self.assertEqual('test_name', obj.name)
        self.assertEqual('test info', obj.info)
        self.assertEqual(True, obj.is_active)

    def test_category(self):
        obj = Category.objects.create(name='test_name', )
        self.assertEqual('test_name', obj.name)

    def test_material(self):
        obj = Material.objects.create(name='test_name', unit='one_gr', unit_price=2.5, description='test des')
        self.assertEqual(2.5, obj.unit_price)
        self.assertEqual('test_name', obj.name)
        self.assertEqual('test des', obj.description)
        self.assertEqual('one_gr', obj.unit)

    def test_menu(self):
        cat = test_model_object_creator(Category)
        obj = Menu.objects.create(name=self.char, cat=cat, price=self.float, image=self.image)
        self.assertEqual(cat, obj.cat)
        self.assertEqual(self.char, obj.name)
        self.assertEqual(self.float, obj.price)
        self.assertEqual(self.image, obj.image)

    def test_order(self):
        obj = Order.objects.create(product=self.char, description=self.text, table=self.char,
                                   is_ready=self.bool, is_payed=self.bool)
        self.assertEqual(self.char, obj.product)
        self.assertEqual(self.char, obj.table)
        self.assertEqual(self.bool, obj.is_payed)
        self.assertEqual(self.bool, obj.is_ready)
        self.assertEqual(self.text, obj.description)

    def test_product(self):
        order = test_model_object_creator(Menu)
        obj = Product.objects.create(order=order, materials=self.text, description=self.text)
        self.assertEqual(order, obj.order)
        self.assertEqual(self.text, obj.materials)
        self.assertEqual(self.text, obj.description)

    def test_pay(self):
        table = test_model_object_creator(Table)
        obj = Pay.objects.create(table=table, total_price=str(self.float), products=self.char, success=self.bool)
        self.assertEqual(table, obj.table)
        self.assertEqual(self.char, obj.products)
        self.assertEqual(str(self.float), obj.total_price)
        self.assertEqual(self.bool, obj.success)

# --------------------------------------- view set actions -------------------------------------------------------------


class TableTestCase(APITestCase):

    def setUp(self):
        self.table = Table.objects.create(name='table_name_setup', info='table info setup', is_active=True)
        self.table2 = Table.objects.create(name='table_name_setup2', info='table info setup', is_active=True)
        self.data = {"name": 'table_name', "info": 'test table info', }

    def test_create(self):
        response = self.client.post("/table-view-set/", self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'table_name')
        self.assertEqual(response.data['info'], 'test table info')

    def test_put(self):
        data = {"name": 'new_name_setup', 'info': 'new info setup'}
        response = self.client.put(f"/table-view-set/{self.table.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        table_obj = Table.objects.get(id=self.table.id)
        self.assertEqual(table_obj.name, data['name'])
        self.assertEqual(table_obj.info, data['info'])

    def test_patch(self):
        data = {"name": 'new_name_setup_patch', }
        response = self.client.patch(f"/table-view-set/{self.table.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        table_obj = Table.objects.get(id=self.table.id)
        self.assertEqual(table_obj.name, data['name'])

    def test_destroy(self):
        response = self.client.delete(f"/table-view-set/{self.table.id}/", )
        response2 = self.client.delete(f"/table-view-set/{self.table.id}/", )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response2.status_code, status.HTTP_404_NOT_FOUND)

    def test_retrieve(self):
        table_obj = Table.objects.get(id=self.table.id)
        response = self.client.get(f"/table-view-set/{self.table.id}/", )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(table_obj.name, response.data['name'])
        self.assertEqual(table_obj.info, response.data['info'])

    def test_list(self):
        response = self.client.get("/table-view-set/", )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_change_table_is_active(self):
    #     response = self.client.get("table-view-set/change_table_is_active/",
    #                                data={"table": self.table.name, "choices": "activate"})
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)


class UtilsTestCase(APITestCase):

    def setUp(self):
        self.table = Table.objects.create(name='table_name_setup', info='table info setup', )
        self.table2 = Table.objects.create(name='table_name_setup2', info='table info setup', )

    def test_create_choices(self):
        pass


