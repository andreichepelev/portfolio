from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'images/')
    body = models.TextField()
    pub_date = models.DateTimeField()
