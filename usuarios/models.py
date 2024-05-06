# models.py en tu aplicación de menús

from django.db import models


class UserItem(models.Model):
    # @edad INT = 12;
    # nombre VARCHAR(12)
    
    id_user = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.name

