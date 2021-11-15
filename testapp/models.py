
from django.contrib.gis.db import models

class Shapes(models.Model):
    name = models.CharField('name',max_length=30)
    subname = models.CharField('subname', max_length=30)
    classmane=models.PositiveSmallIntegerField('classname')
    geom=models.PolygonField(srid=4326)
