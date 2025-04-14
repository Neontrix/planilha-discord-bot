from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests
import os

# Configurações do navegador
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--remote-debugging-port=9222')
options.add_argument("force-device-scale-factor=1")
options.binary_location = "/usr/bin/google-chrome"  # atualizado para usar Google Chrome

# Instancia o driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Acessa a planilha
planilha_url = os.environ['PLANILHA_URL']
driver.get(planilha_url)

# Aguarda carregamento
driver.implicitly_wait(10)

# Define tamanho da janela
custom_width = 900
custom_height = 750
driver.set_window_size(custom_width, custom_height)

# Tira print
screenshot_path = "/tmp/screenshot.png"
driver.save_screenshot(screenshot_path)

# Encerra navegador
driver.quit()

# Envia para Discord
webhook_url = os.environ['WEBHOOK_URL']
with open(screenshot_path, "rb") as screenshot:
    response = requests.post(
        webhook_url,
        data={"content": "✅ Planilha de farm atualizada com sucesso! - @everyone"},
        files={"file": screenshot}
    )

response.raise_for_status()
