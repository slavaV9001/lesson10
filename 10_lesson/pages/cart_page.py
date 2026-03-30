from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class CartPage:
    """
    Page Object для страницы корзины SauceDemo.
    Управляет процессом оформления заказа.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы корзины.

        Args:
            driver: WebDriver — экземпляр драйвера браузера
        """
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(driver, 20)
        self.checkout_button: tuple = (By.ID, "checkout")

    def click_checkout(self) -> None:
        """
        Нажимает кнопку оформления заказа (Checkout).

        Returns:
            None
        """
        checkout_button: WebElement = self.wait.until(
            EC.element_to_be_clickable(self.checkout_button)
        )
        checkout_button.click()
