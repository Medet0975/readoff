from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.

User = get_user_model()


class Books(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    author = models.CharField(max_length=150, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='post_image', max_length=255)
    # book = models.FileField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    published = models.CharField(max_length=10)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    cat_id = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)

    def get_absolute_url(self):
        return reverse('books_detail',
                       kwargs={'books_detail': self.slug})

    def __str__(self):
        return f'{self.name} -> {self.author}'

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)



    def get_absolute_url(self):
        return reverse('shop:book_list_by_category',
                       args=[self.slug])

    def __str__(self):
        return f'{self.name}'





