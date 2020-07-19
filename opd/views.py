from django.shortcuts import render,redirect
import requests
from bs4 import BeautifulSoup
import lxml.html
from .forms import Country_Form
from .models import Country
from django.contrib import messages
from django.contrib.auth.decorators import login_required
country_url = 'https://api.covid19api.com/total/country/{}'

#worldwide corona status
html= requests.get('https://www.worldometers.info/coronavirus/')
india_base_url = requests.get('https://www.mohfw.gov.in/')
doc = lxml.html.fromstring(html.content)
#india corona status
ind = lxml.html.fromstring(india_base_url.content)
base_url= requests.get('https://www.mohfw.gov.in/')
mock = lxml.html.fromstring(base_url.content)
#state wise data collected
page = requests.get('https://www.mohfw.gov.in/')
soup = BeautifulSoup(page.content,'html.parser')
mt = soup.find(class_="data-table")

# Create your views here.
def index(request):
    return render(request,'opd/base.html')

def corona(request):
    mt = doc.xpath('//div[@id="maincounter-wrap"]')
    cases, deaths , recovered  = [i.xpath('.//div[@class="maincounter-number"]/span/text()')[0] for i in mt]
    mt1, recover, death, migr= mock.xpath('//div[@class="site-stats-count"]/ul/li/strong/text()')
    active_cases = int(mt1) + int(recover)+ int(death)+ int(migr)
    context={
    'mt1' : mt1,
    'active_cases' : active_cases,
    'recover' :recover,
    'death' :death,
    'cases' : cases,
    'deaths' : deaths,
    'recovered' : recovered,
    }
    return render(request,'opd/corona.html',context)


def statewise_status(request):
    # statewise corona
    mt1, recover, death, migr= mock.xpath('//div[@class="site-stats-count"]/ul/li/strong/text()')
    active_cases = int(mt1) + int(recover)+ int(death)+ int(migr)
    mi = []
    for i in range(1,34):
        li = []
        for m in range(0,5):
            li.append(mt.find_all('tr')[i].find_all('td')[m].get_text())
        mi.append(li)
    context={
    'mi':mi,
    'mt1' : mt1,
    'active_cases' : active_cases,
    'recover' :recover,
    'death' :death,
    }
    return render(request,'opd/statewise.html',context)
@login_required
def country_search(request):
    form = Country_Form()
    country_data=request.POST.get('search')
    country_url = f'https://api.covid19api.com/total/country/{country_data}'
    response = requests.get(country_url)
    if response.status_code == 404:
        if country_data == "":
            messages.warning(request, 'Pease enter the valid country')
        context={
         }
    else:
        r = response.json()[-1]
        Confirmed = r['Confirmed']
        Deaths =  r['Deaths']
        Recovered = r['Recovered']
        Active = r['Active']
        context = {

            'Confirmed': Confirmed,
            'Deaths': Deaths,
            'Recovered': Recovered,
            'Active': Active,
        }
    return render(request,'opd/country_search.html',context)



def transmission(request):
    return render(request,'opd/transmit_mode.html')


def precaution(request):
    return render(request,'opd/precaution.html')


@login_required
def map(request):
    return render(request,'opd/map.html')


def alert_zone(request):
    return render(request,'opd/alert_zone.html')