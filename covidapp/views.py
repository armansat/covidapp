from django.shortcuts import render
import requests
import json
import random 

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
	"X-RapidAPI-Key": "86c0354dd3msh349881783983608p1180bajsn65fce824e300",
	"X-RapidAPI-Host": "covid-193.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers).json()


# Create your views here.
def covidworldview(request):
    context = {'response': response['response'][random.randrange(0, len(response['response']) - 1)]}
    return render(request,'covidworld.html',context)