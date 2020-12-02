from django.contrib import admin
from .models import TipoInsumo, RegistroInsumos

# Register your models here.

class RegistroAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'descripcion', 'stock', 'tipo']
    search_fields = ['nombre']
    list_per_page = 5

admin.site.register(TipoInsumo)
admin.site.register(RegistroInsumos, RegistroAdmin)