---
argument-hint: <app-name>
description: Create a new Django app with proper structure and configuration
---

# Create Django App

Create a new Django app named `$1` with proper setup and an organized file structure.

## Instructions

### 1. Generate the App Structure

Run the Django management command to create the app:

```bash
python manage.py startapp $1
```

### 2. Create URLs Configuration

Django doesn't create a `urls.py` file by default. Create `$1/urls.py` with:

```python
from django.urls import path

app_name = "$1"

urlpatterns = []
```

### 3. Register in Settings

Add the app to `INSTALLED_APPS` in the project's settings file:

```python
INSTALLED_APPS = [
    # ... existing apps
    '$1.apps.$1Config',  # Use PascalCase for the config class name
]
```

### 4. Connect Project URLs

Add the app's URLs to the main project `urls.py`:

```python
path('$1/', include('$1.urls')),
```

### 5. Reorganize File Structure

Replace single files with organized directories for better scalability:

**Create these directories with `__init__.py` files:**
- `$1/models/`
- `$1/views/`
- `$1/admin/`
- `$1/tests/`

**Remove the original single files** (`models.py`, `views.py`, `admin.py`, `tests.py`) after creating the directories.

### 6. Enhance Test Organization

Create test subdirectories:
- `$1/tests/factories/` - for test fixtures and factories
- `$1/tests/test_models.py`
- `$1/tests/test_views.py`

### 7. Add Optional Directories (as needed)

Create any of these based on the app's requirements:
- `$1/forms/`
- `$1/serializers/`
- `$1/tasks/`
- `$1/templates/$1/`
- `$1/permissions/`
- `$1/managers/`

### 8. Implement Module Imports

For each directory with multiple files, re-export in `__init__.py` for cleaner imports:

```python
# $1/models/__init__.py
from .example_model import ExampleModel

__all__ = ["ExampleModel"]
```

## Notes

- Use snake_case for the app name
- The Config class in apps.py uses PascalCase (e.g., `DashboardConfig` for app `dashboard`)
- Always run `python manage.py makemigrations $1` after creating models
