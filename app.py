from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time,os, webbrowser
from dotenv import load_dotenv
from mail import send

def get_content(driver, id):
    xpath = f'//*[@id="{id}"]/td[2]/span[3]/a'
    element = driver.find_element(By.XPATH, xpath)

    link = element.get_attribute("href")
    driver.execute_script(f"window.open('{link}', '_blank');")
    driver.switch_to.window(driver.window_handles[-1])

    # Asunto
    asunto_elemento = driver.find_element(By.XPATH, '//*[@id="message-header"]/h2')
    asunto = asunto_elemento.text

    # Cuerpo
    cuerpo_elemento = driver.find_element(By.XPATH, '//*[@id="message-htmlpart1"]/div')
    cuerpo = cuerpo_elemento.text

    send(asunto, cuerpo)

    driver.close()
    driver.switch_to.window(driver.window_handles[0])

def show(tr_elements, driver):
    for tr in tr_elements:
        id = tr.get_attribute("id")
        get_content(driver, id)

def scrape():
    load_dotenv()
    user = os.getenv("USUARIO")
    password = os.getenv("PASSWORD")

    options = Options()
    options.add_argument("--headless")

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
        show(tr_elements, driver)
    else:
        print("No hay ningún mensaje nuevo.")

    driver.quit()




scrape()