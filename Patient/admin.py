from django.contrib import admin
from .models import Chest_Pain, Patient, Physician
# Register your models here.



class ChestPainAdmin(admin.ModelAdmin):
    list_display = ('id','patient','age')

admin.site.register(Chest_Pain,ChestPainAdmin)


class PatientAdmin(admin.ModelAdmin):
    list_display = ('u','dob','joined')
admin.site.register(Patient, PatientAdmin)


class PhysicianAdmin(admin.ModelAdmin):
    list_display = ('u','dob','joined')
admin.site.register(Physician, PhysicianAdmin)

