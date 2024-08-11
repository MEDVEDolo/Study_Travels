from django.contrib import admin
from .models import Travel

# Register your models here.

@admin.register(Travel)
class TravelAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')