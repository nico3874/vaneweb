from django.contrib import admin
from .models import OfferCarruselChildren, OfferCarruselChildren2, OfferCarruselChildren3, OfferCarruselChildren4, OfferCarruselChildren5, OfferCarruselChildren6
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


class CategoryAdmin2(admin.ModelAdmin):
    readonly_fields = ('created',)

class CategoryAdmin3(admin.ModelAdmin):
    readonly_fields = ('created',)

class CategoryAdmin4(admin.ModelAdmin):
    readonly_fields = ('created',)

class CategoryAdmin5(admin.ModelAdmin):
    readonly_fields = ('created',)

class CategoryAdmin6(admin.ModelAdmin):
    readonly_fields = ('created',)




admin.site.register(OfferCarruselChildren, CategoryAdmin)
admin.site.register(OfferCarruselChildren2, CategoryAdmin2)
admin.site.register(OfferCarruselChildren3, CategoryAdmin3)
admin.site.register(OfferCarruselChildren4, CategoryAdmin4)
admin.site.register(OfferCarruselChildren5, CategoryAdmin5)
admin.site.register(OfferCarruselChildren6, CategoryAdmin6)