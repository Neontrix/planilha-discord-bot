import tempfile
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Configura opções do Chrome
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

# Caminho binário do Chrome (ajustar conforme ambiente)
options.binary_location = "/snap/bin/chromium"

# Cria diretório temporário para o perfil do Chrome
temp_user_data_dir = tempfile.mkdtemp()
options.add_argument(f"--user-data-dir={temp_user_data_dir}")

try:
    # Inicia o driver com as opções configuradas
    driver = webdriver.Chrome(options=options)

    # Acesso à página desejada (exemplo)
    driver.get("https://www.google.com")

    # Espera apenas para fins de teste
    time.sleep(3)

    print("Título da página:", driver.title)

    # Aqui você pode colocar o resto da lógica (login, scraping, etc.)

finally:
    # Encerra o driver e remove o diretório temporário
    driver.quit()
    shutil.rmtree(temp_user_data_dir)
