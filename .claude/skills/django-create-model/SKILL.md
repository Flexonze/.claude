---
name: django-create-model
description: Create a new Django model
argument-hint: [app-name] [model-name] [model-name-snake] [custom-instruction]
disable-model-invocation: true
---

# Create Django Model

Create a new Django model named {{model_name}} following an opinionated checklist.

**Arguments:**

- `app-name` - The django app in which to create the new model
- `model-name` - CamelCase name (e.g., TeamProject)
- `model-name-snake` - snake_case version (e.g., team_project)
- `custom-instruction` - Any custom instructions (fields, etc.)

**Example:** `/django-create-model my_app TeamProject team_project`

## Templates

Use these templates as starting points, adapting field names and relationships as needed:

- [Model template](templates/model.py) - Base model structure
- [Model tests template](templates/model_test.py) - Unit tests for the model
- [Factory template](templates/factory.py) - Factory Boy factory for testing
- [Admin template](templates/admin.py) - Django admin configuration
- [Admin tests template](templates/admin_test.py) - Admin page tests with query assertions

## Instructions

**IMPORTANT: Complete ALL 9 steps below. Do not skip any step.**

### 1. The Model

- Create the model file `{{app_name}}/models/{{model_name_snake}}.py` using [model template](templates/model.py)
- Create the model class inheriting from `UUIDModel` and `TimeStampedModel`
- Define the `__str__` method
- Import the model in `{{app_name}}/models/__init__.py`

### 2. The Migration

- Generate the migration: `docker compose run --rm api python manage.py makemigrations {{app_name}}`
- Review the generated migration file
- Execute the migration: `docker compose run --rm api python manage.py migrate`

### 3. Model Tests

- Create test file `{{app_name}}/tests/models/test_{{model_name_snake}}.py` using [model tests template](templates/model_test.py)
- Implement tests:
  - `test_can_create_a_{{model_name_snake}}`
  - `test_can_print_a_{{model_name_snake}}`

### 4. Factory

- Create factory file `{{app_name}}/tests/factories/{{model_name_snake}}_factory.py` using [factory template](templates/factory.py)
- Use `factory.Faker()` for generating dummy data
- Import factory in `{{app_name}}/tests/factories/__init__.py`

### 5. Factory Tests

- Add factory test to the model test file (included in [model tests template](templates/model_test.py))
- Test factory functionality
- Verify object creation works correctly

### 6. Admin Pages

- Create admin file `{{app_name}}/admin/{{model_name_snake}}_admin.py` using [admin template](templates/admin.py)
- Override `get_queryset` to use `select_related` or `prefetch_related` if the model contains ForeignKey or ManyToManyField
- Import admin in `{{app_name}}/admin/__init__.py`

### 7. Admin Page Tests

- Create admin test file `{{app_name}}/tests/admin/test_{{model_name_snake}}_admin.py` using [admin tests template](templates/admin_test.py)
- Test changelist, add, and change pages
- Include query count assertions to prevent N+1 queries

### 8. Run Tests

- Run the tests for the app: `docker compose run --rm api python manage.py test {{app_name}}`
- If tests fail, fix the issues (update tests, fix imports, adjust model code, etc.) and re-run tests
- Iterate until all tests pass

### 9. Format Code

- Run `nformat` to format code with black, isort and fix flake8 issues
