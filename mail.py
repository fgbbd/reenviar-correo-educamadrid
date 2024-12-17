import smtplib, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

def send(asunto, cuerpo):

    remitente = os.getenv('DIRECCION_REMITENTE')
    password = os.getenv('PASS_REMITENTE')
    destinatario = os.getenv('DIRECCION_DESTINATARIO')

    mensaje = MIMEMultipart()
    mensaje["From"] = remitente
    mensaje["To"] = destinatario
    mensaje["Subject"] = f'Educamadrid: {asunto}'

    mensaje.attach(MIMEText(cuerpo, "plain"))

    try:
        servidor = smtplib.SMTP("smtp.gmail.com", 587)
        servidor.ehlo()  # Identificación al servidor
        servidor.starttls()  # Iniciar la conexión segura
        servidor.login(remitente, password)
        servidor.sendmail(remitente, destinatario, mensaje.as_string())
    except Exception as e:
        print(f"Error al enviar el correo: {e}")
    finally:
        servidor.quit()

if __name__ == "__main__":
    send("Asunto", "Cuerpo del mensaje")