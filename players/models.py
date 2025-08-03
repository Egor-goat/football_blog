from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    founded = models.DateField()
    logo = models.ImageField(upload_to='team_logos/', blank=True, null=True)

    def __str__(self):
        return self.name
    
class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    position = models.CharField(max_length=50)
    team = models.ForeignKey(Team,on_delete=models.CASCADE,related_name='players')
    photo = models.ImageField(upload_to='player_photos/', blank=True, null=True)
    goals = models.PositiveIntegerField(default=0)
    assists = models.PositiveIntegerField(default=0)
    clean_sheats = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f"{self.name} ({self.position})"