from django.contrib import admin
from productos.models import  Producto
from productos.models import  Categoria

class ProductoInline(admin.TabularInline):
    
    model = Producto
    extra = 0

class CategoriaAdmin(admin.ModelAdmin):
    inlines= [ProductoInline]

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    #fields =['categoria','fecha_publicacion', 'producto', 'imagen']

    fieldsets = [
        ("Relacion",{"fields":["categoria"]}),
        (
            "Datos generales",
            {
                "fields":[
                    'fecha_publicacion', 'producto', 'estado', 'imagen'
                ]
            },
        ),
    ]
    list_display = ['producto', 'fecha_publicacion', 'tipo_de_producto', 'imagen','upper_case_name']
    ordering = ["-fecha_publicacion"]
    list_filter = ('producto', 'fecha_publicacion')
    search_fields = ('producto', 'estado',)
    list_display_links = ('producto', 'fecha_publicacion')

    @admin.display(description="Name")
    def upper_case_name(self, obj):
        return("%s %s" % (obj.producto, obj.estado)).upper()
#admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)

# Register your models here.
#admin.site.register(Producto)
#admin.site.register(Categoria)