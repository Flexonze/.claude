# {{app_name}}/tests/factories/{{model_name_snake}}_factory.py
import factory
from {{app_name}} import models
from accounts.tests.factories import UserFactory


class {{model_name}}Factory(factory.django.DjangoModelFactory):
    title = factory.Faker("sentence", nb_words=5)
    description = factory.Faker("text", max_nb_chars=300)
    created_by = factory.SubFactory(UserFactory)

    class Meta:
        model = models.{{model_name}}
