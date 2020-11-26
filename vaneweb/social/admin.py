from django.contrib import admin
from .models import Link
# Register your models here.

class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')

    def get_readonly_fields (self, request, obj = None):
        if request.user.groups.filter(name="Personal").exists():
            return ('created', 'update', 'key', 'name')
        else:
            return ('created', 'update') 
#Aquí estamos dejando en solo lectura algunos campos en tiempo de ejecución para evitar que los usuarios
# cometan errores.   

admin.site.register(Link, LinkAdmin)