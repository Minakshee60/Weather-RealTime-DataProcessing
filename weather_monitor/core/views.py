from django.http import HttpResponse
from django.shortcuts import render
import requests

def fetch_data(request):
    cities = ['Mumbai','Kolkata','Delhi','Bangalore','Chennai','Hyderbad']
    weather_data=[]
    for city in cities:
        # url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=735e7621bdf34b489c6106047f56431d"
        url="something"
        res = requests.get(url)
        data = res.json()
        if(res.status_code == 200):
            weather_data.append({
                'city': city,
                'temperature': data['main']['temp'],  
                'main': data['weather'][0]['main'],
                'feels_like': data['main']['feels_like'],
                'date' : data['dt']
            })
        else:
            print("will see the problem")

    # print(weather_data)
    return render(request,'data.html',{'weather_data':weather_data})    

