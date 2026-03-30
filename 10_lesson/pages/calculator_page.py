from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class CalculatorPage:
    """
    Page Object для страницы калькулятора с задержкой.
    Предоставляет методы для взаимодействия с калькулятором.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы калькулятора.

        Args:
            driver: WebDriver — экземпляр драйвера браузера
        """
        self.driver: WebDriver = driver
        self.url: str = (
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/slow-calculator.html"
        )

        # Обновленные локаторы для поля задержки
        # Проверьте актуальные селекторы на странице
        self.delay_input: tuple = (By.ID, "delay")
        self.delay_input_alt: tuple = (
            By.CSS_SELECTOR, "input[placeholder*='delay']")
        self.delay_input_alt2: tuple = (
            By.XPATH, "//input[contains(@id, 'delay')]")
        self.delay_input_alt3: tuple = (
            By.CSS_SELECTOR, "input[type='number']")
        self.delay_input_alt4: tuple = (By.CLASS_NAME, "form-control")

        self.result_display: tuple = (By.CSS_SELECTOR, ".screen")

    def open(self) -> None:
        """
        Открывает страницу калькулятора.

        Returns:
            None
        """
        self.driver.get(self.url)

    def wait_for_page_load(self, timeout: int = 10) -> None:
        """
        Ожидает загрузки страницы.

        Args:
            timeout: int — максимальное время ожидания в секундах

        Returns:
            None
        """
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

    def _find_element_with_fallback(
        self, wait: WebDriverWait, locators: list, element_name: str
    ) -> WebElement:
        """
        Пытается найти элемент по нескольким локаторам.

        Args:
            wait: WebDriverWait объект
            locators: Список локаторов для поиска
            element_name: Название элемента для сообщения об ошибке

        Returns:
            WebElement: Найденный элемент

        Raises:
            TimeoutException: Если элемент не найден ни по одному локатору
        """
        for locator in locators:
            try:
                element = wait.until(EC.presence_of_element_located(locator))
                print(f"Найден элемент {element_name} по локатору: {locator}")
                return element
            except (TimeoutException, NoSuchElementException):
                print(f"Не найден по локатору: {locator}")
                continue

        raise TimeoutException(
            f"{element_name} не найден. Пробовали локаторы: {locators}"
        )

    def set_delay(self, seconds: str) -> None:
        """
        Устанавливает задержку для вычислений.

        Args:
            seconds: str — количество секунд задержки в виде строки

        Returns:
            None
        """
        wait = WebDriverWait(self.driver, 10)

        # Расширенный список локаторов
        locators = [
            self.delay_input,
            self.delay_input_alt,
            self.delay_input_alt2,
            self.delay_input_alt3,
            self.delay_input_alt4,
            (By.XPATH, "//input[@id='delay']"),
            (By.CSS_SELECTOR, "#delay"),
            (By.NAME, "delay"),
        ]

        delay = self._find_element_with_fallback(
            wait, locators, "Элемент задержки")
        delay.clear()
        delay.send_keys(seconds)

    def click_button(self, text: str) -> None:
        """
        Нажимает на кнопку калькулятора по тексту.

        Args:
            text: str — текст на кнопке (например, "7", "+", "=")

        Returns:
            None
        """
        # Пробуем разные способы найти кнопку
        locators = [
            (By.XPATH, f"//span[text()='{text}']"),
            (By.XPATH, f"//button[text()='{text}']"),
            (By.XPATH, f"//div[text()='{text}']"),
            (By.XPATH, f"//*[contains(@class, 'button') and text()='{text}']"),
        ]

        wait = WebDriverWait(self.driver, 10)
        button = None

        for locator in locators:
            try:
                button = wait.until(EC.element_to_be_clickable(locator))
                if button:
                    break
            except (TimeoutException, NoSuchElementException):
                continue

        if button is None:
            raise TimeoutException(f"Кнопка '{text}' не найдена")

        button.click()

    def get_result_text(self, wait_time: int) -> str:
        """
        Получает текст результата после ожидания.

        Args:
            wait_time: int — время ожидания в секундах

        Returns:
            str — текст результата вычислений

        Raises:
            TimeoutException: Если результат не появился за ожидаемое время
        """
        WebDriverWait(self.driver, wait_time + 10).until(
            EC.presence_of_element_located(self.result_display)
        )
        WebDriverWait(self.driver, wait_time + 5).until(
            EC.text_to_be_present_in_element(self.result_display, "15")
        )

        return self.driver.find_element(*self.result_display).text
