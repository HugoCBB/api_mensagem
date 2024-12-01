from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class BOT_MENSAGEM:
    def __init__(self):
        self.servico = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.servico)


    def AcessarSite(self):
        link = 'https://web.whatsapp.com/'
        self.driver.get(link)
        print("Aguardando QRCode")
        sleep(30)

    def EnviarMensagem(self, numero, mensagens):
        # Procurar contato
        url = f"https://web.whatsapp.com/send?phone={numero}"
        self.driver.get(url)
        sleep(10)

        #  Enviar mensagem
        mensagem = self.driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]/p')
        mensagem.click()
        mensagem.send_keys(mensagens)
        mensagem.send_keys(Keys.RETURN)
        sleep(2)