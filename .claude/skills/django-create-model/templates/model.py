# {{app_name}}/models/{{model_name_snake}}.py
from django.db import models
from core.models import UUIDModel
from django_extensions.db.models import TimeStampedModel


class {{model_name}}(UUIDModel, TimeStampedModel):
    title = models.CharField(max_length=512)
    description = models.CharField(max_length=2000, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="{{model_name_snake}}s")

    def __str__(self):
        return self.title
