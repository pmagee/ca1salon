from django.contrib import admin
from .models import HairSalon, HairDresser, Client

# Register your models here.
admin.site.register(HairSalon)
admin.site.register(HairDresser)
admin.site.register(Client)
