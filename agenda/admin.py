from django.contrib import admin
from agenda.models import Contact, Localization, Agenda
'''
class LocalizationInLine(admin.TabularInline):
    model = Localization
    extra = 1
    
class ContactInLine(admin.TabularInline):
    model = Localization
    extra = 1
    
    fieldsets = [
        ('Información Personal',  {'fields': ['first_name', 'last_name']}),
        ('Información Laboral', {'fields': ['company_name'], 'classes':['collapse']}),
    ]
    
    inlines = [LocalizationInLine]
    search_fields = ['first_name', 'last_name']
    
class AgendaAdmin(admin.ModelAdmin):
    search_fields = ['name']
'''
# Register your models here.
#admin.site.register(Contact, ContactAdmin)
#admin.site.register(Agenda, AgendaAdmin)
admin.site.register(Agenda)
admin.site.register(Contact)
admin.site.register(Localization)


