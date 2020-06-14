from selenium import webdriver
import time


class WhatsAppBot: 
    def __init__(self):
        self.message = input("Type the message: ")
        self.groups = [] #[Groups' name ""]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def sendMessage(self):
        # <span dir="auto" title="GRUPO ZAPBOT" class="_3ko75 _5h6Y_ _3Whw5">GRUPO ZAPBOT</span>
        # <div tabindex="-1" class="_3uMse">
        # <span data-icon="send" 
        self.driver.get('https://web.whatsapp.com')
        time.sleep(15)
        for group in self.groups:
            group = self.driver.find_element_by_xpath(f"//span[@title='{group}']")
            time.sleep(3)
            group.click()
            chat_box = self.driver.find_element_by_class_name(#chat_box class)
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.message)
            send_btn = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(3)
            send_btn.click()
            time.sleep(5)


bot = WhatsAppBot()
bot.sendMessage()