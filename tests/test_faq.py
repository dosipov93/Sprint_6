import allure
import pytest
from pages.home_page import HomePage
from config.test_data import YaScooterTestData


class TestFAQ:

    @allure.title('Проверка ответа на вопрос {index} в разделе "Вопросы о важном"')
    @allure.description('Валидация поведения компонента: при клике на вопрос должен раскрываться соответствующий ответ.')
    @pytest.mark.parametrize('index, expected_text',YaScooterTestData.FAQ_ANSWERS)
    def test_check_faq_answers(self, driver, index, expected_text):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.accept_cookies()
        home_page.click_question(index)
        actual_text = home_page.get_answer_text(index)
        assert actual_text == expected_text, (
            f'Ответ на вопрос {index}, не совпадает!\n'
            f'Ожидалось: {expected_text}\n'
            f'Получено: {actual_text}')