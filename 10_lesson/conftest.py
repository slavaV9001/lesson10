import sys
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

"""Добавляем корневую папку в PYTHONPATH  """
root_dir = os.path.dirname(os.path.abspath(__file__))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)


def pytest_addoption(parser):
    """Добавляем опцию для выбора браузера"""
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        choices=["chrome", "firefox"],
        help="Browser to run tests: chrome or firefox",
    )


@pytest.fixture(scope="function")
def driver(request):
    """
    Фикстура для создания и закрытия драйвера браузера.

    Args:
        request: объект запроса pytest для получения параметров

    Yields:
        WebDriver: экземпляр драйвера браузера
    """
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif browser == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver

    driver.quit()
