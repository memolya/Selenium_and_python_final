from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.BUTTON)
        add_to_cart_button.click()

    def should_solve_promo_quiz(self):
        """Решает промо-квиз (alert с задачкой)."""
        self.solve_quiz_and_get_code()

    def should_be_product_name_in_success_message(self):
        """Название товара в сообщении должно совпадать с реальным товаром."""
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_product_name = self.browser.find_element(
            *ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME
        ).text
        assert product_name == message_product_name, (
            f"Имя товара в сообщении не совпадает: "
            f"ожидали '{product_name}', а в сообщении '{message_product_name}'"
        )

    def should_basket_total_be_equal_to_product_price(self):
        """Стоимость корзины должна совпадать с ценой товара."""
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert product_price == basket_total, (
            f"Сумма в корзине '{basket_total}' не равна цене товара '{product_price}'"
        )

    def should_not_be_success_message(self):
        """После добавления товара в корзину пользователь не должен видеть сообщение об успехе"""
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        """После добавления товара в корзину появляется сообщение об успехе, затем исчезает"""
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME), \
            "Success message did not disappear"
