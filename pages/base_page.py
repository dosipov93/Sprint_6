import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    @allure.step('Ожидание видимости элемента')
    def wait_for_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step('Ожидание кликабельности элемента')
    def wait_for_element_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    @allure.step('Клик по элементу')
    def click_to_element(self, locator):
        self.wait_for_element_clickable(locator).click()
    
    @allure.step('Получить текст элемента')
    def get_text(self, locator):
        return self.wait_for_element_visible(locator).text

    @allure.step('Ввести данные')
    def fill_input(self, locator, text):
        element = self.wait_for_element_visible(locator)
        element.clear()
        element.send_keys(text)

    @allure.step('Вернуть текущий URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Открыть URL')
    def open_url(self, url):
        self.driver.get(url)

    @allure.step('Переключиться на новую вкладку')
    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Прокрутить до элемента')
    def scroll_to_element(self, locator):
        element = self.wait_for_element_visible(locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)


