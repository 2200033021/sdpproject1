from django.db import models

# Create your models here.
from django.db import models
class Register(models.Model):
    name = models.CharField(max_length=100)
    email=models.EmailField(primary_key=True)
    password = models.CharField(max_length=100)
    phonenumber = models.IntegerField()
    class Meta:
        db_table="Register"

from django.db import models
class Contactus(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email=models.EmailField(primary_key=True)
    comment = models.TextField(max_length=255)

    class Meta:
        db_table="Contactus"

class TouristReview(models.Model):
    user = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.IntegerField()
    image = models.ImageField(upload_to='static/media/review_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f'Review - {self.created_at}'
