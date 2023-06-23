from django.contrib import admin
from .models import Articel

# class AricelAdmin(admin.ModelAdmin):
#     list_dispaly = ["name", "auther"]
   

admin.site.register(Articel)


