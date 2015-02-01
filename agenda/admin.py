from django.contrib import admin
from agenda.models import Contact, Localization

class LocalizationInLine(admin.TabularInline):
    model = Localization
    extra = 1
    
class ContactAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Información Personal',  {'fields': ['first_name', 'last_name']}),
        ('Información Laboral', {'fields': ['company_name'], 'classes':['collapse']}),
    ]
    
    inlines = [LocalizationInLine]
    search_fields = ['first_name', 'last_name']
    
# Register your models here.
# Register your models here.
admin.site.register(Contact, ContactAdmin)
