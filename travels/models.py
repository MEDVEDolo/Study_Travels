from django.db import models
from Core.models import User

# Create your models here.

class Travel(models.Model):
    title = models.CharField(max_length=355)
    description = models.TextField()
    price = models.PositiveIntegerField()
    photo = models.ImageField(
        upload_to="travels/images/travel/photos/", null=True)
    popular_place = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        null=True, related_name='travels', blank=True)