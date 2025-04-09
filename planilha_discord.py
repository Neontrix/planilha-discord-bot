import time
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def main():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.binary_location = "/usr/bin/chromium-browser"  # Força o uso do Chromium certo

    try:
        driver = webdriver.Chrome(options=options)
        driver.get("https://www.google.com")
        time.sleep(2)
        print("Título da página:", driver.title)
    except Exception as e:
        print("Erro durante a execução:", e)
    finally:
        try:
            driver.quit()
        except:
            pass

if __name__ == "__main__":
    main()
