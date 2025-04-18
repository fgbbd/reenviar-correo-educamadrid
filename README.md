# Reenvío de correos de educamadrid
Programa de Python para reenviar correos no leídos del [Correo de EducaMadrid](https://correoweb.educa.madrid.org/).
Los correos se reenvían a Discord y/o a un correo electrónico.

> [!IMPORTANT]
> Se puede conectar el correo de EducaMadrid a un correo personal por medio de IMAP y SMTP. Sin embargo, no funciona con Proton.

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
1. Ejecuta `git clone https://github.com/fgbbd/reenviar-correo-educamadrid.git` en tu entorno local.
2. Haz los cambios que quieras o deja el código como está y sube el código a GitHub.
3. Ve a **`Settings` > `Secrets and variables` > `Actions`**.
4. Añade todas las variables de entorno.
5. Ve a **`Actions` > `Ejecutar Script Diario` > `Run workflow`** y prueba que funcione correctamente.


[^1]: Cómo obtener tu token [aquí](https://gist.github.com/MarvNC/e601f3603df22f36ebd3102c501116c6#how-to-get-your-discord-token-from-the-browser-console)

[^2]: Para crear una contraseña de aplicación debes [activar la autentificación en dos factores](https://support.google.com/accounts/answer/185839?hl=es) e ir a [Crear contraseñas de apliación](https://myaccount.google.com/apppasswords)  en tu cuenta de Google. Más información [aquí](https://support.google.com/accounts/answer/185833?hl=es#Create%20&%20use%20app%20passwords).