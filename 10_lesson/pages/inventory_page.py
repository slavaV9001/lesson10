from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class InventoryPage:
    """
    Page Object для страницы инвентаря SauceDemo.
    Управляет добавлением товаров в корзину и переходом в корзину.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы инвентаря.

        Args:
            driver: WebDriver — экземпляр драйвера браузера
        """
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(driver, 20)
        self.backpack_add_button: tuple = (
            By.XPATH,
            "//button[@data-test='add-to-cart-sauce-labs-backpack']",
        )
        self.bolt_tshirt_add_button: tuple = (
            By.XPATH,
            "//button[@data-test='add-to-cart-sauce-labs-bolt-t-shirt']",
        )
        self.onesie_add_button: tuple = (
            By.XPATH,
            "//button[@data-test='add-to-cart-sauce-labs-onesie']",
        )
        self.cart_link: tuple = (By.CLASS_NAME, "shopping_cart_link")

    def add_backpack_to_cart(self) -> None:
        """
        Добавляет рюкзак Sauce Labs Backpack в корзину.

        Returns:
            None
        """
        button: WebElement = self.wait.until(
            EC.element_to_be_clickable(self.backpack_add_button)
        )
        button.click()

    def add_bolt_tshirt_to_cart(self) -> None:
        """
        Добавляет футболку Sauce Labs Bolt T-Shirt в корзину.

        Returns:
            None
        """
        button: WebElement = self.wait.until(
            EC.element_to_be_clickable(self.bolt_tshirt_add_button)
        )
        button.click()

    def add_onesie_to_cart(self) -> None:
        """
        Добавляет комбинезон Sauce Labs Onesie в корзину.

        Returns:
            None
        """
        button: WebElement = self.wait.until(
            EC.element_to_be_clickable(self.onesie_add_button)
        )
        button.click()

    def go_to_cart(self) -> None:
        """
        Переходит в корзину покупок.

        Returns:
            None
        """
        cart_link: WebElement = self.wait.until(
            EC.element_to_be_clickable(self.cart_link)
        )
        cart_link.click()
