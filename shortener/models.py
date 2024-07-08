from django.db import models

class URL(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=20)

    def __str__(self):
        return self.original_url
