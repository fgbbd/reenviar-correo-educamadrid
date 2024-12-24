import requests, os

def message(asunto, cuerpo, link):
    # Obtener variable de entorno
    token = os.getenv('TOKEN')

    # Asignar URL, Autorización y Contenido del mensaje
    id = 1133821801051467827 # Reemplza con la ID del canal MD
    url = f'https://discord.com/api/v10/channels/{id}/messages'
    headers = {'Authorization': token}
    json = {'content': f'# [{asunto}](<{link}>)\n{cuerpo}'}

    # Realizar solicitud
    response = requests.post(url, headers=headers, json=json)

    if response.ok:
        print('Se ha enviado el mensaje a discord correctamente.')
    else:
        print('No se ha podido enviar el mensaje a Discord.')
        print(response.json())
