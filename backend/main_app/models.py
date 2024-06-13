from django.db import models

# Create your models here.
class UserProfile(models.Model):
    username = models.CharField(max_length=30)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def _str_(self):
        return self.title