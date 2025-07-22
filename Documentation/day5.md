# Django Day 4: Model Managers & QuerySets

Mastering Django's ORM is key to building powerful, efficient applications. Today’s topics—Model Managers, QuerySets, filtering, ordering, chaining queries, custom managers, and aggregation—are the backbone of Django database interaction. Below you'll find in-depth explanations, code examples, and best practices for each topic.

---

## 1. **Model Managers and QuerySets**

### **What are Model Managers?**

- **Model Manager** is a class that manages database query operations for Django models.
- Every Django model has at least one manager—`objects` by default.

#### **Example:**

```python
class Book(models.Model):
    title = models.CharField(max_length=200)
    published = models.DateField()
    # 'objects' is the default manager
```

### **What are QuerySets?**

- **QuerySet** is a collection of database queries to retrieve objects from the database.
- They are lazy—queries aren't executed until you iterate or explicitly request the data.

#### **Example:**

```python
books = Book.objects.all()  # Returns a QuerySet of all Book objects
```

---

## 2. **Filtering, Ordering, Chaining Queries**

### **Filtering**

- Use `.filter()` to get objects matching certain criteria.
- Use `.exclude()` to get objects NOT matching certain criteria.

#### **Example:**

```python
recent_books = Book.objects.filter(published__year__gte=2020)
old_books = Book.objects.exclude(published__year__gte=2020)
```

#### **Best Practices:**

- **Chaining:** Filter, exclude, and order can be chained for complex queries.
- **Use lookups:** e.g., `__icontains`, `__gte`, `__lte`, etc.

### **Ordering**

- Use `.order_by()` to sort query results.

#### **Example:**

```python
books_ordered = Book.objects.order_by('title')      # Ascending by title
books_desc = Book.objects.order_by('-published')    # Descending by published date
```

### **Chaining Queries**

- QuerySets are chainable, allowing you to build complex queries step by step.

#### **Example:**

```python
books = Book.objects.filter(published__year=2023).order_by('-title')
```

#### **Best Practice:**

- **Minimize queries**: Chain methods before data retrieval to optimize performance.

---

## 3. **Custom Model Managers**

### **Why Custom Managers?**

- Encapsulate common queries or logic.
- Make your code DRY (Don’t Repeat Yourself).

### **How to Create a Custom Manager**

#### **Example:**

```python
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)

class Article(models.Model):
    title = models.CharField(max_length=200)
    is_published = models.BooleanField(default=False)

    objects = models.Manager()        # The default manager.
    published = PublishedManager()    # Our custom manager.
```

#### **Usage:**

```python
Article.published.all()  # Returns only published articles
```

#### **Best Practices:**

- **Add custom methods** for reusable query logic.
- **Always keep the default manager** (`objects`) for admin compatibility, unless you have a good reason.

---

## 4. **Aggregations & Annotations**

### **Aggregations**

- Use `aggregate()` to calculate values over a QuerySet (sum, average, min, max, count).

#### **Example:**

```python
from django.db.models import Avg, Count, Max, Min, Sum

stats = Book.objects.aggregate(
    total=Count('id'),
    avg_pub_year=Avg('published__year'),
    latest_pub=Max('published'),
)
```

### **Annotations**

- Use `annotate()` to add calculated fields to each object in the QuerySet.

#### **Example:**

```python
from django.db.models import Count

authors = Author.objects.annotate(book_count=Count('book'))
for author in authors:
    print(author.name, author.book_count)
```

#### **Best Practices:**

- **Use select_related/prefetch_related** for related object queries to reduce DB hits.
- **Keep aggregates simple** for performance.
- **Use annotations for display and reporting, not for filtering**—filtering annotated fields can be tricky.

---

## **Summary & Best Practices**

- Use QuerySets efficiently: always chain filters, excludes, and orderings before retrieving data.
- Custom managers make code easier to maintain and more expressive.
- Aggregations and annotations power advanced reporting, but use judiciously for performance.
- Avoid N+1 queries by leveraging related object optimizations.
- Always test and profile database queries for large datasets.

---

## **References**

- [Django Model Managers](https://docs.djangoproject.com/en/4.2/topics/db/managers/)
- [QuerySets Documentation](https://docs.djangoproject.com/en/4.2/ref/models/querysets/)
- [Aggregation](https://docs.djangoproject.com/en/4.2/topics/db/aggregation/)
- [Best Practices for Django ORM](https://realpython.com/django-orm-best-practices/)
