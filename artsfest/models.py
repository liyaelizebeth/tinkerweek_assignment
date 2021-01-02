from django.db import models

# Create your models here

class Events(models.Model):
    event_name = models.CharField(max_length=200,)

    event_venue = models.CharField(max_length=200)

    def __str__(self):
        return self.event_name+'-'+self.event_venue


class Participants(models.Model):
    event = models.ForeignKey(Events,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,blank=False)
    gender = models.CharField(max_length=50,blank=False)
    year = models.IntegerField(max_length=20)
    team_name = models.CharField(max_length=200)
    