from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import tempfile
import requests
import os

# Configurações do navegador
options = Options()
options.add_argument('--headless')  # Executa sem abrir janela
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.binary_location = "/snap/bin/chromium"
options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")

# Inicia o navegador
driver = webdriver.Chrome(options=options)

# Acessa a planilha
planilha_url = os.environ['PLANILHA_URL']
driver.get(planilha_url)

# Tira screenshot
screenshot_path = "/tmp/screenshot.png"
driver.save_screenshot(screenshot_path)

# Fecha o navegador
driver.quit()

# Envia o print no Discord
webhook_url = os.environ['WEBHOOK_URL']
with open(screenshot_path, "rb") as screenshot:
    response = requests.post(
        webhook_url,
        data={"content": "✅ Planilha de farm atualizada com sucesso! - @everyone"},
        files={"file": screenshot}
    )

# (Opcional) Lança erro se o envio falhar, para forçar o "failure()" no .yml
response.raise_for_status()
