import requests
from django.shortcuts import render
from urllib.request import urlopen
import json


def home(request):
    data = []
    url = "https://covid-193.p.rapidapi.com/statistics"

    querystring = {"country":"Bangladesh"}

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "be7f37114bmsh38c0486c35a5050p1bc1e5jsnf574155ad041"
        }

    response = requests.request("GET", url, headers=headers, params=querystring).json()
    
    d = response['response']
    s = d[0]

    context = {
        'date': s['day'],
        'all': s['cases']['total'],
        'recovered': s['cases']['recovered'],
        'active': s['cases']['active'],
        'newdeaths': s['deaths']['new'],
        'deaths': s['deaths']['total'],
        'new': s['cases']['new'],
        'critical': s['cases']['critical'],
    }
    
   

    return render(request, 'index.html', context)
