from django.db import models


# Create your models here.
class ProgContent(models.Model):
    headline = models.CharField(max_length=300)
    img = models.URLField(null=True, blank=True)
    url = models.TextField()

    def __str__(self):
        return self.headline


8