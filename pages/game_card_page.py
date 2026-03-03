from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


class GameCardPage:
    def __init__(self, driver):
        self.driver = driver

#Chrome
        self.iframe_selector = (By.TAG_NAME, "iframe")
        self.video = (By.CSS_SELECTOR, "#movie_player > div.ytp-cued-thumbnail-overlay > button")
        self.fullscreen_btn = (By.CSS_SELECTOR, ".ytp-fullscreen-button")
        self.video_stop = (By.CSS_SELECTOR, "video")
        self.exit_fullscreen = (By.CSS_SELECTOR, ".ytp-fullscreen-button")
        self.torrent_download = (By.CSS_SELECTOR, "div.game_trailer a")

        self.another_game = (By.CSS_SELECTOR, "body > main > div > div > div.col-8 > div.recommendation.mt-3.p-3.text-light > div > div:nth-child(1) > div > a")
        self.video = (By.CSS_SELECTOR, "#movie_player > div.ytp-cued-thumbnail-overlay > button")
        self.fullscreen_btn = (By.CSS_SELECTOR, ".ytp-fullscreen-button")
        self.video_stop = (By.CSS_SELECTOR, "video")
        self.exit_fullscreen = (By.CSS_SELECTOR, ".ytp-fullscreen-button")

        self.comment_add = (By.CSS_SELECTOR, "#id_text")
        self.comment_send = (By.CSS_SELECTOR, "body > main > div > div > div.col-8 > div.comment_block.mt-5.text-light.p-3 > div.comment_action > form > button")

        self.profile_btn = (By.CSS_SELECTOR, "#navbarSupportedContent > ul > li.nav-item.dropdown > a")
        self.exit_account_btn = (By.CSS_SELECTOR, "#navbarSupportedContent > ul > li.nav-item.dropdown > ul > li:nth-child(4) > a")

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(1)  # Пауза для завершения анимации скролла

    def click_video(self):
        wait = WebDriverWait(self.driver, 20)
        # 1. Сначала скроллим к фрейму с видео
        self.scroll_to_element(self.iframe_selector)

        # 2. Переключаемся внутрь IFRAME
        iframe = wait.until(EC.presence_of_element_located(self.iframe_selector))
        self.driver.switch_to.frame(iframe)

        # 3. Кликаем по кнопке внутри фрейма
        wait.until(EC.element_to_be_clickable(self.video)).click()

    def click_fullscreen_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.fullscreen_btn)).click()

    def click_video_stop(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.video_stop)).click()

    def click_exit_fullscreen(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.exit_fullscreen)).click()

    def click_torrent_download(self):
        self.driver.switch_to.default_content()
        self.scroll_to_element(self.torrent_download)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.torrent_download)).click()

    def click_another_game(self):
        self.driver.switch_to.default_content()
        self.scroll_to_element(self.another_game)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.another_game)).click()

    def enter_comment_add(self, comment_add):
        self.driver.switch_to.default_content()
        self.scroll_to_element(self.comment_add)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.comment_add)).send_keys(comment_add)

    def click_comment_send(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.comment_send)).click()

    def click_profile_btn(self):
        # Если мы все еще во фрейме - выходим
        self.driver.switch_to.default_content()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.profile_btn)).click()

    def click_exit_account_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.exit_account_btn)).click()




