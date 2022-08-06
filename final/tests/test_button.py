import time

from pages.main_page import MainPage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


'''Тест основных кнопок главной страницы'''

def test_btn_books(testing_driver):
    """Проверка перехода на страницу "Книги" """
    page = MainPage(testing_driver)
    page.btn_books.click()
    assert page.get_current_url() == 'https://www.labirint.ru/books/'

def test_btn_boks_else(testing_driver):
    """ Проверка кнопки Книги, переход во вкладку "Все книги" из выпадающего списка"""
    page = MainPage(testing_driver)
    variable = page.btn_books.find()
    ActionChains(testing_driver).move_to_element(variable).perform()
    page.btn_books_all.click()
    assert page.get_current_url() == "https://www.labirint.ru/books/"



def test_btn_mbooks_else(testing_driver):
    """ Проверка кнопки Книги, переход во вкладку "Молодежная литература" из выпадающего списка"""
    page = MainPage(testing_driver)
    variable = page.btn_books.find()
    ActionChains(testing_driver).move_to_element(variable).perform()
    page.btn_mbooks.click()
    assert page.get_current_url() == "https://www.labirint.ru/genres/3066/"


def test_btn_dbooks_else(testing_driver):
    """ Проверка кнопки Книги, переход во вкладку "Книги для детей" из выпадающего списка"""
    page = MainPage(testing_driver)
    variable = page.btn_books.find()
    ActionChains(testing_driver).move_to_element(variable).perform()
    variab = page.btn_dbooks.find()
    ActionChains(testing_driver).move_to_element(variab).perform()
    page.btn_dbooks_all.click()
    assert page.get_current_url() == "https://www.labirint.ru/genres/1850/"


def test_btn_kbooks_else(testing_driver):
    """ Проверка кнопки Книги, переход во вкладку "Комиксы" из выпадающего списка"""
    page = MainPage(testing_driver)
    variable = page.btn_books.find()
    ActionChains(testing_driver).move_to_element(variable).perform()
    variab = page.btn_kbooks.find()
    ActionChains(testing_driver).move_to_element(variab).perform()
    page.btn_kbooks_kom.click()
    assert page.get_current_url() == "https://www.labirint.ru/genres/2969/"


def test_btn_artbooks_else(testing_driver):
    """ Проверка кнопки Артбуки, переход во вкладку "Комиксы" из выпадающего списка"""
    page = MainPage(testing_driver)
    variable = page.btn_books.find()
    ActionChains(testing_driver).move_to_element(variable).perform()
    variab = page.btn_kbooks.find()
    ActionChains(testing_driver).move_to_element(variab).perform()
    page.btn_artbooks_kom.click()
    assert page.get_current_url() == "https://www.labirint.ru/genres/2994/"


def test_btn_childbooks_else(testing_driver):
    """ Проверка кнопки Комиксы для детей, переход во вкладку "Комиксы" из выпадающего списка"""
    page = MainPage(testing_driver)
    variable = page.btn_books.find()
    ActionChains(testing_driver).move_to_element(variable).perform()
    variab = page.btn_kbooks.find()
    ActionChains(testing_driver).move_to_element(variab).perform()
    page.btn_childbooks_kom.click()
    assert page.get_current_url() == "https://www.labirint.ru/genres/2996/"


def test_btn_nowdbooks_else(testing_driver):
    """ Проверка кнопки Новеллизации, переход во вкладку "Комиксы" из выпадающего списка"""
    page = MainPage(testing_driver)
    variable = page.btn_books.find()
    ActionChains(testing_driver).move_to_element(variable).perform()
    variab = page.btn_kbooks.find()
    ActionChains(testing_driver).move_to_element(variab).perform()
    page.btn_nowdbooks_kom.click()
    assert page.get_current_url() == "https://www.labirint.ru/genres/3136/"


def test_btn_obrdbooks_else(testing_driver):
    """ Проверка кнопки Образовательные комиксы, переход во вкладку "Комиксы" из выпадающего списка"""
    page = MainPage(testing_driver)
    variable = page.btn_books.find()
    ActionChains(testing_driver).move_to_element(variable).perform()
    variab = page.btn_kbooks.find()
    ActionChains(testing_driver).move_to_element(variab).perform()
    page.btn_obrdbooks_kom.click()
    assert page.get_current_url() == "https://www.labirint.ru/genres/2995/"


