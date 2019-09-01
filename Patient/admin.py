from django.contrib import admin
from .models import Chest_Pain
# Register your models here.



class ChestPainAdmin(admin.ModelAdmin):
    list_display = ('id','age')

admin.site.register(Chest_Pain,ChestPainAdmin)