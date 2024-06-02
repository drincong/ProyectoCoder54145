from django.contrib import admin
from .models import Curso
from .models import Profesor
from .models import Estudiante
from .models import Entregable


class CurstoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'camada']
    search_fields =['nombre', 'camada']
    list_filter=['nombre']

# Register your models here.
admin.site.register(Curso, CurstoAdmin)
admin.site.register(Profesor)
admin.site.register(Estudiante)
admin.site.register(Entregable)

