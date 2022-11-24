from django.shortcuts import render

from scraping.models import Vacancy

def home_view(request):
    # for show post request in cmd we use this command
    print(request.GET) # ONLY IN CMD 
    # ADD TO THE VARIABLE GET REQUEST IN FORMS
    city = request.GET.get('city')
    language = request.GET.get('language')

    #Create empty list
    qs=[]
    # Our sorting work if language or city is not empty
    if city or language:
        # Create an empty dictioanary
        _filter = {}
        # If user add city name add to the filter 
        # we use 2 under line(__) between to call the field name -- city__name => model.name__fieldName
        if city:
            _filter['city__name'] = city
        # If user add city name add to the filter 
        if language:
            _filter['language__name'] = language
    #call our vacancy list
    # ** ==> Returns a new QuerySet containing objects that match the given lookup parameters.
        qs = Vacancy.objects.filter(**_filter)
    # We transmit our vacancy to render like an deictionary
    return render(request, 'scraping/home.html', {'object_list': qs})
