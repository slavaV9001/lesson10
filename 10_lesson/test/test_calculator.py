import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.calculator_page import CalculatorPage


@allure.feature("Калькулятор")
@allure.story("Арифметические операции с задержкой")
@allure.title("Тест сложения 7 + 8 с задержкой 45 секунд")
@allure.description("""
    Тест проверяет работу калькулятора с установленной задержкой 45 секунд.

    Шаги теста:
    1. Открыть страницу калькулятора
    2. Установить задержку 45 секунд
    3. Нажать кнопки: 7, +, 8, =
    4. Дождаться результата
    5. Проверить, что результат равен 15
    """)
@allure.severity(allure.severity_level.CRITICAL)
def test_slow_calculator(driver) -> None:
    """
    Тест сложения чисел на калькуляторе с установленной задержкой.

    Args:
        driver: WebDriver — экземпляр драйвера браузера

    Returns:
        None
    """
    with allure.step("Открыть страницу калькулятора"):
        calc = CalculatorPage(driver)
        calc.open()

        # Дополнительное ожидание загрузки страницы
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        allure.attach(
            driver.get_screenshot_as_png(),
            name="Страница калькулятора открыта",
            attachment_type=allure.attachment_type.PNG,
        )

    with allure.step("Установить задержку 45 секунд"):
        calc.set_delay("45")

    with allure.step("Выполнить вычисление: 7 + 8 ="):
        calc.click_button("7")
        calc.click_button("+")
        calc.click_button("8")
        calc.click_button("=")

    with allure.step("Получить результат вычислений"):
        final_result = calc.get_result_text(45)
        allure.attach(
            f"Результат: {final_result}",
            name="Результат вычисления",
            attachment_type=allure.attachment_type.TEXT,
        )

    with allure.step("Проверить, что результат равен 15"):
        assert final_result == "15", f"Ожидалось '15', получено '{
            final_result}'"
