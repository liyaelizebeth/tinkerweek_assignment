from django.db import models

# Create your models here

class Events(models.Model):
    event_name = models.CharField(max_length=200)
    event_venue = models.CharField(max_length=200)
    event_type = models.CharField(max_length=200)
    event_sic = models.CharField(max_length=200)

    def __str__(self):
        return self.event_name+'-'+self.event_venue




class individual_Registrations(models.Model):
    event = models.ForeignKey(Events,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,blank=False)
    year = models.CharField(max_length=20)
    team_name = models.CharField(max_length=200)

    def __str__(self):
        return self.event.event_name+'-'+self.name
        
    



class group_Registrations(models.Model):
    event = models.ForeignKey(Events,on_delete=models.CASCADE) 
    team_name = models.CharField(max_length=200) 
    team_mem1 = models.CharField(max_length=200) 
    team_mem2 = models.CharField(max_length=200) 
    team_mem3 = models.CharField(max_length=200) 
    team_mem4 = models.CharField(max_length=200) 

    def __str__(self):
        return self.event.event_name+'-'+self.team_name
    

    