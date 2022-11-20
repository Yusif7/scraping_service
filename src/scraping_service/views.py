import datetime
from django.shortcuts import render


def home(request):
    # Create variable, this information maybe be return from database ? but we create manualy for testing
    date = datetime.datetime.now().date()
    name = 'Yusif'
    # for useing our variables in our project we add them to dictionary
    _context ={
        'date':date,
        'name':name
    }
    # Function returns home.html
    # add our dictionary to function render like third parameter
    return render(request, 'home.html', _context)