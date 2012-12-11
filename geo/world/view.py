# -*- coding: utf-8 -*-
from django.http import HttpResponse
from world.models import *
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.geos import *
from django.contrib.gis.measure import D
#from django.contrib.gis.geos.point import Point 
from django.shortcuts import render_to_response
from django.contrib.gis.geos import Polygon
from django.core.context_processors import csrf
from django.db import connection, transaction

from Crypto.Cipher import AES
from Crypto import Random
import os , random


def sqlQuery():
    return connection.cursor()

def index(request):
    return HttpResponse('Hello')

def postgps(peticion,idUsr,longitud,latitud):
    c={}
    c.update(csrf(peticion))
    
    usr = AuthUser.objects.get(pk=idUsr)
    
    modelo = Track(usr=AuthUser(idUsr), lon= str(longitud), lat=str(latitud))
    modelo.save()
    return HttpResponse ("ok")
    
def report (peticion):
	cod="new google.maps.LatLng("
	modelo = Track.objects.all()
	modelo = modelo.filter(usr=4)
	centro = (-43.29632,-65.08785)
	valor = modelo
	return render_to_response('report.html',{'centro':centro,'valor':valor},)

def reporte (peticion):
	cod="new google.maps.LatLng"
	centro = (-43.307958,-65.055286)
	valor = (cod+"(-43.300212,-65.08257)",cod+"(-43.301485,-65.082248)",cod+"(-43.301555,-65.08272)",cod+"(-43.301751,-65.082602)",cod+"(-43.301384,-65.080059)",cod+"(-43.301727,-65.076937)",cod+"(-43.301727,-65.076937)",cod+"(-43.306537,-65.059267)",cod+"(-43.307958,-65.055286)",cod+"(-43.308777,-65.054224)",cod+"(-43.309027,-65.052604)",cod+"(-43.309199,-65.050222)",cod+"(-43.311268,-65.043281)",cod+"(-43.311479,-65.04298)",cod+"(-43.311322,-65.042637)",cod+"(-43.31151,-65.041178)")
	return render_to_response('reporte.html',{'centro':centro,'valor':valor},)

def testArea (peticion):
	modelo = Areas.objects.get(pk=2)	
	prep_poly = modelo.area.prepared	
	rta1 = prep_poly.contains(Point(-65.046469,-43.316188))
        rta = "noIf"
	if rta1:
		rta = "Correcto"
	else:
		rta = "Fuera de Area"
	return render_to_response('area.html',{'area':modelo,'resp':rta},)

def distancia (listD):
        TAM = len(listD)
        i = 0
        resultado = 0
        
	while i <= TAM-1:
		if i+1 != TAM:
                	p1 = listD[i]
                	p2 = listD[i+1]
	                #p1 = p1.transform(900913)
        	        #p2 = p2.transform(900913)
                	#resultado = resultado + D(m=p1.distance(p2)).mi
	                #resultado = resultado + p1.distance(p2)
        	        l = LineString(p1,p2)
                	resultado = resultado + l.length
                i = i+1
        return resultado


def testDist (peticion):
	cod="new google.maps.LatLng("
        #cursor = sqlQuery()
        modelo = Track.objects.all()
	modelo = modelo.filter(usr=1)
        centro = (-43.297073,-65.090564)
	listD = list()
	for mod in modelo:
		#pnt = GEOSGeometry('Point('+mod.lat+' '+ mod.lon+')')
		pnt = (float(mod.lat),float(mod.lon))
		listD.append(pnt)
	resultado = distancia(listD)

	return render_to_response('distancia.html',{'recorrido':modelo,'resultado':resultado},)

def valUsr (peticion, hashUsr):
        key = '0123456789abcdef'
        iv = Random.new().read(16)
        mode = AES.MODE_CBC
        crypto = AES.new(key, mode, iv)
	desencriptado = crypto.decrypt(hashUsr)
	return render_to_response('prueba.html',{'hash':hashUsr,'desencriptado':desencriptado},)


def informe (peticion, idUsr):
    usuario = AuthUser.objects.get(pk=idUsr)
    modelo = Track.objects.filter(usr = idUsr)
    poly = GEOSGeometry('MULTIPOLYGON((( 1 1, 1 2, 2 2, 1 1)))')
    punt = GEOSGeometry('POINT(-65.09465 -43.296332)')

    a=(-65.08257,-43.300212)
    b=(-65.082248,-43.301485)
    c=(-65.08272,-43.301555)
    d=(-65.082602,-43.301751)
    e=(-65.080059,-43.301384)
    f=(-65.076937,-43.301727)
    g=(-65.076937,-43.301727)
    h=(-65.059267,-43.306537)
    i=(-65.055286,-43.307958)
    j=(-65.054224,-43.308777)
    k=(-65.052604,-43.309027)
    l=(-65.050222,-43.309199)
    m=(-65.043281,-43.311268)
    n=(-65.04298,-43.311479)
    o=(-65.042637,-43.311322)
    p=(-65.041178,-43.31151)

    l1 = LineString(a,b)
    l2 = LineString(b,c)
    l3 = LineString(c, d)
    l4 = LineString(d, e)
    l5 = LineString(e, f)
    l6 = LineString(f, g)
    l7 = LineString(g, h)
    l8 = LineString(h, i)
    l9 = LineString(i, j)
    l10 = LineString(j, k)
    l11 = LineString(k, l)
    l12 = LineString(l, m)
    l13 = LineString(m, n)
    l14 = LineString(n, o)
    l15 = LineString(o, p)
    lin=MultiLineString(l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15)
    #geome = Geometria(punto=punt)
    geome = Geometria(geometrica=poly, punto=punt,linea=lin)    
    geome.save()
    return render_to_response('informe.html',{'track':modelo},)
