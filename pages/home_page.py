import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:
    def __init__(self, driver):
        self.driver = driver
#Chrome
        self.about_btn = (By.CSS_SELECTOR, "#navbarSupportedContent > ul > li:nth-child(1) > a")
        self.logo = (By.CSS_SELECTOR, "body > nav > div > a")
        self.search = (By.CSS_SELECTOR, "#navbarSupportedContent > form > input")
        self.search_btn = (By.CSS_SELECTOR, "#navbarSupportedContent > form > button")
        self.game_card = (By.CSS_SELECTOR,
                          "body > main > div > div.col-12.d-flex.justify-content-between.main_block > div.col-8 > div.row.row-cols-1.row-cols-md-2.row-cols-lg-3.g-4 > div:nth-child(2) > div > a")

    def scroll_to_element(self, locator):
        """Вспомогательный метод для прокрутки к элементу"""
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(1)  # Короткая пауза, чтобы скролл плавно завершился

    def click_about_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.about_btn)).click()

    def click_logo(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.logo)).click()

    def enter_search(self, search):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.search)).send_keys(search)

    def click_search_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.search_btn)).click()

    def click_game_card(self):
        # 1. Сначала скроллим вниз к карточке
        self.scroll_to_element(self.game_card)

        # 2. Ждем, пока она станет кликабельной, и жмем
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.game_card)).click()






# #Edge
#         self.about_btn_edge = (By.CSS_SELECTOR, "#navbarSupportedContent > ul > li:nth-child(1) > a")
#         self.logo_edge = (By.CSS_SELECTOR, "body > nav > div > a")
#         self.search_edge = (By.CSS_SELECTOR, "#navbarSupportedContent > form > input")
#         self.search_btn_edge = (By.CSS_SELECTOR, "#navbarSupportedContent > form > button")
#         self.game_card_edge = (By.CSS_SELECTOR,
#                           "body > main > div > div.col-12.d-flex.justify-content-between.main_block > div.col-8 > div.row.row-cols-1.row-cols-md-2.row-cols-lg-3.g-4 > div:nth-child(2) > div > a")
#
#     def scroll_to_element(self, locator):
#         wait = WebDriverWait(self.driver, 10)
#         element = wait.until(EC.presence_of_element_located(locator))
#         self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
#         time.sleep(1)  # Короткая пауза, чтобы скролл плавно завершился
#
#     def click_about_btn_edge(self):
#         wait = WebDriverWait(self.driver, 10)
#         wait.until(EC.element_to_be_clickable(self.about_btn_edge)).click()
#
#     def click_logo_edge(self):
#         wait = WebDriverWait(self.driver, 10)
#         wait.until(EC.element_to_be_clickable(self.logo_edge)).click()
#
#     def enter_search_edge(self, search_edge):
#         wait = WebDriverWait(self.driver, 10)
#         wait.until(EC.presence_of_element_located(self.search_edge)).send_keys(search_edge)
#
#     def click_search_btn_edge(self):
#         wait = WebDriverWait(self.driver, 10)
#         wait.until(EC.element_to_be_clickable(self.search_btn_edge)).click()
#
#     def click_game_card_edge(self):
#         # 1. Сначала скроллим вниз к карточке
#         self.scroll_to_element(self.game_card_edge)
#
#         # 2. Ждем, пока она станет кликабельной, и жмем
#         wait = WebDriverWait(self.driver, 10)
#         wait.until(EC.element_to_be_clickable(self.game_card_edge)).click()




# #FireFox
#         self.about_btn_firefox = (By.CSS_SELECTOR, "li.nav-item:nth-child(1) > a:nth-child(1)")
#         self.logo_firefox = (By.CSS_SELECTOR, ".navbar-brand")
#         self.search_firefox = (By.CSS_SELECTOR, ".form-control")
#         self.search_btn_firefox = (By.CSS_SELECTOR, "button.btn")
#         self.game_card_firefox = (By.CSS_SELECTOR, "div.col:nth-child(2) > div:nth-child(1)")
#
#     def scroll_to_element(self, locator):
#         wait = WebDriverWait(self.driver, 10)
#         element = wait.until(EC.presence_of_element_located(locator))
#         self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
#         time.sleep(1)  # Короткая пауза, чтобы скролл плавно завершился
#
#     def click_about_btn_firefox(self):
#         wait = WebDriverWait(self.driver, 10)
#         wait.until(EC.element_to_be_clickable(self.about_btn_firefox)).click()
#
#     def click_logo_firefox(self):
#         wait = WebDriverWait(self.driver, 10)
#         wait.until(EC.element_to_be_clickable(self.logo_firefox)).click()
#
#     def enter_search_firefox(self, search_firefox):
#         wait = WebDriverWait(self.driver, 10)
#         wait.until(EC.presence_of_element_located(self.search_firefox)).send_keys(search_firefox)
#
#     def click_search_btn_firefox(self):
#         wait = WebDriverWait(self.driver, 10)
#         wait.until(EC.element_to_be_clickable(self.search_btn_firefox)).click()
#
#     def click_game_card_firefox(self):
#         # 1. Сначала скроллим вниз к карточке
#         self.scroll_to_element(self.game_card_firefox)
#
#         # 2. Ждем, пока она станет кликабельной, и жмем
#         wait = WebDriverWait(self.driver, 10)
#         wait.until(EC.element_to_be_clickable(self.game_card_firefox)).click()
