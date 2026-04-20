import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.home_locators import HomePageLocators
from config.urls import Urls


class HomePage(BasePage):

    @allure.step('ОТкрыть главную страницу')
    def open_home_page(self):
        self.open_url(Urls.HOME_PAGE)
        self.wait_for_element_clickable(HomePageLocators.ACCEPT_COOKIES_BTN)

    @allure.step('Принять cookies')
    def accept_cookies(self):
        self.click_to_element(HomePageLocators.ACCEPT_COOKIES_BTN)

    @allure.step('Кликнуть по вопросу с индексом {index}')
    def click_question(self, index):
        locator = (By.XPATH, HomePageLocators.QUESTION[1].format(index))
        self.click_to_element(locator)

    @allure.step('Получить текст ответа для вопроса с индексом {index}')
    def get_answer_text(self, index):
        locator = (By.XPATH, HomePageLocators.ANSWER[1].format(index))
        return self.get_text(locator)
    
    @allure.step('Кликнуть на кнопку "Заказать" в шапке')
    def click_order_button_header(self):
        self.click_to_element(HomePageLocators.ORDER_HEADER_BTN)

    @allure.step('Кликнуть на кнопку "Заказать" внизу страницы')
    def click_order_button_bottom(self):
        self.scroll_to_element(HomePageLocators.ORDER_BOTTOM_BTN)
        self.click_to_element(HomePageLocators.ORDER_BOTTOM_BTN)

    @allure.step('Кликнуть на логотип "Самокат"')
    def click_samokat_logo(self):
        self.click_to_element(HomePageLocators.LOGO_SAMOKAT)

    @allure.step('Кликнуть на логотип "Яндекс"')
    def click_yandex_logo(self):
        self.click_to_element(HomePageLocators.LOGO_YANDEX)

    @allure.step('Дождаться появления логотипа "Дзен"')
    def wait_dzen_logo(self):
        self.wait_for_element_visible(HomePageLocators.DZEN_LOGO)

    