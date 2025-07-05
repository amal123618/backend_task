from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return f"{self.name} - {self.mobile_number}"
