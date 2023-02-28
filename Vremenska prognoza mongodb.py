
from pymongo import MongoClient
#import pymongo
from pymongo import errors
from dotenv import load_dotenv
import os
from datetime import datetime
import requests
import pprint
import datetime
import threading
import time

#Importuj Objectid iz BSONa da bi mogao da tražiš ovaj podatak
from bson.objectid import ObjectId


#Program za uzimanje podataka vremenske prognoze za niš

load_dotenv()
MONGODB_URL = os.environ["MONGODB_URL"]

client = MongoClient(MONGODB_URL)
#client = pymongo.MongoClient('mongodb://localhost:27017')
#listanje svih kolekcija u bazi
#for db_name in client.list_database_names():

#    print(db_name)


def vreme_nis():
    url = 'http://api.openweathermap.org/data/2.5/weather?q=niš&appid=cc5342ce347185367d6dd8020643a404&lang=sr'
    res = requests.get(url)
    data = res.json()

    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind = data['wind']['speed']
    description = data['weather'][0]['description']
    temp = data['main']['temp']
    min_temp = data['main']['temp_min']
    max_temp = data['main']['temp_max']
    grupni_izvestaj = data['weather'][0]['main']
    vremenska_zona = data['timezone']

    tempC = temp - 273.15
    maxC = max_temp - 273.15
    minC = min_temp - 273.15
    now = datetime.datetime.now() # current date and time
    time = now.strftime("%H:%M:%S")

    global client
    db = client.vremenska_prognoza
    vreme_1 = db.vreme_srbija
    selektuj = {'grad': "Niš"}
    prognoza_nis =   { "$set": {
            "trenutna_temperatura": int(tempC),
            "min_temp": int(minC),
            "max_temp": int(maxC),
            "wind": int(wind),
            "opis": str(description),
            "pritisak": float(pressure),
            "vremenska_zona": int(vremenska_zona),
            "trenutno_vreme": str(time),
            "last_updated": datetime.datetime.utcnow()
    }}
    try:
        vreme_1.update_many(selektuj, prognoza_nis)
    
    except errors.DuplicateKeyError:
        pass
                                                        
def vreme_banjaluka():
    url = 'http://api.openweathermap.org/data/2.5/weather?q=banja luka&appid=cc5342ce347185367d6dd8020643a404&lang=sr'
    res = requests.get(url)
    data = res.json()

    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind = data['wind']['speed']
    description = data['weather'][0]['description']
    temp = data['main']['temp']
    min_temp = data['main']['temp_min']
    max_temp = data['main']['temp_max']
    grupni_izvestaj = data['weather'][0]['main']
    vremenska_zona = data['timezone']

    tempC = temp - 273.15
    maxC = max_temp - 273.15
    minC = min_temp - 273.15
    now = datetime.datetime.now() # current date and time
    time = now.strftime("%H:%M:%S")

    global client
    db = client.vremenska_prognoza
    vreme_1 = db.vreme_srbija
    selektuj = {'grad': "Banja Luka"}
    prognoza_banjaluka =   { "$set": {
            "trenutna_temperatura": int(tempC),
            "min_temp": int(minC),
            "max_temp": int(maxC),
            "wind": int(wind),
            "opis": str(description),
            "pritisak": float(pressure),
            "vremenska_zona": int(vremenska_zona),
            "trenutno_vreme": str(time),
            "last_updated": datetime.datetime.utcnow()
    }}
    try:
        vreme_1.update_many(selektuj, prognoza_banjaluka)
    
    except errors.DuplicateKeyError:
        pass

def vreme_leskovac():
    url = 'http://api.openweathermap.org/data/2.5/weather?q=leskovac&appid=cc5342ce347185367d6dd8020643a404&lang=sr'
    res = requests.get(url)
    data = res.json()

    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind = data['wind']['speed']
    description = data['weather'][0]['description']
    temp = data['main']['temp']
    min_temp = data['main']['temp_min']
    max_temp = data['main']['temp_max']
    grupni_izvestaj = data['weather'][0]['main']
    vremenska_zona = data['timezone']

    tempC = temp - 273.15
    maxC = max_temp - 273.15
    minC = min_temp - 273.15
    now = datetime.datetime.now() # current date and time
    time = now.strftime("%H:%M:%S")

    global client
    db = client.vremenska_prognoza
    vreme_1 = db.vreme_srbija
    selektuj = {'grad': "Leskovac"}
    prognoza_leskovac =   { "$set": {
            "trenutna_temperatura": int(tempC),
            "min_temp": int(minC),
            "max_temp": int(maxC),
            "wind": int(wind),
            "opis": str(description),
            "pritisak": float(pressure),
            "vremenska_zona": int(vremenska_zona),
            "trenutno_vreme": str(time),
            "last_updated": datetime.datetime.utcnow()
    }}
    try:
        vreme_1.update_many(selektuj, prognoza_leskovac)
    
    except errors.DuplicateKeyError:
        pass

