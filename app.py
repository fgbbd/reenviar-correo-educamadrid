import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from mail import send
from discord import message

def main():
    # Cargar variables de entorno
    user = os.getenv("USUARIO")
    password = os.getenv("PASSWORD")

    # Cargar sin interfaz gráfica
    options = Options()
    options.add_argument("--headless")

    # Iniciar chromedriver
    driver = webdriver.Chrome(options=options)
    driver.get("https://correoweb.educa.madrid.org")

    time.sleep(30)
    
    # Definir pausa hasta que los elementos existan
    wait = WebDriverWait(driver, 10) 

    # Introducir usuario
    user_element = wait.until(EC.presence_of_element_located((By.ID, "rcmloginuser")))
    user_element.send_keys(user)

    # Introducir contraseña
    password_element = wait.until(EC.presence_of_element_located((By.ID, "rcmloginpwd")))
    password_element.send_keys(password)

    # Iniciar sesión
    boton = wait.until(EC.element_to_be_clickable((By.ID, "rcmloginsubmit")))
    boton.click()

    time.sleep(4)
    # Buscar mensajes no leídos
    mails = driver.find_elements(By.CSS_SELECTOR, 'tr.unread')

    if mails:
        get_content(driver, mails)
    else:
        print('Ningún mensaje detectado.')

    driver.quit()

def get_content(driver, mails):
    for mail in mails:
        # Encontrar elemento del correo
        id = mail.get_attribute('id')
        element = driver.find_element(By.XPATH, f'//*[@id="{id}"]/td[2]/span[3]/a')

        try:
            # Abrir el correo en una nueva pestaña
            link = element.get_attribute("href")
            driver.execute_script(f"window.open('{link}', '_blank');")
            driver.switch_to.window(driver.window_handles[-1])

            # Asunto
            asunto_elemento = driver.find_element(By.XPATH, '//*[@id="message-header"]/h2')
            asunto = asunto_elemento.text

            # Cuerpo
            cuerpo_elemento = driver.find_element(By.XPATH, '//*[@id="message-htmlpart1"]/div')
            cuerpo = cuerpo_elemento.get_attribute('outerHTML')

            # Enviar correo a cuenta personal
            send(asunto, cuerpo, link)

            # Enviar mensaje por Discord
            message(asunto, cuerpo_elemento.text, link)

        except Exception as e:
            print(f"Error al obtener el contenido del correo: {e}")

        finally:
            # Cerrar pestaña
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

if __name__ == "__main__":
    main()