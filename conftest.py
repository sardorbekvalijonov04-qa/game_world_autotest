import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser choice: chrome, edge, firefox"
    )


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    is_ci = os.environ.get("GITHUB_ACTIONS")

    if browser == "chrome":
        options = ChromeOptions()

        if is_ci:
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=1920,1080")
        else:
            options.add_argument("--start-maximized")

        driver = webdriver.Chrome(options=options)

    elif browser == "edge":
        options = EdgeOptions()

        if is_ci:
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=1920,1080")
        else:
            options.add_argument("--start-maximized")

        driver = webdriver.Edge(options=options)

    elif browser == "firefox":
        options = FirefoxOptions()

        if is_ci:
            options.add_argument("--headless")
            options.add_argument("--width=1920")
            options.add_argument("--height=1080")
        else:
            driver = webdriver.Firefox(options=options)
            driver.maximize_window()
            driver.implicitly_wait(10)
            yield driver
            driver.quit()
            return

        driver = webdriver.Firefox(options=options)

    else:
        raise ValueError("Browser must be chrome, edge or firefox")

    driver.implicitly_wait(10)

    yield driver

    driver.quit()
# import pytest
# from selenium import webdriver


# @pytest.fixture
# def driver_chrome():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()

# @pytest.fixture
# def driver_edge():
#     driver = webdriver.Edge()
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()

# @pytest.fixture
# def driver_firefox():
#     driver = webdriver.Firefox()
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()
