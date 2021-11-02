from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=220)
    author = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.title