def vreme_beograd():
    url = 'http://api.openweathermap.org/data/2.5/weather?q=beograd&appid=cc5342ce347185367d6dd8020643a404&lang=sr'
    res = requests.get(url)
    data = res.json()

    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind = data['wind']['speed']
    description = data['weather'][0]['description']
    temp = data['main']['temp']
    min_temp = data['main']['temp_min']
    max_temp = data['main']['temp_max']
    grupni_izvestaj = data['weather'][0]['main']
    vremenska_zona = data['timezone']

    tempC = temp - 273.15
    maxC = max_temp - 273.15
    minC = min_temp - 273.15
    now = datetime.datetime.now() # current date and time
    time = now.strftime("%H:%M:%S")

    global client
    db = client.vremenska_prognoza
    vreme_1 = db.vreme_srbija
    selektuj = {'grad': "Beograd"}
    prognoza_beograd =   { "$set": {
            "trenutna_temperatura": int(tempC),
            "min_temp": int(minC),
            "max_temp": int(maxC),
            "wind": int(wind),
            "opis": str(description),
            "pritisak": float(pressure),
            "vremenska_zona": int(vremenska_zona),
            "trenutno_vreme": str(time),
            "last_updated": datetime.datetime.utcnow()
    }}
    try:
        vreme_1.update_many(selektuj, prognoza_beograd)
    
    except errors.DuplicateKeyError:
        pass

def vreme_novisad():
    url = 'http://api.openweathermap.org/data/2.5/weather?q=novi sad&appid=cc5342ce347185367d6dd8020643a404&lang=sr'
    res = requests.get(url)
    data = res.json()

    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind = data['wind']['speed']
    description = data['weather'][0]['description']
    temp = data['main']['temp']
    min_temp = data['main']['temp_min']
    max_temp = data['main']['temp_max']
    grupni_izvestaj = data['weather'][0]['main']
    vremenska_zona = data['timezone']

    tempC = temp - 273.15
    maxC = max_temp - 273.15
    minC = min_temp - 273.15
    now = datetime.datetime.now() # current date and time
    time = now.strftime("%H:%M:%S")

    global client
    db = client.vremenska_prognoza
    vreme_1 = db.vreme_srbija
    selektuj = {'grad': "Novi Sad"}
    prognoza_novisad =   { "$set": {
            "trenutna_temperatura": int(tempC),
            "min_temp": int(minC),
            "max_temp": int(maxC),
            "wind": int(wind),
            "opis": str(description),
            "pritisak": float(pressure),
            "vremenska_zona": int(vremenska_zona),
            "trenutno_vreme": str(time),
            "last_updated": datetime.datetime.utcnow()
    }}
    try:
        vreme_1.update_many(selektuj, prognoza_novisad)
    
    except errors.DuplicateKeyError:
        pass

def vreme_sarajevo():
    url = 'http://api.openweathermap.org/data/2.5/weather?q=sarajevo&appid=cc5342ce347185367d6dd8020643a404&lang=sr'
    res = requests.get(url)
    data = res.json()

    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind = data['wind']['speed']
    description = data['weather'][0]['description']
    temp = data['main']['temp']
    min_temp = data['main']['temp_min']
    max_temp = data['main']['temp_max']
    grupni_izvestaj = data['weather'][0]['main']
    vremenska_zona = data['timezone']

    tempC = temp - 273.15
    maxC = max_temp - 273.15
    minC = min_temp - 273.15
    now = datetime.datetime.now() # current date and time
    time = now.strftime("%H:%M:%S")

    global client
    db = client.vremenska_prognoza
    vreme_1 = db.vreme_srbija
    selektuj = {'grad': "Sarajevo"}
    prognoza_sarajevo =   { "$set": {
            "trenutna_temperatura": int(tempC),
            "min_temp": int(minC),
            "max_temp": int(maxC),
            "wind": int(wind),
            "opis": str(description),
            "pritisak": float(pressure),
            "vremenska_zona": int(vremenska_zona),
            "trenutno_vreme": str(time),
            "last_updated": datetime.datetime.utcnow()
    }}
    try:
        vreme_1.update_many(selektuj, prognoza_sarajevo)
    
    except errors.DuplicateKeyError:
        pass

if __name__ == "__main__":
    locations = {}
    
        
    while 1:
        try:
            t1 = threading.Thread(target = lambda : vreme_nis(), name='t1')
            t1.setDaemon(True)
            t2 = threading.Thread(target = lambda : vreme_banjaluka(), name='t2')
            t2.setDaemon(True)
            t3 = threading.Thread(target = lambda : vreme_leskovac(), name='t3')
            t3.setDaemon(True)
            t4 = threading.Thread(target = lambda : vreme_beograd(), name='t4')
            t4.setDaemon(True)
            t5 = threading.Thread(target = lambda : vreme_novisad(), name='t5')
            t5.setDaemon(True)
            t6 = threading.Thread(target = lambda : vreme_sarajevo(), name='t6')
            t6.setDaemon(True)


  
            t1.start()
            t1.join()
            t2.start()
            t2.join()
            t3.start()
            t3.join()
            t4.start()
            t4.join()
            t5.start()
            t5.join()
            t6.start()
            t6.join()


            time.sleep(600) 

        except Exception as e:
            print(e)