# #Edge
#         self.iframe_selector = (By.TAG_NAME, "iframe")
#
#         self.video_edge = (By.CSS_SELECTOR, "#movie_player > div.ytp-cued-thumbnail-overlay > button")
#         self.fullscreen_btn_edge = (By.CSS_SELECTOR, ".ytp-fullscreen-button")
#         self.video_stop_edge = (By.CSS_SELECTOR, "video")
#         self.exit_fullscreen_edge = (By.CSS_SELECTOR, ".ytp-fullscreen-button")
#         self.torrent_download_edge = (By.CSS_SELECTOR, "div.game_trailer a")
#
#         self.another_game_edge = (By.CSS_SELECTOR, "body > main > div > div > div.col-8 > div.recommendation.mt-3.p-3.text-light > div > div:nth-child(1) > div > a")
#         self.video_edge = (By.CSS_SELECTOR, "#movie_player > div.ytp-cued-thumbnail-overlay > button")
#         self.fullscreen_btn_edge = (By.CSS_SELECTOR, ".ytp-fullscreen-button")
#         self.video_stop_edge = (By.CSS_SELECTOR, "video")
#         self.exit_fullscreen_edge = (By.CSS_SELECTOR, ".ytp-fullscreen-button")
#
#         self.comment_add_edge = (By.CSS_SELECTOR, "#id_text")
#         self.comment_send_edge = (By.CSS_SELECTOR, "body > main > div > div > div.col-8 > div.comment_block.mt-5.text-light.p-3 > div.comment_action > form > button")
#
#         self.profile_btn_edge = (By.CSS_SELECTOR, "#navbarSupportedContent > ul > li.nav-item.dropdown > a")
#         self.exit_account_btn_edge = (By.CSS_SELECTOR,
#                                  "#navbarSupportedContent > ul > li.nav-item.dropdown > ul > li:nth-child(4) > a")
#
#     def scroll_to_element(self, locator):
#         element = self.driver.find_element(*locator)
#         self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
#         time.sleep(1)  # Пауза для завершения анимации скролла
#
#     def click_video_edge(self):
#         wait = WebDriverWait(self.driver, 21)
#         # 1. Сначала скроллим к фрейму с видео
#         self.scroll_to_element(self.iframe_selector)
#
#         # 2. Переключаемся внутрь IFRAME
#         iframe = wait.until(EC.presence_of_element_located(self.iframe_selector))
#         self.driver.switch_to.frame(iframe)
#
#         # 3. Кликаем по кнопке внутри фрейма
#         wait.until(EC.element_to_be_clickable(self.video_edge)).click()
#
#     def click_fullscreen_btn_edge(self):
#         wait = WebDriverWait(self.driver, 10)
#         wait.until(EC.element_to_be_clickable(self.fullscreen_btn_edge)).click()
#
#     def click_video_stop_edge(self):
#         # Клик по самому видео (пауза)
#         wait = WebDriverWait(self.driver, 10)
#         wait.until(EC.element_to_be_clickable(self.video_stop_edge)).click()
#
#     def click_exit_fullscreen_edge(self):
#         wait = WebDriverWait(self.driver, 10)
#         wait.until(EC.element_to_be_clickable(self.exit_fullscreen_edge)).click()
#
#     def click_torrent_download_edge(self):
#         # 1. Выходим из IFRAME обратно на главную страницу (ВАЖНО!)
#         self.driver.switch_to.default_content()
#
#         # 2. Скроллим к кнопке торрента
#         self.scroll_to_element(self.torrent_download_edge)
#
#         wait = WebDriverWait(self.driver, 10)
#         wait.until(EC.element_to_be_clickable(self.torrent_download_edge)).click()
#
#
#     def click_another_game_edge(self):
#         self.driver.switch_to.default_content()
#         self.scroll_to_element(self.another_game_edge)
#         wait = WebDriverWait(self.driver, 10)
#         wait.until(EC.element_to_be_clickable(self.another_game_edge)).click()
#
#     def enter_comment_add_edge(self, comment_add):
#         self.driver.switch_to.default_content()
#         self.scroll_to_element(self.comment_add_edge)
#         wait = WebDriverWait(self.driver, 10)
#         wait.until(EC.presence_of_element_located(self.comment_add_edge)).send_keys(comment_add)
#
#     def click_comment_send_edge(self):
#         wait = WebDriverWait(self.driver, 10)
#         wait.until(EC.element_to_be_clickable(self.comment_send_edge)).click()
#
#     def click_profile_btn_edge(self):
#         # Если мы все еще во фрейме - выходим
#         self.driver.switch_to.default_content()
#         wait = WebDriverWait(self.driver, 10)
#         wait.until(EC.element_to_be_clickable(self.profile_btn_edge)).click()
#
#     def click_exit_account_btn_edge(self):
#         wait = WebDriverWait(self.driver, 10)
#         wait.until(EC.element_to_be_clickable(self.exit_account_btn_edge)).click()







