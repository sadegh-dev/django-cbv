from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=200, unique=True)
    pages = models.PositiveIntegerField()
    date_publish = models.DateTimeField()

    def __str__(self):
        return self.name