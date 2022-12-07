import codecs
import os, sys

# We create absolute path for using anywhere 
proj = os.path.dirname(os.path.abspath('manage.py'))
# adding our absolute path to sys module
sys.path.append(proj)
# We use scraping_service because our settings file here
os.environ['DJANGO_SETTINGS_MODULE'] = 'scraping_service.settings'

import django
django.setup()


from scraping.parsers import *
from scraping.models import Vacancy, City, Language

# function and website url 
parsers = (
    (work, 'https://www.work.ua/ru/jobs-kyiv-python/'),
    (dou, 'https://jobs.dou.ua/vacancies/?category=Python')
)


city = City.objects.filter(slug = 'kiev')
# vacancy and error list
jobs, errors = [], []

# For activate all parser with loop 
for func, url in parsers:
    j, e = func(url)
    jobs += j
    errors += e

h = codecs.open('work.txt','w','utf-8')
h.write(str(jobs))
h.close()