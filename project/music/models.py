from django.db import models

# Create your models here.

class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

def image_upload_path(instance,filename):
    return f'{instance.pk}/{filename}'


class Singer(models.Model):
    id = models.AutoField(primary_key=True)
    name =models.CharField(max_length=50)
    content = models.TextField(max_length=300)
    debut = models.DateField()
    tag = models.ManyToManyField(Tag, blank=True)

class Image(models.Model):
    id = models.AutoField(primary_key=True)
    singer = models.ForeignKey(Singer, blank=False,null=False,on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to=image_upload_path,blank=True,null=True)


class Song(models.Model):
    id = models.AutoField(primary_key=True)
    name =models.CharField(max_length=50)
    singer = models.ForeignKey(Singer, blank=False,null=False,on_delete=models.CASCADE,related_name='songs')
    release = models.DateField()
    content = models.TextField(max_length=300)
