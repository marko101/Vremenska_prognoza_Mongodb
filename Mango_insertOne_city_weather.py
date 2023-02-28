from pymongo import MongoClient
from dotenv import load_dotenv
import os
import datetime


load_dotenv()
MONGODB_URL = os.environ["MONGODB_URL"]


client = MongoClient(MONGODB_URL)

#listanje svih kolekcija u bazi
for db_name in client.list_database_names():
    print(db_name)


#Pristup bazi
db = client.vremenska_prognoza

#Pristup kolekciji
vreme_1 = db.vreme_srbija

vr_1 = 28

prognoza_nis =     {
        "grad" : "Banja Luka",
        "trenutna_temperatura": int(vr_1),
        "min_temp": "9",
        "max_temp": "25",
        "wind": "5",
        "opis": "razbacani oblaci",
        "pritisak": "1020",
        "vremenska_zona": "3600",
        "last_updated": datetime.datetime.utcnow(),
}

# Komanda ubaci jedan
result = vreme_1.insert_one(prognoza_nis)

client.close()