from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.

class Information:
    def __init__(self):
        self.version = "2.1"
        self.topics = ["Templates", "Forms", "ORM", 'REST', "Sessions and Cookies"]


class Book(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField(validators=[MinValueValidator(100)])
    pubid = models.IntegerField()

    def __str__(self):
        return self.title