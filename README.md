# Reenvío de correos de educamadrid
Programa de Python para reenviar correos no leídos del [Correo de EducaMadrid](https://correoweb.educa.madrid.org/)

## Variables de entorno
> Las variables de entorno deben ponerse en un archivo .env
- **`USUARIO`**: 
  Usuario de educamadrid sin @educa.madrid.org
- **`PASSWORD`**: Contraseña de educamadrid
- **`DIRECCION_REMITENTE`**: Dirección de Gmail del correo con el que se va a a enviar a tu direccióon principal
- **`PASS_REMITENTE`**: Contraseña para aplicación de la cuenta del remitente. [^1]
- **`DIRECCION_DESTINATARIO`**: Dirección del destinatario (puede ser igual a `DIRECCION_REMITENTE`)

## Desplegar aplicación
Se puede usar Github actions con el archivo `scheduler.yaml` en la carpeta `.github` para ejecutar el script 3 veces al día.

[^1]: Para crear una contraseña de aplicación debes [activar la autentificación en dos factores](https://support.google.com/accounts/answer/185839?hl=es) e ir a [Crear contraseñas de apliación](https://myaccount.google.com/apppasswords)  en tu cuenta de Google. Más información [aquí](https://support.google.com/accounts/answer/185833?hl=es#Create%20&%20use%20app%20passwords).
