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

# Obtém a posição e o tamanho do elemento que representa a área da planilha
# Ajuste esse selector para o elemento correto que representa a planilha
# No caso, você pode usar algo como "table", "tbody" ou outro identificador
planilha_element = driver.find_element("tag name", "table")  # Ajuste conforme necessário

# Obtém a posição e tamanho da planilha
location = planilha_element.location
size = planilha_element.size

# Ajuste o tamanho da janela para capturar até a coluna J (exemplo de largura de 1000px, altere conforme necessário)
driver.set_window_size(1200, size['height'])  # Definindo a altura da janela para o conteúdo da planilha
driver.set_window_position(0, location['y'])  # Ajuste a posição da janela para capturar a área desejada

# Captura de tela da área visível da janela
screenshot_path = "/tmp/screenshot.png"
driver.save_screenshot(screenshot_path)

# Fecha o navegador
driver.quit()

# Envia o print no Discord
webhook_url = os.environ['WEBHOOK_URL']
with open(screenshot_path, "rb") as screenshot:
    response = requests.post(
        webhook_url,
        data={"content": "✅ Planilha de farm atualizada com sucesso! - "},
        files={"file": screenshot}
    )

# Lança erro se o envio falhar
response.raise_for_status()
