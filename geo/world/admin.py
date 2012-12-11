from django.contrib.gis import admin
from models import *


class TrackAdmin(admin.ModelAdmin):
	list_display = ('usr','lon','lat','fecha',)
	ordering = ('usr','fecha',)
	search_fields = ('usr__username',)	


#admin.site.register(WorldBorder, admin.GeoModelAdmin)
admin.site.register(WorldBorder, admin.OSMGeoAdmin)
admin.site.register(Areas, admin.OSMGeoAdmin)
admin.site.register(PointOfInterest)
admin.site.register(Waypoint)
admin.site.register(Track,TrackAdmin)
admin.site.register(Geometria, admin.OSMGeoAdmin)
