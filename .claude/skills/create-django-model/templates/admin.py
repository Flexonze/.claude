# {{app_name}}/admin/{{model_name_snake}}_admin.py
from django.contrib import admin
from {{app_name}}.models import {{model_name}}


@admin.register({{model_name}})
class {{model_name}}Admin(admin.ModelAdmin):
    list_display = ["title", "created_by", "created"]
    search_fields = ["title", "description"]
    list_filter = ["created"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.select_related("created_by")
        return queryset
