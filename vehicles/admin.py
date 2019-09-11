from django.contrib import admin

# Register your models here.
from .models import Vehicle


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):

    list_display = ['id', 'plates', 'type', 'model']
    # list_display = ['id', 'plates', 'type', 'model', 'account']

    # define search box
    search_fields = ['plates', 'brand']

    # define filter columns
    list_filter = ['brand']

    # define which field will be pre populated.
    #prepopulated_fields = {'dept_name': ('dept_name',)}
    # define model data list ordering.
    ordering = ('id','plates')
