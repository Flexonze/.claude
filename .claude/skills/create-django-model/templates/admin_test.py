# {{app_name}}/tests/admin/test_{{model_name_snake}}_admin.py
from django.test import TestCase, Client
from django.urls import reverse
from {{app_name}}.tests import factories


class Test{{model_name}}Admin(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = factories.UserFactory(is_superuser=True)
        cls.{{model_name_snake}}s = factories.{{model_name}}Factory.create_batch(6)

    def setUp(self):
        self.client.force_login(self.user)

    def test_changelist(self):
        url = reverse("admin:{{app_name}}_{{model_name_snake}}_changelist")

        with self.assertNumQueries(5):  # Make sure this number doesn't increase if the number of objects created in setUpTestData increases.
            response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_add(self):
        url = reverse("admin:{{app_name}}_{{model_name_snake}}_add")

        with self.assertNumQueries(5):
            response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_change(self):
        url = reverse(
            "admin:{{app_name}}_{{model_name_snake}}_change", kwargs={"object_id": self.{{model_name_snake}}s[0].id}
        )

        with self.assertNumQueries(5):
            response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
