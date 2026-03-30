"""
Модуль содержит Page Object модели для веб-страниц.
"""

from pages.calculator_page import CalculatorPage
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

__all__ = [
    "CalculatorPage",
    "LoginPage",
    "InventoryPage",
    "CartPage",
    "CheckoutPage"
    ]
