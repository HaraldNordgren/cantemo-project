from django.db import models

# Create your models here.

class BankImage(models.Model):
    path = models.CharField(max_length=200)
    metadata = models.CharField(max_length=200)

    def __str__(self):
        return "%s (%s)" % (self.path, self.metadata)
