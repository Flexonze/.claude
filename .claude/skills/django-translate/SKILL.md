---
name: django-translate
description: Process Django translations - update .po files and compile .mo files
---

# Django Translate

Update Django translation files (.po) with new translations and compile them to .mo files.

## Instructions

### 1. Run Initial Translation Extraction

Run `ntranslate` to extract new translatable strings and update .po files:

```bash
ntranslate
```

### 2. Identify Changed Translations

Check which .po files were modified to understand what needs translation:

```bash
git diff --name-only | grep "\.po$"
```

View the specific changes in all modified .po files:

```bash
git diff $(git diff --name-only | grep "\.po$")
```

Look for:
- New `msgid` entries that need `msgstr` translations
- Lines marked with `#, fuzzy` comments

### 3. Edit Translation Files

For each modified .po file found in step 2:

**Read the file** to see all untranslated or fuzzy entries.

**For each entry:**
- Remove `#, fuzzy` comments AND all the old commented-out translations that come with them (lines starting with `#|`)
- Add French Canadian translations in the `msgstr` field
- Follow Canadian French guidelines:
  - NO spaces before exclamation points (e.g., "Bonjour!" not "Bonjour !")
  - NO spaces before question marks (e.g., "Comment?" not "Comment ?")
  - NO spaces before colons or semicolons
  - Use Canadian French vocabulary and spelling

**Example:**
```
# Before
#, fuzzy
#| msgid "Old text"
msgid "Hello!"
msgstr ""

# After
msgid "Hello!"
msgstr "Bonjour!"
```

### 4. Reformat Translations

Run `ntranslate` again to fix formatting (line lengths, wrapping, etc.):

```bash
docker compose run --rm django python manage.py makemessages -l fr_CA --no-location
```

### 5. Compile Messages

Compile the .po files into .mo files:

```bash
docker compose run --rm django python manage.py compilemessages
```

### 6. Present Summary

Display a summary of translations that were added:

**If there are 10 or fewer new translations:**
- Show all translated messages with their English and French versions

**If there are more than 10 translations:**
- Show the first 5-10 examples
- Mention the total count
- Tell the user to check `git diff $(git diff --name-only | grep "\.po$")` to see the full list

**Example output format:**
```
Translations added:

1. "Hello!" → "Bonjour!"
2. "Welcome to the app" → "Bienvenue dans l'application"
3. "Save changes" → "Enregistrer les modifications"

Total: 3 new translations

Please review the translations to ensure they follow Canadian French guidelines and make sense in context.
```

## Guidelines

- Always remove ALL `#, fuzzy` comments and their associated commented-out old translations (lines starting with `#|`)
- Follow Canadian French punctuation rules (no spaces before !, ?, :, ;)
- Keep translations natural and contextually appropriate
- Verify .mo files are generated after compilation
- Present a clear summary so the user can verify translations
