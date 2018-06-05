from django.shortcuts import render
import requests


def home(request):
    response = requests.get('http://freegeoip.net/json/')
    geodata = response.json()
    # ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
    # response = requests.get('http://freegeoip.net/json/%s' % ip_address)
    # geodata = response.json()
    print geodata
    context = {
        'city' : geodata['city'],
        'ip' : geodata['ip'],
        'country' : geodata['country_name'],
        'latitude' : geodata['latitude'],
        'longitude': geodata['longitude'],
        'api_key': 'AIzaSyC1UpCQp9zHokhNOBK07AvZTiO09icwD8I'
        

    }
    return render(request,'geo/home.html',context)


