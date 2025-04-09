from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests
import os

PLANILHA_URL = os.environ.get("PLANILHA_URL")
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)

try:
    driver.get(PLANILHA_URL)
    time.sleep(8)  # Espera carregar a planilha
    driver.save_screenshot("planilha.png")
finally:
    driver.quit()

with open("planilha.png", "rb") as img:
    files = {'file': img}
    data = {'content': '@everyone - Atualização farm semanal da planilha 📊'}
    r = requests.post(WEBHOOK_URL, data=data, files=files)

    if r.status_code == 204:
        print("Enviado com sucesso!")
    else:
        print(f"Erro ao enviar: {r.status_code} - {r.text}")
