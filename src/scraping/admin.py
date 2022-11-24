from django.contrib import admin
from .models import City,Language,Vacancy

# Registred our db in admin
admin.site.register(City)
admin.site.register(Language)
admin.site.register(Vacancy)
