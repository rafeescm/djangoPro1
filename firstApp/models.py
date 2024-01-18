from django.db import models


# Create your models here.
class Director(models.Model):
    director = models.CharField(max_length=200)
    def __str__(self):
        return self.director
class Actor(models.Model):
    actor=models.CharField(max_length=50)
    def __str__(self):
        return self.actor
class CensorInfo(models.Model):
    rating = models.CharField(max_length=10)
    certified_by = models.CharField(max_length=200,null=True)

class MovieInfo(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField(null=True)
    summary = models.TextField()
    censor_details = models.OneToOneField(CensorInfo,on_delete=models.SET_NULL,related_name='movie',null=True)
    directed_by  = models.ForeignKey(Director,null=True,on_delete=models.CASCADE,related_name='directed_movies')
    acted_by = models.ManyToManyField(Actor,related_name="acted_movies")
    image = models.ImageField(upload_to='uploads/', null=True,blank=True)

    def __str__(self):
        return self.title
