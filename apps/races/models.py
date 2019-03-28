from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    email = models.EmailField(unique=True, default='somestring')
    password = models.CharField(max_length = 255, default= 'somestring')



class Race(models.Model):
    name = models.CharField(max_length = 255)
    city = models.CharField(max_length = 20)
    state = models.CharField(max_length = 20)
    date = models.DateField()
    workers = models.ManyToManyField(User, related_name='events')