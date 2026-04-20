from selenium.webdriver.common.by import By


class OrderPageLocators:
    FIRST_NAME_FIELD = (By.XPATH, "//input[contains(@placeholder, '* Имя')]") # Поле ввода 'Имя'
    LAST_NAME_FIELD = (By.XPATH, "//input[contains(@placeholder, '* Фамилия')]") # Поле ввода 'Фамилия'
    ADRESS_FIELD = (By.XPATH, "//input[contains(@placeholder, '* Адрес: куда привезти заказ')]") # Поле ввода 'Адресс'
    METRO_FIELD = (By.XPATH, "//input[contains(@placeholder, '* Станция метро')]") # Поле ввода 'Станция метро'
    METRO_SELECT_DROPDOWN = (By.XPATH, "//div[contains(@class, 'select-search__select')]//li[1]") # Выбор ст Метро из выпадающего списка
    PHONE_NUMBER_FIELD = (By.XPATH, "//input[contains(@placeholder, '* Телефон: на него позвонит курьер')]") # Поле ввода 'Номер телефона'
    NEXT_BTN = (By.XPATH, "//button[text()='Далее']") # Кнопка 'Далее'
    COMMENT_FOR_COURIER_FIELD = (By.XPATH, "//input[contains(@placeholder, 'Комментарий для курьера')]") # Поле ввода комментария для курьера
    BLACK_COLOR = (By.ID, "black") # Чекбокс выбора цвета самоката 'black'
    GREY_COLOR = (By.ID, "grey") # Чекбокс выбора цвета самоката 'grey'
    DATE_FIELD = (By.XPATH, "//input[contains(@placeholder, '* Когда привезти самокат')]") # Опция выбора даты доставки самоката
    RENT_FIELD = (By.XPATH, "//div[contains(@class, 'Dropdown-placeholder') and contains(., '* Срок аренды')]") # Поле выбора срока аренды 
    RENT_OPTION_3_DAYS = (By.XPATH, "//div[@class='Dropdown-option' and text()='трое суток']") # Опция выбора срока аренды сроком на 'трое суток'
    RENT_OPTION_7_DAYS = (By.XPATH, "//div[@class='Dropdown-option' and text()='семеро суток']") # Опция выбора срока аренды сроком на 'семеро суток'
    ORDER_BTN = (By.XPATH, "//button[text()='Назад']/following-sibling::button") # Кнопка 'Заказать'
    YES_BTN = (By.XPATH, "//button[text()='Да']") # Кнопка подтверждения заказа 'Да'
    ORDER_SUCCESS_WINDOW = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]") # Модальное окно 'Заказ оформлен'