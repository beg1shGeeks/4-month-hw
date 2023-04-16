from django.db import models

# Create your models here.


class Book(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
