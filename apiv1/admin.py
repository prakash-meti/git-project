from django.contrib import admin

from .models import Traveller, TouristPlace, TouristAgency

@admin.register(Traveller)
class TravellerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'birth_date')

@admin.register(TouristPlace)
class TouristPlaceAdmin(admin.ModelAdmin):
    list_display = ('id','place_name', 'location')

@admin.register(TouristAgency)
class TouristAgencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'agency_name', 'package_cost', 'subscribers', 'traveller_display')
    filter_horizontal = ('visited_places',)

    def traveller_display(self, obj):
        return obj.traveller.name if obj.traveller else "N/A"

    traveller_display.short_description = 'Traveller'
