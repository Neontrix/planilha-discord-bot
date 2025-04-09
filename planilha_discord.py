from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests
import os

# Configurações do navegador
options = Options()
options.add_argument('--headless')  # Executa sem abrir janela
options.add_argument('--no-sandbox')  # Recomendado para o ambiente CI/CD
options.add_argument('--disable-dev-shm-usage')  # Necessário em ambientes limitados de memória
options.add_argument('--remote-debugging-port=9222')  # Essencial para ambientes headless
options.binary_location = "/snap/bin/chromium"  # ou remova se der erro

# Configurar o zoom para garantir que a página inteira seja visível
options.add_argument("force-device-scale-factor=1")

# Inicializa o serviço do ChromeDriver
service = Service(ChromeDriverManager().install())

# Inicia o navegador
driver = webdriver.Chrome(service=service, options=options)

# Acessa a planilha
planilha_url = os.environ['PLANILHA_URL']
driver.get(planilha_url)

# Aguarda a página carregar completamente (ajuste o tempo de espera conforme necessário)
driver.implicitly_wait(10)

# Defina a largura e altura da janela
custom_width = 930  # Altere para a largura desejada (em pixels)
custom_height = 750  # Altere para a altura desejada (em pixels)

# Ajusta a janela para o tamanho especificado
driver.set_window_size(custom_width, custom_height)

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
        data={"content": "✅ Planilha de farm atualizada com sucesso! - @💀┆Membro"},
        files={"file": screenshot}
    )

# Lança erro se o envio falhar
response.raise_for_status()
