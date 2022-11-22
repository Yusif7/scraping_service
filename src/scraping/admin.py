from django.contrib import admin
from .models import city,Language,Vacancy

# Registred our db in admin
admin.site.register(city)
admin.site.register(Language)
admin.site.register(Vacancy)
