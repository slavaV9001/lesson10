from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class CheckoutPage:
    """
    Page Object для страницы оформления заказа SauceDemo.
    Управляет заполнением данных покупателя и получением итоговой суммы.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы оформления заказа.

        Args:
            driver: WebDriver — экземпляр драйвера браузера
        """
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(driver, 20)
        self.first_name_input: tuple = (By.ID, "first-name")
        self.last_name_input: tuple = (By.ID, "last-name")
        self.postal_code_input: tuple = (By.ID, "postal-code")
        self.continue_button: tuple = (By.ID, "continue")
        self.total_price: tuple = (By.CLASS_NAME, "summary_total_label")

    def fill_first_name(self, first_name: str) -> None:
        """
        Заполняет поле имени покупателя.

        Args:
            first_name: str — имя покупателя

        Returns:
            None
        """
        field: WebElement = self.wait.until(
            EC.element_to_be_clickable(self.first_name_input)
        )
        field.send_keys(first_name)

    def fill_last_name(self, last_name: str) -> None:
        """
        Заполняет поле фамилии покупателя.

        Args:
            last_name: str — фамилия покупателя

        Returns:
            None
        """
        field: WebElement = self.wait.until(
            EC.element_to_be_clickable(self.last_name_input)
        )
        field.send_keys(last_name)

    def fill_postal_code(self, postal_code: str) -> None:
        """
        Заполняет поле почтового индекса.

        Args:
            postal_code: str — почтовый индекс

        Returns:
            None
        """
        field: WebElement = self.wait.until(
            EC.element_to_be_clickable(self.postal_code_input)
        )
        field.send_keys(postal_code)

    def click_continue(self) -> None:
        """
        Нажимает кнопку продолжения оформления заказа.

        Returns:
            None
        """
        continue_button: WebElement = self.wait.until(
            EC.element_to_be_clickable(self.continue_button)
        )
        continue_button.click()

    def get_total_price(self) -> str:
        """
        Получает итоговую сумму заказа.

        Returns:
            str — текст с итоговой суммой (например, "Total: $58.29")
        """
        total_element: WebElement = self.wait.until(
            EC.visibility_of_element_located(self.total_price)
        )
        return total_element.text
