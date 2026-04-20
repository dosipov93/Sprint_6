from selenium.webdriver.common.by import By

class HomePageLocators:
    ORDER_HEADER_BTN = (By.XPATH, "//button[text()='Статус заказа']/preceding-sibling::button") # Кнопка 'Заказать' в Заголовке 
    ORDER_BOTTOM_BTN = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/child::button") # Втора кнопка 'Заказать' в нижней части страницы
    ORDER_STATUS_BTN = (By.XPATH, "//button[text()='Статус заказа']") # Кнопка 'Статус заказа'
    ACCEPT_COOKIES_BTN = (By.ID, 'rcc-confirm-button') # Кнопка принять Куки 'да все привыкли'
    QUESTION = (By.XPATH, "//div[@id='accordion__heading-{}']") # FAQ - 'Вопрос'
    ANSWER = (By.XPATH, '//div[@id="accordion__panel-{}"]/p') # FAQ - 'Ответ'
    LOGO_YANDEX = (By.XPATH, "//img[@alt='Yandex']/parent::a[contains(@class, 'Header_LogoYandex')]") # Логотип 'Яндекс'
    LOGO_SAMOKAT = (By.XPATH, "//img[@alt='Scooter']/parent::a[contains(@class, 'Header_LogoScooter')]") # Логотип 'Самокат'
    DZEN_LOGO = (By.XPATH, "//a[@data-testid='logo']") # Логотип "Дзен"