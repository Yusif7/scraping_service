from django.apps import AppConfig

# We add verbose for change name of app and then change it in file init.py
class ScrapingConfig(AppConfig):
    name = 'scraping'
    verbose_name = 'Приложение по сбору вакансии'                    

       