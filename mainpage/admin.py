from django.contrib import admin

from .models import Newsletter, Country, Departament, City, Register

@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('institution', 'representant', 'get_full_city')

    def representant(self, obj):
        return "{} {}".format(obj.name, obj.lastname)
    
    def get_full_city(self, obj):
        return "{}, {}, {}".format(obj.city, obj.city.departament, obj.city.departament.country)

    get_full_city.short_description = 'city'

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'departament_count')
    search_fields = ['name']

    def departament_count(self, obj):
        return obj.departament_set.count()
    
    departament_count.short_description = 'Total departamentos'

@admin.register(Departament)
class DepartamentAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'cities_count')
    search_fields = ['name']

    fieldsets = (
        (None, {'fields': (('country', 'name'),)}),
    )

    def cities_count(self, obj):
        return obj.city_set.count()

    cities_count.short_description = "Total ciudades"

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'departament', 'get_country')
    search_fields = ['name']

    def get_country(self, obj):
        return obj.departament.country
    
    get_country.short_description = 'Pais'


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ( 'email', 'active')

    fieldsets = (
        (None, {'fields': (('email', 'active'),)}),
    )

