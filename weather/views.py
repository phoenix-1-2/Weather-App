from django.shortcuts import render,redirect
import urllib.request 
import json
# Create your views here.
def index(request):
    given_order=False
    place="India"
    ACCESS_KEY='9631ab03f3d90cdedf46a8e9ccad48e4'
    if request.method == 'POST':
        given_order=True
        place= request.POST['place']
        place1=place
        place=place.replace(' ','%20')
        ACCESS_KEY='9631ab03f3d90cdedf46a8e9ccad48e4'
        with urllib.request.urlopen('http://api.weatherstack.com/current?access_key=' + ACCESS_KEY + '&+query=' + place) as response:
            source_json = response.read()
            data= json.loads(source_json)
            if data.get('success',True) == False:
                return render(request,'weather/index.html',{
                    'given_order':False
                })
            desciption= data['current']['weather_descriptions'][0].lower()
            image=''
            if data['current']['is_day']=='yes':
                image='images/sun.png'
            if data['current']['is_day'] =='no':
                image='images/moon.png'
            if desciption.find('cloud')!=-1:
                image='images/weather.png'
            if  desciption.find('overcast')!=-1:
                image='images/cloudy.png'
            if desciption.find('sun')!=-1:
                image='images/sun.png'
            if desciption.find('wind')!=-1:
                image='images/wind.png'
            if desciption.find('thunder')!=-1:
                image='images/flash.png'
            if desciption.find('rain') !=-1:
                image='images/rain.png'
            if desciption.find('snow')!=-1:
                image='images/snow.png'
            
            context={
                'given_order':True,
                'value' : place1,
                'city_name': data['location']['name'],
                'country':data['location']['country'],
                'image' : '/static/'+image ,
                'localtime':data['location']['localtime'],
                'temp': data['current']['temperature'],
                'wind_speed': data['current']['wind_speed'],
                'humidity': data['current']['humidity'],
                'visibility': data['current']['visibility'],
                'pressure': data['current']['pressure'],
                'precip': data['current']['precip'],
                'feelslike': data['current']['feelslike'],
            }
            return render(request,'weather/index.html',context)
    else:
        with urllib.request.urlopen('http://api.weatherstack.com/current?access_key=' + ACCESS_KEY + '&+query=' + place) as response:
            source_json = response.read()
            data= json.loads(source_json)
            desciption= data['current']['weather_descriptions'][0]
            image=''
            if data['current']['is_day']=='yes':
                image='images/sun.png'
            if data['current']['is_day'] =='no':
                image='images/moon.png'
            if desciption.find('cloud')!=-1:
                image='images/weather.png'
            if desciption.find('sun')!=-1:
                image='images/sun.png'
            if desciption.find('wind')!=-1:
                image='images/wind.png'
            if desciption.find('thunder')!=-1:
                image='images/flash.png'
            if desciption.find('rain') !=-1:
                image='images/rain.png'
            if desciption.find('snow')!=-1:
                image='images/snow.png'
            
            context={
                'given_order':True,
                'value' : place,
                'city_name': data['location']['name'],
                'country':data['location']['country'],
                'image' : '/static/'+image ,
                'localtime':data['location']['localtime'],
                'temp': data['current']['temperature'],
                'wind_speed': data['current']['wind_speed'],
                'humidity': data['current']['humidity'],
                'visibility': data['current']['visibility'],
                'pressure': data['current']['pressure'],
                'precip': data['current']['precip'],
                'feelslike': data['current']['feelslike'],
            }
            return render(request,'weather/index.html',context)

