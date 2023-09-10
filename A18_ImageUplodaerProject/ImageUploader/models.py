from django.db import models

class ImageTable(models.Model):
    image = models.ImageField(upload_to='myimage')
    desc = models.CharField(max_length=40)
    date = models.DateTimeField(auto_now_add=True)