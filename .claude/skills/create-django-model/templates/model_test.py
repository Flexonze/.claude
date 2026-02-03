# {{app_name}}/tests/models/test_{{model_name_snake}}.py
from django.test import TestCase
from {{app_name}}.models import {{model_name}}
from {{app_name}}.tests.factories import {{model_name}}Factory
from accounts.models import User


class Test{{model_name}}(TestCase):
    def test_can_create_a_{{model_name_snake}}(self):
        {{model_name_snake}} = {{model_name}}(
            title="title",
            description="description",
            created_by=User.objects.create(email="email@example.com")
        )

        {{model_name_snake}}.full_clean()
        {{model_name_snake}}.save()

    def test_can_print_a_{{model_name_snake}}(self):
        {{model_name_snake}} = {{model_name}}(
            title="title",
            description="description",
            created_by=User.objects.create(email="email@example.com")
        )
        expected_str = "title"

        self.assertEqual(str({{model_name_snake}}), expected_str)

    def test_factory_can_create_{{model_name_snake}}(self):
        {{model_name_snake}} = {{model_name}}Factory()
        self.assertIsNotNone({{model_name_snake}}.id)
