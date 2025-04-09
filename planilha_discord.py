from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests

PLANILHA_URL = "https://docs.google.com/spreadsheets/d/1YUA1r2_TX8rG3l6-OwNUVKhCXVExYxrq6LpOWWe5V6U/edit?usp=sharing"
WEBHOOK_URL = "https://discord.com/api/webhooks/1359614605588168767/wyxLusmy9cLmA87OwBktkYJz1f1nAHtzja_LoJh3hu6nIrDJRFADLGY5kPO8_pEHey7L"

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)

try:
    driver.get(PLANILHA_URL)
    time.sleep(8)
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
