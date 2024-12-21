import smtplib, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

def send(asunto, cuerpo_html, link):
    # Cargar variables de entorno
    remitente = os.getenv('DIRECCION_REMITENTE')
    password = os.getenv('PASS_REMITENTE')
    destinatario = os.getenv('DIRECCION_DESTINATARIO')

    # Crear cuerpo con link
    cuerpo = f"""
    <html>
    <body>
    {cuerpo_html}
    <p><a href="{link}">Abre el correo de EducaMadrid aquí</a></p>
    </body>
    </html>
    """
    # Crear mensaje
    mensaje = MIMEMultipart()
    mensaje["From"] = remitente
    mensaje["To"] = destinatario
    mensaje["Subject"] = asunto
    mensaje.attach(MIMEText(cuerpo, "html"))

    try:
        # Establecer conexión con el servidor
        servidor = smtplib.SMTP("smtp.gmail.com", 587)
        servidor.ehlo() 
        servidor.starttls()

        # Inciar sesión y enviar correo
        servidor.login(remitente, password)
        servidor.sendmail(remitente, destinatario, mensaje.as_string())

        print('Se ha enviado el mensaje por correo correctamente.')
    except Exception as e:
        print(f"Error al enviar el correo: {e}")
    finally:
        servidor.quit()