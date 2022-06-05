from django.db import models


class Link(models.Model):
    url = models.URLField(max_length=2000)
    alias = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f'{self.alias} -> {self.url}'