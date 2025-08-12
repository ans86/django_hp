from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to="authors/")
    fathername = models.CharField(max_length=255)
    publishedbooks = models.IntegerField()

    def __str__(self):
        return self.name
    



class Books(models.Model):

    title = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to="bookss/")
    publishyear = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title