from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time,os, webbrowser
from dotenv import load_dotenv
from mail import send
from discord import message

def get_content(driver, tr_elements):
    for tr in tr_elements:
        id = tr.get_attribute('id')
        # Encontrar elemento del correo
        xpath = f'//*[@id="{id}"]/td[2]/span[3]/a'
        element = driver.find_element(By.XPATH, xpath)

        # Abrir el correo en una nueva pestaña
        link = element.get_attribute("href")
        driver.execute_script(f"window.open('{link}', '_blank');")
        driver.switch_to.window(driver.window_handles[-1])

        # Asunto
        asunto_elemento = driver.find_element(By.XPATH, '//*[@id="message-header"]/h2')
        asunto = asunto_elemento.text

        # Cuerpo
        cuerpo_elemento = driver.find_element(By.XPATH, '//*[@id="message-htmlpart1"]/div')
        cuerpo = cuerpo_elemento.text

        # Enviar correo a cuenta personal
        send(asunto, cuerpo)

        # Enviar mensaje por Discord
        message(asunto, cuerpo)

        # Cerrar pestaña
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

def scrape():
    # Cargar variables de entorno
    load_dotenv()
    user = os.getenv("USUARIO")
    password = os.getenv("PASSWORD")

    # Cargar sin interfaz gráfica
    options = Options()
    options.add_argument("--headless")

    # Iniciar chromedriver
    driver = webdriver.Chrome(options=options)
    driver.get("https://correoweb.educa.madrid.org")

    # Introducir usuario
    user_element = driver.find_element(By.ID, "rcmloginuser")
    user_element.send_keys(user)

    # Introducir contraseña
    password_element = driver.find_element(By.ID, "rcmloginpwd")
    password_element.send_keys(password)

    # Iniciar sesión
    boton = driver.find_element(By.ID, "rcmloginsubmit")
    boton.click()

    time.sleep(4)
    # Buscar mensajes no leídos
    tr_elements = driver.find_elements(By.CSS_SELECTOR, 'tr.unread')

    if tr_elements:
        get_content(driver, tr_elements)
    else:
        print('Ningún mensaje detectado.')

    driver.quit()

if __name__ == "__main__":
    scrape()