def test_btn_randbooks_else(testing_driver):
    """ Проверка кнопки Ранобэ  переход во вкладку "Комиксы" из выпадающего списка"""
    page = MainPage(testing_driver)
    variable = page.btn_books.find()
    ActionChains(testing_driver).move_to_element(variable).perform()
    variab = page.btn_kbooks.find()
    ActionChains(testing_driver).move_to_element(variab).perform()
    page.btn_randbooks_kom.click()
    assert page.get_current_url() == "https://www.labirint.ru/genres/3258/"


def test_btn_fandbooks_else(testing_driver):
    """ Проверка кнопки Фан-сувениры  переход во вкладку "Комиксы" из выпадающего списка"""
    page = MainPage(testing_driver)
    variable = page.btn_books.find()
    ActionChains(testing_driver).move_to_element(variable).perform()
    variab = page.btn_kbooks.find()
    ActionChains(testing_driver).move_to_element(variab).perform()
    page.btn_fandbooks_kom.click()
    assert page.get_current_url() == "https://www.labirint.ru/genres/3241/"


def test_btn_pbooks_else(testing_driver):
    """ Проверка кнопки Книги, переход во вкладку "Периодические издания" из выпадающего списка"""
    page = MainPage(testing_driver)
    variable = page.btn_books.find()
    ActionChains(testing_driver).move_to_element(variable).perform()
    page.btn_pbooks.click()
    assert page.get_current_url() == "https://www.labirint.ru/genres/2137/"


def test_btn_non_ficbooks(testing_driver):
    """ Проверка кнопки Бизнес.Экономика переход во вкладку "Нехудожественная литература" из выпадающего списка"""
    page = MainPage(testing_driver)
    variable = page.btn_books.find()
    ActionChains(testing_driver).move_to_element(variable).perform()
    variab = page.btn_non_ficbooks.find()
    ActionChains(testing_driver).move_to_element(variab).perform()
    page.btn_eco_non_ficbooks.click()
    assert page.get_current_url() == "https://www.labirint.ru/genres/2342/"

def test_btn_hebooks(testing_driver):
    """ Проверка кнопки Домоводство переход во вкладку "Нехудожественная литература" из выпадающего списка"""
    page = MainPage(testing_driver)
    variable = page.btn_books.find()
    ActionChains(testing_driver).move_to_element(variable).perform()
    variab = page.btn_non_ficbooks.find()
    ActionChains(testing_driver).move_to_element(variab).perform()
    page.btn_hebooks.click()
    assert page.get_current_url() == "https://www.labirint.ru/genres/2223/"


def test_btn_scienbooks(testing_driver):
    """ Проверка кнопки Естественные науки переход во вкладку "Нехудожественная литература" из выпадающего списка"""
    page = MainPage(testing_driver)
    variable = page.btn_books.find()
    ActionChains(testing_driver).move_to_element(variable).perform()
    variab = page.btn_non_ficbooks.find()
    ActionChains(testing_driver).move_to_element(variab).perform()
    page.btn_scienbooks.click()
    assert page.get_current_url() == "https://www.labirint.ru/genres/1854/"


def test_inftechnbooks(testing_driver):
    """ Проверка кнопки Информационные технологии переход во вкладку "Нехудожественная литература" из выпадающего списка"""
    page = MainPage(testing_driver)
    variable = page.btn_books.find()
    ActionChains(testing_driver).move_to_element(variable).perform()
    variab = page.btn_non_ficbooks.find()
    ActionChains(testing_driver).move_to_element(variab).perform()
    page.btn_inftechnbooks.click()
    assert page.get_current_url() == "https://www.labirint.ru/genres/2304/"


def test_cookingbooks(testing_driver):
    """ Проверка кнопки Кулинария переход во вкладку "Нехудожественная литература" из выпадающего списка"""
    page = MainPage(testing_driver)
    variable = page.btn_books.find()
    ActionChains(testing_driver).move_to_element(variable).perform()
    variab = page.btn_non_ficbooks.find()
    ActionChains(testing_driver).move_to_element(variab).perform()
    page.btn_cookingbooks.click()
    assert page.get_current_url() == "https://www.labirint.ru/genres/2192/"


