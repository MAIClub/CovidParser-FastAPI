from typing import Optional
from fastapi import FastAPI
from parser import getData

app = FastAPI()
#  GET, POST, PUT, PATCH, DELETE 

@app.get("/")
async def index():
    return {"Data": "MAIDEN SELAMLAR"}

@app.get("/mai")
def mai():
    return {"mesaj": "FASTAPI ile api denemesi"}


@app.get("/uyeler/{uye_adi}")
def getUye(uye_adi: str):
    uye = {
        "batuhan" : "yenidunya",
        "dogukan" : 'ozdemir',
        "bersan" : 'uslular'
    }
    donecek_deger = ''
    try:
        donecek_deger = uye[uye_adi]
    except:
        donecek_deger = "UYE BULUNAMADI"

    return {"soyad" : donecek_deger}


@app.get('/covid')
async def getCovidData():
    data = getData()
    return {"Turkiye Geneli" : data}