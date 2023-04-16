from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Phone(models.Model):
    image = models.ImageField()
    video = models.FileField()
    title = models.CharField(max_length=100)
    cost = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    model_phone = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title