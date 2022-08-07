mport time
import pytest
from config import *
from pages.main_page import MainPage

def test_auth_no_valid_code(testing_driver):
    """ Авторизация пользователя c не валидным кодом скидки """
    page = MainPage(testing_driver)
    page.btn_my_lab.click()
    time.sleep(2)
    page.fild_email.click()
    page.fild_email.send_keys(valid_email)
    page.btn_enter.click()
    time.sleep(2)
    page.email_pod.find()
    my_email = page.email_pod.get_attribute('value')

    assert my_email == valid_email

    page.input_code_email.click()
    page.input_code_email.send_keys(no_valid_code)
    page.button_assert_and_enter.click()
    message = page.message_no_code.find()
    print(message.text)
    assert message.text == "Введенного кода не существует"


def test_valid_my_lab(testing_driver):
    """ Авторизация пользователя c валидными данными """
    page = MainPage(testing_driver)
    page.btn_my_lab.click()
    time.sleep(2)
    page.fild_email.click()
    page.fild_email.send_keys(valid_email)
    page.btn_enter.click()
    time.sleep(2)
    page.email_pod.find()
    my_email = page.email_pod.get_attribute('value')

    assert my_email == valid_email

    page.input_code_email.click()
    page.input_code_email.send_keys(email_code_enter)
    page.button_assert_and_enter.click()


def test_add_book_defer(testing_driver):
    """Проверка добавления книги в "Отложено" авторизованного пользователя"""

    page = MainPage(testing_driver)
    page.btn_my_lab.click()
    time.sleep(2)
    page.fild_email.click()
    page.fild_email.send_keys(valid_email)
    page.btn_enter.click()
    time.sleep(2)
    page.email_pod.find()
    my_email = page.email_pod.get_attribute('value')

    assert my_email == valid_email

    page.input_code_email.click()
    page.input_code_email.send_keys(email_code_enter)
    page.button_assert_and_enter.click()
    time.sleep(7)
    page.input_search.send_keys("Python")
    page.btn_search_two.click()
    page.basket.scroll_to_element()
    title_book_python = page.python_book.get_attribute('data-name')
    print(title_book_python.lower())  # Python. Искусственный интеллект, большие данные и облачные вычисления

    page.like_defer.click()
    page.btn_pending.scroll_to_element()
    page.btn_pending.click()
    page.book_python_pending.scroll_to_element()
    title_book_pending = page.book_python_pending.get_attribute('data-name')
    print(title_book_pending.lower())

    page.like_button.click()

    assert title_book_pending == title_book_pending, "Книга не добавлена в отложено"


def test_search(testing_driver):
        """Проверка поиска книг автора "Достоевский" """
        page_one = MainPage(testing_driver)
        page_one.input_search.send_keys("Достоевский")
        page_one.btn_search.click()
        # проверка, что на открытой странице есть элементы
        assert page_one.products_titles.count() > 0
        # Проверяем наличие книг автора
        for title in page_one.products_titles.get_text():
            msg = 'Wrong product in search "{}"'.format(title)
            assert 'достоевский' in title.lower(), msg



def test_check_wrong_input_in_search(testing_driver):
        """ Проверка, что ввод с неправильной раскладки клавиатуры работает нормально. """

        page_one = MainPage(testing_driver)

        # Попробуйте ввести «достоевский» с английской клавиатуры:
        page_one.input_search.send_keys("ljcnjtdcrbq")
        page_one.btn_search.click()

        # Проверяем, что пользователь может видеть список книг:
        assert page_one.products_titles.count() > 0

        # Проверяем, что пользователь нашел соответствующие книги:
        for title in page_one.products_titles.get_text():
            msg = 'Wrong product in search "{}"'.format(title)
            assert 'достоевский' in title.lower(), msg



def test_check_input_numbers_in_search(testing_driver):
        """ Проверка, что при вводе цифр поиск работает нормально. """

        page_one = MainPage(testing_driver)

        # Попробуем ввести несколько цифр:
        page_one.input_search.send_keys("123")
        page_one.btn_search.click()

        # Проверяем, что пользователь может видеть список :
        assert page_one.products_titles.count() > 0

        # Проверяем, что пользователь нашел соответствующие товары:
        for title in page_one.products_titles.get_text():
            msg = 'Wrong product in search "{}"'.format(title)
            assert '123' in title.lower(), msg




def test_filter_presence(testing_driver):
        """ Проверка кнопки фильтра "В наличии """
        page = MainPage(testing_driver)
        page.input_search.send_keys("Гримм")
        page.btn_search.click()

        if page.products_titles.count() > 0:
            page.btn_filter_presence.click()
        else:
            print("Список пуст")

        assert page.products_titles.count() > 0
        for title in page.products_titles.get_text():
            message_er = 'Wrong product in search "{}"'.format(title)
            assert 'гримм' in title.lower(), message_er

