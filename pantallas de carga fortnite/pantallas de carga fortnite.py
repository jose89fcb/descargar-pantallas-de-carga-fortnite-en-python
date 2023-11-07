import requests
import os
from tqdm import tqdm
import time
from os import path
import requests
import os
from os import remove, stat_result
from os import path
from notifypy import Notify
import time
import random


time.sleep(4)
notification = Notify()
notification.application_name = "Pantallas de carga fortnite"
notification.title = "Fortnite"
notification.message = "Comenzando la descarga...😎"
icono = "logo/KevinORO.png"
audio = "audio/descarga.wav"
direcion = path.abspath(path.dirname(__file__))
notification.icon = path.join(direcion, icono)
notification.audio = path.join(direcion, audio)
notification.send()
time.sleep(4)

# URL de la API

api_url = "https://fortnite-api.com/v2/cosmetics/br/search/all?type=loadingscreen"



# Realiza una solicitud HTTP a la API
response = requests.get(api_url)

cadena = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
sa = []
for i in range(8):
  sa.append(random.choice(cadena))
textorandom = ''.join(sa)       

# Verifica si la solicitud fue exitosa
if response.status_code == 200:
    data = response.json()
    
    # Crea una carpeta base para las imágenes
    base_folder = f"Fortnite_{textorandom}"
    os.makedirs(base_folder, exist_ok=True)

    # Itera a través de los elementos en "data" con barra de progreso
    for item in tqdm(data["data"], desc="Descargando imágenes"):
        if item is not None and "images" in item and "other" in item["images"] and item["images"]["other"] is not None and "background" in item["images"]["other"]:
            background_url = item["images"]["other"]["background"]
            
            # Verifica si la estructura "introduction" está presente y no es None
            if "introduction" in item and item["introduction"] is not None:
                chapter = item["introduction"].get("chapter", "Desconocido")
                season = item["introduction"].get("season", "Desconocido")
            else:
                chapter = "Desconocido"
                season = "Desconocido"
            
            # Crea una carpeta para cada capítulo y temporada si no existe
            folder_path = os.path.join(base_folder, f"Capitulo_{chapter}", f"Sesion_{season}")
            os.makedirs(folder_path, exist_ok=True)
            
            # Descarga la imagen de fondo y guárdala en la carpeta correspondiente
            image_data = requests.get(background_url).content
            with open(os.path.join(folder_path, f"{item['id']}.png"), 'wb') as f:
                f.write(image_data)

            # Agrega la notificación y pausa
            
else:
    print("Error al acceder a la API:", response.status_code)


notification = Notify()
notification.application_name = "Pantallas de carga fortnite" 
notification.title = "Fortnite"
notification.message = "fin de la descarga...🥳"
icono = "logo/KevinORO.png"
audio = "audio/fin.wav"
direcion = path.abspath(path.dirname(__file__))
notification.icon = path.join(direcion, icono)
notification.audio = path.join(direcion, audio)
notification.send()
time.sleep(3)

notification = Notify()
notification.application_name = "Pantallas de carga fortnite" 
notification.title = "Fortnite"
notification.message = "Abriendo carpeta...📁"
icono = "logo/KevinORO.png"
audio = "audio/abriendo.wav"
direcion = path.abspath(path.dirname(__file__))
notification.icon = path.join(direcion, icono)
notification.audio = path.join(direcion, audio)
notification.send()

path=f"Fortnite_{textorandom}"
path=os.path.realpath(path)
os.startfile(path)
