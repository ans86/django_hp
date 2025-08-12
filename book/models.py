from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="books/")
    author = models.CharField()
    publishyear = models.IntegerField()

    def __str__(self):
        return self.title