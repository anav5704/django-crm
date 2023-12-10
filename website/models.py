from django.db import models

class Customer(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    phone = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    country = models.CharField(max_length=25)

    def __str__(self):
        return(f"{self.firstName} {self.lastName}")