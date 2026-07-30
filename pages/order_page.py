import allure
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.order_locators import OrderPageLocators
from config.urls import Urls


class OrderPage(BasePage):

    @allure.step('Заполнить поле "Имя": {first_name}')
    def fill_first_name(self, first_name):
        self.fill_input(OrderPageLocators.FIRST_NAME_FIELD, first_name)

    @allure.step('Заполнить поле "Фамилия": {last_name}')
    def fill_last_name(self, last_name):
        self.fill_input(OrderPageLocators.LAST_NAME_FIELD, last_name)

    @allure.step('Заполнить поле "Адрес": {address}')
    def fill_address(self, address):
        self.fill_input(OrderPageLocators.ADRESS_FIELD, address)

    @allure.step('Выбрать станцию метро: {metro}')
    def select_metro(self, metro):
        self.fill_input(OrderPageLocators.METRO_FIELD, metro)
        self.click_to_element(OrderPageLocators.METRO_SELECT_DROPDOWN)

    @allure.step('Заполнить поле "Телефон": {phone}')
    def fill_phone(self, phone):
        self.fill_input(OrderPageLocators.PHONE_NUMBER_FIELD, phone)
    
    @allure.step('Нажать кнопку "Далее"')
    def click_next_button(self):
        self.click_to_element(OrderPageLocators.NEXT_BTN)

    @allure.step('Выбрать дату доставки')
    def select_date(self):
        self.click_to_element(OrderPageLocators.DATE_FIELD)
        self.fill_input(OrderPageLocators.DATE_FIELD, Keys.ENTER)

    @allure.step('Выбрать срок аренды: {rent_period}')
    def select_rent_period(self, rent_period):
        self.click_to_element(OrderPageLocators.RENT_FIELD)
        if rent_period == 'трое суток':
            self.click_to_element(OrderPageLocators.RENT_OPTION_3_DAYS)
        else:
            self.click_to_element(OrderPageLocators.RENT_OPTION_7_DAYS)
    
    @allure.step('Выбрать цвет самоката: {colour}')
    def select_colour(self, colour):
        if colour == 'black':
            self.click_to_element(OrderPageLocators.BLACK_COLOR)
        else:
            self.click_to_element(OrderPageLocators.GREY_COLOR)

    @allure.step('Заполнить комментарий для курьера: {comment}')
    def fill_comment(self,comment):
        self.fill_input(OrderPageLocators.COMMENT_FOR_COURIER_FIELD, comment)

    @allure.step('Нажать на кнопку "Заказать"')
    def click_order_button(self):
        self.click_to_element(OrderPageLocators.ORDER_BTN)

    @allure.step('Подтвердить заказ в модальном окне')
    def confirm_order(self):
        self.click_to_element(OrderPageLocators.YES_BTN)

    @allure.step('Проверить появления окна "Заказ оформлен"')
    def check_order_success(self):
        return self.get_text(OrderPageLocators.ORDER_SUCCESS_WINDOW)
    
    @allure.step('Окрыть страницу оформления заказа')
    def open_order_page(self):
        self.open_url(Urls.ORDER_PAGE)
        self.wait_for_element_visible(OrderPageLocators.FIRST_NAME_FIELD)
    
    @allure.step('Заполнить форму Шаг 1: Личные данные')
    def fill_first_step(self, order_data):
        self.fill_first_name(order_data['name'])
        self.fill_last_name(order_data['last_name'])
        self.fill_address(order_data['address'])
        self.select_metro(order_data['metro'])
        self.fill_phone(order_data['phone'])
        self.click_next_button()

    @allure.step('Заполнить форму Шаг 2: Доставка и подтверждение')
    def fill_second_step(self,order_data):
        self.select_date()
        self.select_rent_period(order_data['rent_period'])
        self.select_colour(order_data['colour'])
        self.fill_comment(order_data['comment'])
        self.click_order_button()
        self.confirm_order()
        return self.check_order_success()
