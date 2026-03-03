import time
from pages.auth_page import AuthPage
from pages.home_page import HomePage
from pages.game_card_page import GameCardPage


#Chrome
def test_auth_chrome(driver_chrome):
    driver_chrome.get("https://greshnik.pythonanywhere.com/")

    auth_page = AuthPage(driver_chrome)
    auth_page.click_login_btn()
    time.sleep(3)
    auth_page.enter_login("alibek")
    time.sleep(3)
    auth_page.enter_password("palos5555")
    time.sleep(3)
    auth_page.click_send_btn()
    time.sleep(3)

    # О сайте
    home_page = HomePage(driver_chrome)
    home_page.click_about_btn()
    time.sleep(3)
    home_page.click_logo()
    time.sleep(3)

    # Поиск игры
    home_page.enter_search("Резидент")
    time.sleep(3)
    home_page.click_search_btn()
    time.sleep(3)
    home_page.click_game_card()
    time.sleep(3)

    # Взаимодействие с видео
    game_card_page = GameCardPage(driver_chrome)

    # 1. Запуск видео (внутри произойдет скролл и вход в iframe)
    game_card_page.click_video()
    time.sleep(3)

    # 2. Fullscreen
    game_card_page.click_fullscreen_btn()
    print("Смотрим видео 20 секунд...")
    time.sleep(20)  # Сократил для теста, можете вернуть 60

    # 3. Стоп и пауза
    game_card_page.click_video_stop()
    time.sleep(2)

    # 4. Выход из fullscreen
    game_card_page.click_exit_fullscreen()
    time.sleep(2)

    # 5. Торрент (внутри произойдет выход из iframe и скролл вниз)
    game_card_page.click_torrent_download()
    time.sleep(3)

    game_card_page.click_another_game()
    time.sleep(3)

    game_card_page.click_video()
    time.sleep(3)

    game_card_page.click_fullscreen_btn()
    print("Смотрим видео 20 секунд...")
    time.sleep(20)  # Сократил для теста, можете вернуть 60

    game_card_page.click_video_stop()
    time.sleep(2)

    game_card_page.click_exit_fullscreen()
    time.sleep(2)

    game_card_page.enter_comment_add("Testing comment Chrome !")
    time.sleep(3)
    game_card_page.click_comment_send()
    time.sleep(3)

    # 6. Выход из аккаунта
    game_card_page.click_profile_btn()
    time.sleep(3)
    game_card_page.click_exit_account_btn()
    print("Тест успешно завершен!")
    time.sleep(5)





# #Edge
# def test_auth_edge(driver_edge):
#     driver_edge.get("https://greshnik.pythonanywhere.com/")
#
#     # Авторизация
#     auth_page = AuthPage(driver_edge)
#     auth_page.click_login_btn_edge()
#     time.sleep(3)
#     auth_page.enter_login_edge("alibek")
#     time.sleep(3)
#     auth_page.enter_password_edge("palos5555")
#     time.sleep(3)
#     auth_page.click_send_btn_edge()
#     time.sleep(3)
#
#     # О сайте
#     home_page = HomePage(driver_edge)
#     home_page.click_about_btn_edge()
#     time.sleep(3)
#     home_page.click_logo_edge()
#     time.sleep(3)
#
#     # Поиск игры
#     home_page.enter_search_edge("Dead space")
#     time.sleep(3)
#     home_page.click_search_btn_edge()
#     time.sleep(3)
#     home_page.click_game_card_edge()
#     time.sleep(3)
#
#     # Взаимодействие с видео
#     game_card_page = GameCardPage(driver_edge)
#
#     # 1. Запуск видео (внутри произойдет скролл и вход в iframe)
#     game_card_page.click_video_edge()
#     time.sleep(3)
#
#     # 2. Fullscreen
#     game_card_page.click_fullscreen_btn_edge()
#     print("Смотрим видео 20 секунд...")
#     time.sleep(19)  # Сократил для теста, можете вернуть 60
#
#     # 3. Стоп и пауза
#     game_card_page.click_video_stop_edge()
#     time.sleep(2)
#
#     # 4. Выход из fullscreen
#     game_card_page.click_exit_fullscreen_edge()
#     time.sleep(2)
#
#     # 5. Торрент (внутри произойдет выход из iframe и скролл вниз)
#     game_card_page.click_torrent_download_edge()
#     time.sleep(3)
#
#     game_card_page.click_another_game_edge()
#     time.sleep(3)
#
#     game_card_page.click_video_edge()
#     time.sleep(3)
#
#     game_card_page.click_fullscreen_btn_edge()
#     print("Смотрим видео 20 секунд...")
#     time.sleep(20)
#
#     game_card_page.click_video_stop_edge()
#     time.sleep(2)
#
#     game_card_page.click_exit_fullscreen_edge()
#     time.sleep(2)
#
#     game_card_page.enter_comment_add_edge("Testing comment Edge !")
#     time.sleep(3)
#     game_card_page.click_comment_send_edge()
#     time.sleep(3)
#
#     # 6. Выход из аккаунта
#     game_card_page.click_profile_btn_edge()
#     time.sleep(3)
#     game_card_page.click_exit_account_btn_edge()
#     print("Тест успешно завершен!")
#     time.sleep(4)


#FireFox
# def test_auth_firefox(driver_firefox):
#     driver_firefox.get("https://greshnik.pythonanywhere.com/")
#
#     auth_page = AuthPage(driver_firefox)
#     auth_page.click_login_btn_firefox()
#     time.sleep(3)
#     auth_page.enter_login_firefox("test@gmail.com")
#     time.sleep(3)
#     auth_page.enter_password_firefox("qawow1221")
#     time.sleep(3)
#     auth_page.click_send_btn_firefox()
#     time.sleep(3)
#
#
#     home_page = HomePage(driver_firefox)
#     home_page.click_about_btn_firefox()
#     time.sleep(3)
#     home_page.click_logo_firefox()
#     time.sleep(3)
#
#     home_page.enter_search_firefox("Dead space")
#     time.sleep(3)
#     home_page.click_search_btn_firefox()
#     time.sleep(3)
#     home_page.click_game_card_firefox()
#     time.sleep(3)
#
#
#     game_card_page = GameCardPage(driver_firefox)
#     game_card_page.click_video_firefox()
#     time.sleep(3)
#     game_card_page.click_fullscreen_btn_firefox()
#     time.sleep(21)
#     game_card_page.click_video_stop_firefox()
#     time.sleep(3)
#     game_card_page.click_exit_fullscreen_firefox()
#     time.sleep(3)
#     game_card_page.click_torrent_download_firefox()
#     time.sleep(3)
#
#     game_card_page.click_another_game_firefox()
#     time.sleep(3)
#     game_card_page.click_video_firefox()
#     time.sleep(3)
#     game_card_page.click_fullscreen_btn_firefox()
#     time.sleep(21)
#     game_card_page.click_video_stop_firefox()
#     time.sleep(3)
#     game_card_page.click_exit_fullscreen_firefox()
#     time.sleep(3)
#
#     game_card_page.enter_comment_add_firefox("FireFox Comment test !")
#     time.sleep(3)
#     game_card_page.click_comment_send_firefox()
#     time.sleep(3)
#
#     game_card_page.click_profile_btn_firefox()
#     time.sleep(3)
#     game_card_page.click_exit_account_btn_firefox()
#     time.sleep(10)