# #FireFox
#         self.iframe_selector = (By.TAG_NAME, "iframe")
#
#         self.video_firefox = (By.CSS_SELECTOR, ".ytp-large-play-button")
#         self.fullscreen_btn_firefox = (By.CSS_SELECTOR, ".ytp-fullscreen-button")
#         self.video_stop_firefox = (By.CSS_SELECTOR, ".video-stream")
#         self.exit_fullscreen_firefox = (By.CSS_SELECTOR, ".ytp-fullscreen-button")
#         self.torrent_download_firefox = (By.CSS_SELECTOR, "a.btn-success")
#
#         self.another_game_firefox = (By.CSS_SELECTOR, "div.col:nth-child(1) > div:nth-child(1)")
#         self.video_firefox = (By.CSS_SELECTOR, ".ytp-large-play-button")
#         self.fullscreen_btn_firefox = (By.CSS_SELECTOR, ".ytp-fullscreen-button")
#         self.video_stop_firefox = (By.CSS_SELECTOR, ".video-stream")
#         self.exit_fullscreen_firefox = (By.CSS_SELECTOR, ".ytp-fullscreen-button")
#
#         self.comment_add_firefox = (By.CSS_SELECTOR, "textarea.form-control:nth-child(2)")
#         self.comment_send_firefox = (By.CSS_SELECTOR, "button.btn-success")
#
#         self.profile_btn_firefox = (By.CSS_SELECTOR, ".dropdown-toggle")
#         self.exit_account_btn_firefox = (By.CSS_SELECTOR, ".dropdown-menu > li:nth-child(4) > a:nth-child(1)")
#
#     def scroll_to_element(self, locator):
#         element = self.driver.find_element(*locator)
#         self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
#         time.sleep(1)  # Пауза для завершения анимации скролла
#
#     def click_video_firefox(self):
#         wait = WebDriverWait(self.driver, 21)
#         # 1. Сначала скроллим к фрейму с видео
#         self.scroll_to_element(self.iframe_selector)
#
#         # 2. Переключаемся внутрь IFRAME
#         iframe = wait.until(EC.presence_of_element_located(self.iframe_selector))
#         self.driver.switch_to.frame(iframe)
#
#         # 3. Кликаем по кнопке внутри фрейма
#         wait.until(EC.element_to_be_clickable(self.video_firefox)).click()
#
#     def click_fullscreen_btn_firefox(self):
#         wait = WebDriverWait(self.driver, 10)
#         wait.until(EC.element_to_be_clickable(self.fullscreen_btn_firefox)).click()
#
#     def click_video_stop_firefox(self):
#         # Клик по самому видео (пауза)
#         wait = WebDriverWait(self.driver, 10)
#         wait.until(EC.element_to_be_clickable(self.video_stop_firefox)).click()
#
#     def click_exit_fullscreen_firefox(self):
#         wait = WebDriverWait(self.driver, 10)
#         wait.until(EC.element_to_be_clickable(self.exit_fullscreen_firefox)).click()
#
#     def click_torrent_download_firefox(self):
#         # 1. Выходим из IFRAME обратно на главную страницу (ВАЖНО!)
#         self.driver.switch_to.default_content()
#
#         # 2. Скроллим к кнопке торрента
#         self.scroll_to_element(self.torrent_download_firefox)
#
#         wait = WebDriverWait(self.driver, 10)
#         wait.until(EC.element_to_be_clickable(self.torrent_download_firefox)).click()
#
#
#     def click_another_game_firefox(self):
#         self.driver.switch_to.default_content()
#         self.scroll_to_element(self.another_game_firefox)
#         wait = WebDriverWait(self.driver, 10)
#         wait.until(EC.element_to_be_clickable(self.another_game_firefox)).click()
#
#     def enter_comment_add_firefox(self, comment_add):
#         self.driver.switch_to.default_content()
#         self.scroll_to_element(self.comment_add_firefox)
#         wait = WebDriverWait(self.driver, 10)
#         wait.until(EC.presence_of_element_located(self.comment_add_firefox)).send_keys(comment_add)
#
#     def click_comment_send_firefox(self):
#         wait = WebDriverWait(self.driver, 10)
#         wait.until(EC.element_to_be_clickable(self.comment_send_firefox)).click()
#
#     def click_profile_btn_firefox(self):
#         # Если мы все еще во фрейме - выходим
#         self.driver.switch_to.default_content()
#         wait = WebDriverWait(self.driver, 10)
#         wait.until(EC.element_to_be_clickable(self.profile_btn_firefox)).click()
#
#     def click_exit_account_btn_firefox(self):
#         wait = WebDriverWait(self.driver, 10)
#         wait.until(EC.element_to_be_clickable(self.exit_account_btn_firefox)).click()




