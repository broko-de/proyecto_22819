from django.contrib import admin

from cac.models import EstudianteM, Proyecto

# Register your models here.
admin.site.register(Proyecto)

class EstudianteMAdmin(admin.ModelAdmin):
    list_display = ('dni_m','nombre_m','apellido_m')
    list_editable = ('nombre_m',)
    search_fields = ['apellido_m']

admin.site.register(EstudianteM,EstudianteMAdmin)

