from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class LoginPage:
    """
    Page Object для страницы авторизации SauceDemo.
    Управляет процессом входа в систему.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы авторизации.

        Args:
            driver: WebDriver — экземпляр драйвера браузера
        """
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(driver, 20)
        self.username_input: tuple = (By.ID, "user-name")
        self.password_input: tuple = (By.ID, "password")
        self.login_button: tuple = (By.ID, "login-button")

    def open(self) -> None:
        """
        Открывает страницу авторизации SauceDemo.

        Returns:
            None
        """
        self.driver.get("https://www.saucedemo.com/")

    def enter_username(self, username: str) -> None:
        """
        Вводит имя пользователя в поле авторизации.

        Args:
            username: str — имя пользователя

        Returns:
            None
        """
        username_field: WebElement = self.wait.until(
            EC.element_to_be_clickable(self.username_input)
        )
        username_field.send_keys(username)

    def enter_password(self, password: str) -> None:
        """
        Вводит пароль в поле авторизации.

        Args:
            password: str — пароль пользователя

        Returns:
            None
        """
        password_field: WebElement = self.wait.until(
            EC.element_to_be_clickable(self.password_input)
        )
        password_field.send_keys(password)

    def click_login(self) -> None:
        """
        Нажимает кнопку входа в систему.

        Returns:
            None
        """
        login_button: WebElement = self.wait.until(
            EC.element_to_be_clickable(self.login_button)
        )
        login_button.click()
