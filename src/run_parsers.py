import codecs
import os, sys
from django.contrib.auth import get_user_model
# For using DB if we we have aany errors while scraping is working
from django.db import DatabaseError

# We create absolute path for using anywhere 
proj = os.path.dirname(os.path.abspath('manage.py'))
# adding our absolute path to sys module
sys.path.append(proj)
# We use scraping_service because our settings file here
os.environ['DJANGO_SETTINGS_MODULE'] = 'scraping_service.settings'

import django
django.setup()


from scraping.parsers import *
from scraping.models import Url, Vacancy, City, Language, Error

# Import our user which we add in settings.py - auth
User = get_user_model()

# function and website url 
parsers = (
    (work, 'https://www.work.ua/ru/jobs-kyiv-python/'),
    (dou, 'https://jobs.dou.ua/vacancies/?category=Python')
)

# .first()  return first object in query set
# city = City.objects.filter(slug = 'kiev').first()
# language = Language.objects.filter(slug = 'python').first()
# vacancy and error list
jobs, errors = [], []

# Functions to define id of serach filters
def get_settings():
    # .values() convert instance of object to id that mean we get only id in db not name like python
    qs = User.objects.filter(send_email=True).values()
    # Ad to tuple city and language id 
    settings_lst = set((q['city_id'], q['language_id']) for q in qs)
    return settings_lst

def get_urls(_settings):
    qs = Url.objects.all().values()
    url_dict = {(q['city_id'], q['language_id']): q['url_data'] for q in qs}
    urls = []
    for pair in _settings:
        tmp = {}
        tmp['city'] = pair[0]
        tmp['language'] = pair[1]
        tmp['url_data'] = url_dict.get(pair)
        urls.append(tmp)
    return urls

settings = get_settings()
url_list = get_urls(settings)
for data in url_list:
    # For activate all parser with loop 
    for func, key in parsers:
        url = data['url_data'][key]
        j, e = func(url, city=data['city'], language=data['language'])
        jobs += j
        errors += e

for job in jobs:
    # Vacancy accept all element from jobs and he must be have city and language because we give them that status
    v = Vacancy(**job)
    # our url is unique and if it does not changed we can have error so when we try catch we can solve this problem
    try:
        v.save()
    except DatabaseError:
        pass
# If we find error in our sites we add it to our db 
if errors:
    er = Error(data=errors).save()

h = codecs.open('work.txt','w','utf-8')
h.write(str(jobs))
h.close()