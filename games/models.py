from django.db import models
from django.contrib.auth.models import User
import math

class Game(models.Model):
        onsale = models.IntegerField(default=0)
        steamworks = models.IntegerField(default=0)
        game_title = models.CharField(max_length=50)
        game_link = models.CharField(max_length=100)
        rrp = models.FloatField()
        drp = models.FloatField()
        pic = models.ImageField(upload_to = '/static/bootstrap/images/', default = 'no-img.jpg')
        

        def discount(self):
                return int(round(((self.rrp - self.drp)/self.rrp*100)))
                
class Wishlist(models.Model):
        user = models.ForeignKey(User)
        game = models.ForeignKey(Game)
