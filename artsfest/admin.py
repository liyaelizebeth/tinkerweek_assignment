from django.contrib import admin
from .models import Events
from .models import individual_Registrations
from .models import group_Registrations

# Register your models here.
admin.site.register(Events)
admin.site.register(individual_Registrations)
admin.site.register(group_Registrations)