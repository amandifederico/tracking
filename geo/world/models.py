# -*- coding: utf-8 -*-
from django.db import models
from geoposition.fields import GeopositionField
# Create your models here.
from django.contrib.gis.db import models

class WorldBorder(models.Model):
    fips = models.CharField(max_length=2)
    iso2 = models.CharField(max_length=2)
    iso3 = models.CharField(max_length=3)
    un = models.IntegerField()
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField()
    region = models.IntegerField()
    subregion = models.IntegerField()
    lon = models.FloatField()
    lat = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()

    def __unicode__(self):
        return self.name

# Auto-generated `LayerMapping` dictionary for WorldBorder model
worldborders_mapping = {
    'fips' : 'FIPS',
    'iso2' : 'ISO2',
    'iso3' : 'ISO3',
    'un' : 'UN',
    'name' : 'NAME',
    'area' : 'AREA',
    'pop2005' : 'POP2005',
    'region' : 'REGION',
    'subregion' : 'SUBREGION',
    'lon' : 'LON',
    'lat' : 'LAT',
    'geom' : 'MULTIPOLYGON',
}

class PointOfInterest(models.Model):
    name = models.CharField(max_length=100)
    position = GeopositionField()

    def __unicode__(self):
        return self.name

class Waypoint(models.Model):

    name = models.CharField(max_length=32)
    geometry = models.PointField(srid=4326)
    objects = models.GeoManager()

    def __unicode__(self):
        return '%s %s %s' % (self.name, self.geometry.x, self.geometry.y)
#-----------------------------------------------------------------------------------------
class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    password = models.CharField(max_length=128)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    is_superuser = models.BooleanField()
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = u'auth_user'
    def __unicode__(self):
        return self.username


class Track(models.Model):
    id_track = models.AutoField(primary_key=True)
    usr = models.ForeignKey(AuthUser, db_column='usr')
#    lon = models.FloatField()
    lon = models.CharField(max_length=128)
#    lat = models.FloatField()
    lat = models.CharField(max_length=128)
    fecha = models.DateField(auto_now=True)
    
    class Meta:
        db_table = u'track'
    
#    def __unicode__(self):
#        return self.usr     

class Areas(models.Model):
    id_track = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=128)
    area = models.MultiPolygonField()
    objects = models.GeoManager()
    class Meta:
        db_table = 'areas'
    def __unicode__(self):
        return self.descripcion


class Geometria(models.Model):
    id_geo = models.AutoField(primary_key=True)
    geometrica = models.MultiPolygonField()
    punto = models.PointField()
    linea = models.MultiLineStringField(blank = True)
    objects = models.GeoManager()
    class Meta:
        db_table = 'geometria'

