from django.db import models

class Blogupdate(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:10]
