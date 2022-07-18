from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    phone_number = models.IntegerField(unique=True)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        contact = {"name": self.name, "number": self.phone_number}
        return contact