def test_art_books(testing_driver):
    """ Проверка кнопки Культура. Искусство переход во вкладку "Нехудожественная литература" из выпадающего списка"""
    page = MainPage(testing_driver)
    variable = page.btn_books.find()
    ActionChains(testing_driver).move_to_element(variable).perform()
    variab = page.btn_non_ficbooks.find()
    ActionChains(testing_driver).move_to_element(variab).perform()
    page.btn_artbooks.click()
    assert page.get_current_url() == "https://www.labirint.ru/genres/2440/"


def test_health_books(testing_driver):
    """ Проверка кнопки Медицина и здоровье. Искусство переход во вкладку "Нехудожественная литература" из выпадающего списка"""
    page = MainPage(testing_driver)
    variable = page.btn_books.find()
    ActionChains(testing_driver).move_to_element(variable).perform()
    variab = page.btn_non_ficbooks.find()
    ActionChains(testing_driver).move_to_element(variab).perform()
    page.btn_healthbooks.click()
    assert page.get_current_url() == "https://www.labirint.ru/genres/2406/"


def test_hunt_books(testing_driver):
    """ Проверка кнопки Охота. Рыбалка. Собирательство. Искусство переход во вкладку "Нехудожественная литература" из выпадающего списка"""
    page = MainPage(testing_driver)
    variable = page.btn_books.find()
    ActionChains(testing_driver).move_to_element(variable).perform()
    variab = page.btn_non_ficbooks.find()
    ActionChains(testing_driver).move_to_element(variab).perform()
    page.btn_huntbooks.click()
    assert page.get_current_url() == "https://www.labirint.ru/genres/2252/"


def test_psy_books(testing_driver):
    """ Проверка кнопки Психология переход во вкладку "Нехудожественная литература" из выпадающего списка"""
    page = MainPage(testing_driver)
    variable = page.btn_books.find()
    ActionChains(testing_driver).move_to_element(variable).perform()
    variab = page.btn_non_ficbooks.find()
    ActionChains(testing_driver).move_to_element(variab).perform()
    page.btn_psybooks.click()
    assert page.get_current_url() == "https://www.labirint.ru/genres/2379/"


def test_publ_books(testing_driver):
    """ Проверка кнопки Публицистика переход во вкладку "Нехудожественная литература" из выпадающего списка"""
    page = MainPage(testing_driver)
    variable = page.btn_books.find()
    ActionChains(testing_driver).move_to_element(variable).perform()
    variab = page.btn_non_ficbooks.find()
    ActionChains(testing_driver).move_to_element(variab).perform()
    page.btn_publbooks.click()
    assert page.get_current_url() == "https://www.labirint.ru/genres/2809/"


def test_best_2022(testing_driver):
    """Проверка перехода на страницу "Главное 2022" """
    page = MainPage(testing_driver)
    page.btn_best_2022.click()
    assert page.get_current_url() == 'https://www.labirint.ru/best/'


def test_btn_school(testing_driver):
    """Проверка перехода на страницу "Школа" """
    page = MainPage(testing_driver)
    page.btn_school.click()
    assert page.get_current_url() == 'https://www.labirint.ru/school/'


def test_btn_toys(testing_driver):
    """Проверка перехода на страницу "Игрушки" """
    page = MainPage(testing_driver)
    page.btn_toys.click()
    assert page.get_current_url() == 'https://www.labirint.ru/games/'


def test_btn_office_supplies(testing_driver):
    """Проверка перехода на страницу "Канцтовары" """
    page = MainPage(testing_driver)
    page.btn_office.click()
    assert page.get_current_url() == 'https://www.labirint.ru/office/'


def test_delivery_and_payment(testing_driver):
    """Проверка перехода на страницу "Доставка и оплата" """
    page = MainPage(testing_driver)
    page.btn_delivery.click()
    assert page.get_current_url() == 'https://www.labirint.ru/help/'


def test_btn_certificates(testing_driver):
    """Проверка перехода на страницу "Сертификаты" """
    page = MainPage(testing_driver)
    page.btn_certificates.click()
    assert page.get_current_url() == 'https://www.labirint.ru/top/certificates/'


def test_btn_ratings(testing_driver):
    """Проверка перехода на страницу "Рейтинги" """
    page = MainPage(testing_driver)
    page.btn_rating.click()
    assert page.get_current_url() == 'https://www.labirint.ru/rating/?id_genre=-1&nrd=1'


