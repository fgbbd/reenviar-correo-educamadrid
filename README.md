# Reenvío de correos de educamadrid
Programa de Python para reenviar correos no leídos del [Correo de EducaMadrid](https://correoweb.educa.madrid.org/)
Los correos se reenvían a Discord o a Gmail.

#### Discord
- Puedes prescindir de las variables de entorno `DIRECCION_REMITENTE`, `PASS_REMITENTE` y `DIRECCION_DESTINATARIO`. Necesitarás la variable `TOKEN`. 
- Necesitarás una cuenta de Discord aparte de la que recibirá los correos. Necesitarás el token de tu cuenta [^1]
- Ve a **`Ajustes de usuario > Avanzado > Modo desarrollador`**. Después ve al canal MD entre ambas cuentas, haz click derecho en él y haz click en `Copiar ID del Canal`.

#### Gmail
- Necesitarás las variables de entorno `DIRECCION_REMITENTE`, `PASS_REMITENTE` y `DIRECCION_DESTINATARIO`. No necesitarás la variable `TOKEN`. 


## Variables de entorno
> Las variables de entorno deben ponerse en un archivo .env
- **`USUARIO`**: 
  Usuario de educamadrid sin @educa.madrid.org
- **`PASSWORD`**: Contraseña de educamadrid
- **`DIRECCION_REMITENTE`**: Dirección de Gmail del correo con el que se va a a enviar a tu direccióon principal
- **`PASS_REMITENTE`**: Contraseña para aplicación de la cuenta del remitente. [^2]
- **`DIRECCION_DESTINATARIO`**: Dirección del destinatario (puede ser igual a `DIRECCION_REMITENTE`)
- **`TOKEN`**: Token de la cuenta de Discord

## Desplegar aplicación
Se puede usar Github actions con el archivo `schedule.yaml` en la carpeta `.github` para ejecutar el script 3 veces al día.


[^1]: Cómo obtener tu token [aquí](https://gist.github.com/MarvNC/e601f3603df22f36ebd3102c501116c6#how-to-get-your-discord-token-from-the-browser-console)

[^2]: Para crear una contraseña de aplicación debes [activar la autentificación en dos factores](https://support.google.com/accounts/answer/185839?hl=es) e ir a [Crear contraseñas de apliación](https://myaccount.google.com/apppasswords)  en tu cuenta de Google. Más información [aquí](https://support.google.com/accounts/answer/185833?hl=es#Create%20&%20use%20app%20passwords).

