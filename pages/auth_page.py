from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait

class AuthPage:
    def __init__(self, driver):
        self.driver = driver
    #Chrome
        self.login_btn = (By.CSS_SELECTOR, "#navbarSupportedContent > ul > li:nth-child(2) > a")
        self.login = (By.CSS_SELECTOR, "#id_username")
        self.password = (By.CSS_SELECTOR, "#id_password")
        self.send_btn = (By.CSS_SELECTOR, "body > main > div > div > div > div > form > button")
        # self. = (By.CSS_SELECTOR, "")

    def click_login_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.login_btn)).click()

    def enter_login(self, login):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.login)).send_keys(login)

    def enter_password(self, password):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.password)).send_keys(password)

    def click_send_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(element_to_be_clickable(self.send_btn)).click()





    #Edge
    #     self.login_btn_edge = (By.CSS_SELECTOR, "#navbarSupportedContent > ul > li:nth-child(2) > a")
    #     self.login_edge = (By.CSS_SELECTOR, "#id_username")
    #     self.password_edge = (By.CSS_SELECTOR, "#id_password")
    #     self.send_btn_edge = (By.CSS_SELECTOR, "body > main > div > div > div > div > form > button")
    #
    # def click_login_btn_edge(self):
    #     wait = WebDriverWait(self.driver, 10)
    #     wait.until(EC.element_to_be_clickable(self.login_btn_edge)).click()
    #
    # def enter_login_edge(self, login):
    #     wait = WebDriverWait(self.driver, 10)
    #     wait.until(EC.presence_of_element_located(self.login_edge)).send_keys(login)
    #
    # def enter_password_edge(self, password):
    #     wait = WebDriverWait(self.driver, 10)
    #     wait.until(EC.presence_of_element_located(self.password_edge)).send_keys(password)
    #
    # def click_send_btn_edge(self):
    #     wait = WebDriverWait(self.driver, 10)
    #     wait.until(element_to_be_clickable(self.send_btn_edge)).click()






    #FireFox
    #     self.login_btn_firefox = (By.CSS_SELECTOR, "li.nav-item:nth-child(2) > a:nth-child(1)")
    #     self.login_firefox = (By.CSS_SELECTOR, "#id_username")
    #     self.password_firefox = (By.CSS_SELECTOR, "#id_password")
    #     self.send_btn_firefox = (By.CSS_SELECTOR, "button.btn:nth-child(4)")
    #     # self. = (By.CSS_SELECTOR, "")
    #
    # def click_login_btn_firefox(self):
    #     wait = WebDriverWait(self.driver, 10)
    #     wait.until(EC.element_to_be_clickable(self.login_btn_firefox)).click()
    #
    # def enter_login_firefox(self, login):
    #     wait = WebDriverWait(self.driver, 10)
    #     wait.until(EC.presence_of_element_located(self.login_firefox)).send_keys(login)
    #
    # def enter_password_firefox(self, password):
    #     wait = WebDriverWait(self.driver, 10)
    #     wait.until(EC.presence_of_element_located(self.password_firefox)).send_keys(password)
    #
    # def click_send_btn_firefox(self):
    #     wait = WebDriverWait(self.driver, 10)
    #     wait.until(element_to_be_clickable(self.send_btn_firefox)).click()