def test_btn_novelty(testing_driver):
    """Проверка перехода на страницу "Новинки" """
    page = MainPage(testing_driver)
    page.btn_novelty.click()
    assert page.get_current_url() == 'https://www.labirint.ru/novelty/'


def test_btn_contact(testing_driver):
    """Проверка перехода на страницу "Контакты" """
    page = MainPage(testing_driver)
    page.btn_contact.click()

def test_btn_pending(testing_driver):
    """Проверка перехода на страницу "Отложено" """
    page = MainPage(testing_driver)
    page.btn_pending.click()
    assert page.get_current_url() == 'https://www.labirint.ru/cabinet/putorder/'


def test_btn_support(testing_driver):
    """Проверка перехода на страницу "Поддержка" """
    page = MainPage(testing_driver)
    page.btn_support.click()
    assert page.get_current_url() == 'https://www.labirint.ru/support/'


def test_btn_pick_up_point(testing_driver):
    """Проверка перехода на страницу "Пункты самовывоза" """
    page = MainPage(testing_driver)
    page.btn_maps.click()
    assert page.get_current_url() == 'https://www.labirint.ru/maps/'


def test_btn_sale(testing_driver):
    """Проверка перехода на страницу "Скидки" """
    page = MainPage(testing_driver)
    page.btn_sale.click()
    assert page.get_current_url() == 'https://www.labirint.ru/search/?discount=1&available=1&order=actd&way=back&paperbooks=1&ebooks=1&otherbooks=1'


def test_btn_club(testing_driver):
    """Проверка перехода на страницу "Клуб" """
    page = MainPage(testing_driver)
    page.btn_club.click()
    assert page.get_current_url() == 'https://www.labirint.ru/club/'


def test_btn_geolock(testing_driver):
    """Проверка смены "Местоположение" """
    page = MainPage(testing_driver)
    page.btn_geolock.click()
    page.input_city.click()
    page.input_city.send_keys("Санкт-Петербург")
    page.input_city.send_keys(Keys.ENTER)
    title = page.city_title.get_attribute('title')
    print(title)
    assert title == "Санкт-Петербург"


def test_button_else_household_goods(testing_driver):
    """ Проверка кнопки еще, переход во вкладку "Товары для дома" из выпадающего списка"""
    page = MainPage(testing_driver)
    variable = page.btn_else.find()
    ActionChains(testing_driver).move_to_element(variable).perform()
    page.household.click()
    assert page.get_current_url() == "https://www.labirint.ru/household/"



def test_button_else_cd_dvd(testing_driver):
    """ Проверка кнопки еще, переход во вкладку "СD/DVD" из выпадающего списка"""
    page = MainPage(testing_driver)
    variable = page.btn_else.find()
    ActionChains(testing_driver).move_to_element(variable).perform()
    page.cd_dvd.click()
    assert page.get_current_url() == "https://www.labirint.ru/multimedia/"


def test_button_else_souvenirs(testing_driver):
    """ Проверка кнопки еще, переход во вкладку "Сувениры" из выпадающего списка"""
    page = MainPage(testing_driver)
    variable = page.btn_else.find()
    ActionChains(testing_driver).move_to_element(variable).perform()
    page.souvenirs.click()
    assert page.get_current_url() == "https://www.labirint.ru/souvenir/"


def test_button_else_magazines(testing_driver):
    """ Проверка кнопки еще, переход во вкладку "Журналы" из выпадающего списка"""
    page = MainPage(testing_driver)
    variable = page.btn_else.find()
    ActionChains(testing_driver).move_to_element(variable).perform()
    page.magazines.click()
    assert page.get_current_url() == "https://www.labirint.ru/journals/"



def test_button_more_books_sale(testing_driver):
    """ Проверка кнопки "Больше книг со скидкой" """
    page = MainPage(testing_driver)
    page.more_books_sale.scroll_to_element()
    page.more_books_sale.click()
    assert page.get_current_url() == "https://www.labirint.ru/best/sale/"


def test_user_agreement(testing_driver):
    """ Проверка кнопки "18+"(Пользовательское соглашение) """
    page = MainPage(testing_driver)
    page.agreement.click()
    assert page.get_current_url() == "https://www.labirint.ru/agreement/"


def test_btn_recommendations(testing_driver):
    """Проверка кнопки "Что читать? Рекомендуем" """
    page = MainPage(testing_driver)
    page.btn_recom.click()

