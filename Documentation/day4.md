# Day 4: Models and Database in Django

## Table of Contents

1. [Introduction to ORM](#introduction-to-orm)
2. [Defining Models & Model Fields](#defining-models--model-fields)
3. [Relationships in Models](#relationships-in-models)
   - [OneToOne](#onetoone)
   - [ForeignKey](#foreignkey)
   - [ManyToMany](#manytomany)
4. [Migrations: makemigrations & migrate](#migrations-makemigrations--migrate)
5. [Best Practices](#best-practices)

---

## Introduction to ORM

**Object-Relational Mapping (ORM)** allows you to interact with your database using Python objects rather than writing raw SQL queries. Django’s ORM translates Python code to SQL, making database operations safer, faster, and more maintainable.

**Advantages:**

- Avoid SQL injection risks.
- Database-agnostic code.
- Easier to read and maintain.

---

## Defining Models & Model Fields

A **model** is a Python class that maps to a single table in your database. Each attribute in the model represents a database field.

**Example:**

```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    is_available = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
```

**Common Field Types:**

- `CharField`: Short text, needs `max_length`
- `TextField`: Long text
- `IntegerField`: Integer value
- `BooleanField`: True/False
- `DateField`, `DateTimeField`
- `FloatField`, `DecimalField`
- `EmailField`, `URLField`, `SlugField`
- `FileField`, `ImageField`

**Best Practices:**

- Always specify `max_length` for `CharField`.
- Use `choices` for fields with fixed options.
- Set `null=True` and `blank=True` thoughtfully.
- Use `verbose_name` for better admin readability.

---

## Relationships in Models

### OneToOne

Represents a 1:1 relationship. Often used for extending the `User` model.

```python
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
```

**Best Practice:** Use `on_delete=models.CASCADE` for closely related models.

---

### ForeignKey

Represents a many-to-one relationship. E.g., Each book belongs to one author, but an author can write many books.

```python
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
```

**Best Practice:** Always set `on_delete` (e.g., `CASCADE`, `SET_NULL`).

---

### ManyToMany

Represents a many-to-many relationship. E.g., Books and Genres.

```python
class Genre(models.Model):
    name = models.CharField(max_length=50)

class Book(models.Model):
    title = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre)
```

**Best Practice:** Use `related_name` for reverse access.

---

## Migrations (makemigrations & migrate)

**Migrations** are Django’s way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema.

### Workflow

- `python manage.py makemigrations`
  - Detects model changes and creates migration files.
- `python manage.py migrate`
  - Applies migrations to the database.

**Best Practices:**

- Run `makemigrations` after every model change.
- Review migration files before applying.
- Use version control to track migration files.
- Avoid editing migration files manually unless necessary.

---

## Best Practices

- **Model Design:** Keep models lean. Use custom managers for complex queries.
- **Field Naming:** Be explicit, avoid ambiguous names.
- **Indexes:** Use `db_index=True` for fields frequently queried.
- **Meta Options:** Use `class Meta` for table name, ordering, and verbose names.
- **Data Integrity:** Leverage validators and constraints (`unique`, `choices`, `validators`).

---
