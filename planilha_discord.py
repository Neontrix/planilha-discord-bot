from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import os
import traceback

def send_to_discord(file_path=None, error_msg=None):
    data = {"content": "❌ Falha ao printar a planilha."}
    files = {"file": open(file_path, "rb")} if file_path and os.path.exists(file_path) else None

    if error_msg:
        data["content"] += f"\n```{error_msg}```"

    requests.post(
        os.environ['WEBHOOK_URL'],
        data=data,
        files=files
    )

try:
    # Configurações do navegador
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)

    # Acessa a planilha
    driver.get(os.environ['PLANILHA_URL'])

    # Tira um print
    screenshot_path = "/tmp/screenshot.png"
    driver.save_screenshot(screenshot_path)
    driver.quit()

    # Envia print com mensagem de sucesso
    requests.post(
        os.environ['WEBHOOK_URL'],
        data={"content": "✅ Planilha printada com sucesso!"},
        files={"file": open(screenshot_path, "rb")}
    )

except Exception:
    screenshot_path = "/tmp/error_screenshot.png"
    try:
        driver.save_screenshot(screenshot_path)
        driver.quit()
    except:
        screenshot_path = None
    send_to_discord(file_path=screenshot_path, error_msg=traceback.format_exc())
