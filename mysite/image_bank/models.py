from django.db import models

# Create your models here.

class BankImage(models.Model):
    path = models.CharField(max_length=200)
    file_type = models.CharField(max_length=100)
    converted_path = models.CharField(max_length=200, default="")
    metadata = models.CharField(max_length=200, default="")

    def __str__(self):
        return "%s (%s) (%s)" % (self.path, self.file_type, self.metadata)
