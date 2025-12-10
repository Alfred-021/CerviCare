from django.contrib import admin
from .models import Hospital

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'phone', 'created_at')
    search_fields = ('name', 'city')
    list_filter = ('city', 'created_at')
