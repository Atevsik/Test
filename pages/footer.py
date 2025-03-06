from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Footer:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://only.digital/')

    def scroll(self):
        scroll = self.browser.find_element(By.XPATH, "//div[@class='Footer_grid__lfZ34']")
        scroll = self.browser.execute_script("arguments[0].scrollIntoView();", scroll)

    #Проверка кнопок соц сетей

    def be(self):
        wait = WebDriverWait(self.browser, 10)
        be = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//div[@class='Socials_socialsWrap__DPtp_ Footer_socials__C39yX']//a[1]")))
        be.click()
        wait.until(lambda driver: len(driver.window_handles) > 1)
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)
        assert self.browser.current_url == 'https://www.behance.net/onlydigitalagency', "Не правильный Behance"
        self.browser.close()
        self.browser.switch_to.window(self.browser.window_handles[0])

    def dp(self):
        wait = WebDriverWait(self.browser, 10)
        dp = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//div[@class='Socials_socialsWrap__DPtp_ Footer_socials__C39yX']//a[2]")))
        dp.click()
        wait.until(lambda driver: len(driver.window_handles) > 1)
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)
        sleep(6) #Долго грузится страница, можно избавится от sleep
        assert self.browser.current_url == 'https://dprofile.ru/only?utm_source=only.digital&utm_medium=referral&utm_campaign=only.digital&utm_referrer=only.digital', "Не правильный Dprofile"
        self.browser.close()
        self.browser.switch_to.window(self.browser.window_handles[0])

    def tg(self):
        wait = WebDriverWait(self.browser, 10)
        tg = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//footer[@class='Footer_root___6Q28']//a[3]")))
        tg.click()
        wait.until(lambda driver: len(driver.window_handles) > 1)
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)
        assert self.browser.current_url == 'https://t.me/onlycreativedigitalagency', "Не правильный tg"
        self.browser.close()
        self.browser.switch_to.window(self.browser.window_handles[0])

    def vk(self):
        wait = WebDriverWait(self.browser, 10)
        vk = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//footer[@class='Footer_root___6Q28']//a[4]")))
        vk.click()
        wait.until(lambda driver: len(driver.window_handles) > 1)
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)
        assert self.browser.current_url == 'https://vk.com/onlydigitalagency', "Не правильный vk"
        self.browser.close()
        self.browser.switch_to.window(self.browser.window_handles[0])

    def project(self):
        project = self.browser.find_element(
            By.XPATH,"//button[@class='buttons Button_root__GbzzH Button_regular__RLX5e Button_primary__swzAa StartProjectButton_root__jB_Lv  Footer_button__RHd0Q']")
        project.click()
        sleep(5)
        assert self.browser.current_url == 'https://only.digital/#brief', "Не открылось окно"

    def check_project(self):
        check_project = self.browser.find_element(
            By.XPATH,"//h3[contains(text(),'Ваши контакты')]")
        #Проверим наличие текста в окне
        #Дальше можно много и много проверок делать, сообщите если нужно!















