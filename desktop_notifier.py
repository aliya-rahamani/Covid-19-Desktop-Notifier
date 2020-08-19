import requests
from win10toast import ToastNotifier
import datetime
try:
    data = requests.get("http://api.coronatracker.com/v3/stats/worldometer/country?countryCode=IN")
except:
    print("Check your Internet connection")
    data = None

if data is not None:
    getData = data.json()
    covid_India = getData[0]


    title = """Covid-19 India/ {}""".format(datetime.date.today())

    message= """In India covid-19 total cases is: {} , deaths : {}, recovered : {}, today-case is: {}""".format(covid_India["totalConfirmed"],covid_India["totalDeaths"],covid_India["totalRecovered"],covid_India["dailyConfirmed"])

    toaster = ToastNotifier()
    toaster.show_toast(title,message,icon_path="G:\Coding\python programs/corona.ico",duration = 25)