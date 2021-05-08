from django.db import models

class Finalblog2(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image=models.ImageField(upload_to="blog2/", blank=True, null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:5]

