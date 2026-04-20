import allure
import pytest
from pages.home_page import HomePage
from pages.order_page import OrderPage
from config.urls import Urls


class TestLogos:

    @allure.title('Проверка перехода по логотипу "Самокат"')
    def test_scooter_logo_redirect(self, driver):
        home_page = HomePage(driver)
        order_page = OrderPage(driver)
        home_page.open_home_page()
        home_page.accept_cookies()
        order_page.open_order_page()
        home_page.click_samokat_logo()
        current_url = home_page.get_current_url()
        assert current_url == Urls.HOME_PAGE, (
            f'Ожидался URL: {Urls.HOME_PAGE}\n'
            f'Получен URL: {current_url}'
        )

    @allure.title('Проверка перехода по логотипу "Яндекс"')
    def test_yandex_logo_redirect(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.accept_cookies()
        home_page.click_yandex_logo()
        home_page.switch_to_new_window()
        home_page.wait_dzen_logo()
        current_url = home_page.get_current_url()
        assert current_url == Urls.DZEN_HOME_PAGE,(
            f'Ожидался URL: {Urls.DZEN_HOME_PAGE}\n'
            f'Получен URL: {current_url}'
        )