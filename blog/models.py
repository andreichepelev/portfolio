from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'images/')
    body = models.TextField()
    pub_date = models.DateTimeField()

    def __str___(self):
        return self.title

    def summary(self):
        return self.body[:200]+"..."
