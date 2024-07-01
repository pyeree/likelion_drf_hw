from django.db import models

# Create your models here.

class Singer(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField(max_length=300)
    debut = models.DateField()


class Song(models.Model):
    id = models.AutoField(primary_key=True)
    singer = models.ForeignKey(Singer,on_delete=models.CASCADE,related_name = 'songs')
    release = models.DateField()
    content = models.TextField(max_length=300)
