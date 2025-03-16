import requests #la libreria requests permette fare richieste http ad un server e mi permette interagire facilmente con i servizi web

chiave_api = "47996ffe2aa2b29f1c8ec2e51cd11207" #Chiave api ,la si può richiedere dal sito Open weather

citta = input("Inserisce la città: ")

meteo_dati= requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={citta}&units=metric&appid={chiave_api}")#con la funzione requests.get() faccio richieste http  dentro il server open weather


meteo = meteo_dati.json()['weather'][0]['main']#la funzione json praticamente mi permette di fare una sorta di traduccione del dizionario poichè diciamo che le informazioni mi arrivano in formato jason
#ESEMPIO INFORMAZIONE FORMATO JSON
"""{
    "weather": [
        {
            "main": "Clouds",
            "description": "few clouds"
        }
    ],
    "main": {
        "temp": 296.15,
        "feels_like": 295.52,
        "temp_min": 295.01,
        "temp_max": 297.61
    }
}"""

temp = meteo_dati.json()['main']['temp']#Vado a richiedere le informazioni che si trovano dentro 'main' come la temperatura temp_max etc

print(f"Il meteo è {meteo} e la temperatura è {temp}°C")
