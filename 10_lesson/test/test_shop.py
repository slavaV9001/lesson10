import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.feature("Интернет-магазин SauceDemo")
@allure.story("Оформление заказа")
@allure.title("Проверка итоговой суммы корзины при покупке трех товаров")
@allure.description("""
    Тест проверяет процесс оформления заказа в интернет-магазине SauceDemo.

    Шаги теста:
    1. Авторизация под стандартным пользователем
    2. Добавление трех товаров в корзину:
       - Sauce Labs Backpack
       - Sauce Labs Bolt T-Shirt
       - Sauce Labs Onesie
    3. Переход в корзину и оформление заказа
    4. Заполнение данных покупателя
    5. Проверка итоговой суммы заказа
    """)
@allure.severity(allure.severity_level.BLOCKER)
def test_shop_purchase(driver) -> None:
    """
    Оформление заказа и проверка итоговой суммы.

    Args:
        driver: WebDriver — экземпляр драйвера браузера

    Returns:
        None
    """
    with allure.step("Инициализация страниц"):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

    with allure.step("Открыть страницу авторизации"):
        login_page.open()
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Страница авторизации открыта",
            attachment_type=allure.attachment_type.PNG,
        )

    with allure.step("Ввод учетных данных и вход в систему"):
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()
        allure.attach(
            "Пользователь standard_user авторизован",
            name="Авторизация",
            attachment_type=allure.attachment_type.TEXT,
        )

    with allure.step("Добавление товаров в корзину"):
        inventory_page.add_backpack_to_cart()
        inventory_page.add_bolt_tshirt_to_cart()
        inventory_page.add_onesie_to_cart()
        allure.attach(
            "Добавлены товары: Backpack, Bolt T-Shirt, Onesie",
            name="Товары в корзине",
            attachment_type=allure.attachment_type.TEXT,
        )

    with allure.step("Переход в корзину и оформление заказа"):
        inventory_page.go_to_cart()
        cart_page.click_checkout()

    with allure.step("Заполнение данных покупателя"):
        checkout_page.fill_first_name("Имя")
        checkout_page.fill_last_name("Фамилия")
        checkout_page.fill_postal_code("123456")
        checkout_page.click_continue()
        allure.attach(
            "Данные покупателя: Имя, Фамилия, 123456",
            name="Данные покупателя",
            attachment_type=allure.attachment_type.TEXT,
        )

    with allure.step("Получение итоговой суммы заказа"):
        total_text = checkout_page.get_total_price()
        allure.attach(
            f"Итоговая сумма: {total_text}",
            name="Сумма заказа",
            attachment_type=allure.attachment_type.TEXT,
        )

    with allure.step("Проверка, что итоговая сумма равна $58.29"):
        assert "58.29" in total_text, (
            f"Ожидалось '$58.29' в итоговой сумме, " f"получили '{total_text}'"
        )
