from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=128, null=False)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=256, null=False)
    description = models.TextField(null=True, blank=True)
    category = models.ManyToManyField(Category)
    author = models.CharField(max_length=128, null=True, blank=True)
    pub_date = models.DateTimeField('date published')
    number_of_page = models.IntegerField(default=0)
