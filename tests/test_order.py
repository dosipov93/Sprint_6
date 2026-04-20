import allure
import pytest
from pages.home_page import HomePage
from pages.order_page import OrderPage
from config.test_data import YaScooterTestData


class TestOrder:

    @allure.title('Оформление заказа кнопкой "Заказать" в шапке')
    @allure.description('Тест проверяет полный цыкл оформления заказа, через вход кнопкой в шапке')
    @pytest.mark.parametrize('order_data',YaScooterTestData.ORDER_SETS)
    def test_order_from_header(self, driver, order_data):
        home_page = HomePage(driver)
        order_page = OrderPage(driver)
        home_page.open_home_page()
        home_page.accept_cookies()
        home_page.click_order_button_header()
        order_page.fill_first_step(order_data)
        sucсess_message = order_page.fill_second_step(order_data)
        assert 'Заказ оформлен' in sucсess_message, ('Сообщение об успешном заказе не появилось!\n')

    @allure.title('Оформление заказа кнопкой "Заказать" в низу страницы')
    @allure.description('Тест проверяет полный цыкл оформления заказа, через вход кнопкой в низу страницы')
    @pytest.mark.parametrize('order_data',YaScooterTestData.ORDER_SETS)
    def test_order_from_footer(self, driver, order_data):
        home_page = HomePage(driver)
        order_page = OrderPage(driver)
        home_page.open_home_page()
        home_page.accept_cookies()
        home_page.click_order_button_bottom()
        order_page.fill_first_step(order_data)
        sucсess_message = order_page.fill_second_step(order_data)
        assert 'Заказ оформлен' in sucсess_message, ('Сообщение об успешном заказе не появилось!\n')