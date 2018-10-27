from django.db import models


# Create your models here.

class Information:
    def __init__(self):
        self.version = "2.1"
        self.topics = ["Templates", "Forms", "ORM", 'REST', "Sessions and Cookies"]


class Book(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    pubid = models.IntegerField()

    def __str__(self):
        return self.title