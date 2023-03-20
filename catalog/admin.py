from django.contrib import admin
from .models import Chocolate, Company, Nutrients
# Register your models here.

# admin.site.register(Chocolate)
# admin.site.register(Company)
# admin.site.register(Nutrients)

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name','estb','company_id')

admin.site.register(Company, CompanyAdmin)

@admin.register(Chocolate)
class ChocolateAdmin(admin.ModelAdmin):
    pass

@admin.register(Nutrients)
class NutrientsAdmin(admin.ModelAdmin):
    pass

