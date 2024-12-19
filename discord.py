import requests, os, logging
from dotenv import load_dotenv

load_dotenv()

def message(asunto, cuerpo):
    # Obtener variable de entorno
    token = os.getenv('TOKEN')

    # Asignar URL, Autorización y Contenido del mensaje
    url = 'https://discord.com/api/v10/channels/1133821801051467827/messages'
    headers = {'Authorization': token}
    json = {'content': f'# Educamadrid: {asunto}\n{cuerpo}'}

    # Realizar solicitud
    response = requests.post(url, headers=headers, json=json)

    if response.ok:
        print('Se ha enviado el mensaje a discord correctamente.')
    else:
        print('No se ha podido enviar el mensaje a Discord.')
        print(response.json())
