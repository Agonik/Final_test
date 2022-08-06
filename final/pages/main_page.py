from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://www.labirint.ru/'
        super().__init__(web_driver, url)


    # Пользовательское соглашение
    agreement = WebElement(css_selector='.b-header-e-icon-adult.b-header-e-icon-adult-m-big.b-header-e-sprite-background[href="/agreement/"]')

    # Поле поиск
    input_search = WebElement(id='search-field')
    # Кнопка поиск
    btn_search = WebElement(css_selector='.b-header-b-search-e-btntxt')

    products_titles = ManyWebElements(xpath='// *[ @ id = "rubric-tab"] / div[3] / div[1] / div[3] / div[1]')

    # Кнопка фильтра "В наличии"
    btn_filter_presence = WebElement(xpath='//*[@id="catalog-navigation"]/form[1]/div[1]/div[2]/div[1]/div[1]/a[3]/div[1]')
    # Кнопка "отложено"
    btn_pending = WebElement(xpath='// span[contains(text(), "Отложено")]')
    # Кнопка "Еще"
    btn_else = WebElement(xpath='//span[contains(text(),"Еще")]')
    # Пункт CD/DVD выпадающего списка кнопки "Ещё"
    cd_dvd = WebElement(xpath='//a[@title="Аудиокниги, музыка, видеофильмы, компьютерные программы, игры и др."]')
    # Пункт "Сувениры" выпадающего списка кнопки "Ещё"
    souvenirs = WebElement(xpath='//a[@title="Сувениры, альбомы для фотографий, фоторамки, календари."]')
    # Пункт "Журналы" выпадающего списка кнопки "Ещё"
    magazines = WebElement(xpath='//a[@title="Литературные журналы: художественные и публицистические, поэтические."]')
    # Пункт "Товары для дома" выпадающего списка кнопки "Ещё"
    household = WebElement(xpath='//a[@title="Товары для дома"]')

    # Кнопка "Книги"
    btn_books = WebElement(css_selector='.b-header-b-menu-e-text[href="/books/"]')
    # Кнопка "Главное 2022"
    btn_best_2022 = WebElement(css_selector='.b-header-b-menu-e-text[href="/best/"]')
    # Кнопка "Школа"
    btn_school = WebElement(css_selector='.b-header-b-menu-e-text[href="/school/"]')
    # Кнопка "Игрушки"
    btn_toys = WebElement(css_selector='.b-header-b-menu-e-text[href="/games/"]')
    # Кнопка "Канцтовары"
    btn_office = WebElement(css_selector='.b-header-b-menu-e-text[href="/office/"]')

    # Кнопка "Доставка и оплата"
    btn_delivery = WebElement(css_selector='.b-header-b-sec-menu-e-link[href="/help/"]')
    # Кнопка "Сертификаты"
    btn_certificates = WebElement(css_selector='.b-header-b-sec-menu-e-link[href="/top/certificates/"]')
    # Кнопка "Рейтинги"
    btn_rating = WebElement(css_selector='.b-header-b-sec-menu-e-link[href="/rating/?id_genre=-1&nrd=1"]')
    # Кнопка "Новинки"
    btn_novelty = WebElement(css_selector='.b-header-b-sec-menu-e-link[href="/novelty/"]')
    # Кнопка "Контакты"
    btn_contact = WebElement(css_selector='.b-header-b-sec-menu-e-link[href="/contact/"]')
    # Кнопка "Что читать? Рекомендуем"
    btn_recom = WebElement(css_selector='.b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long')
    # Кнопка "Поддержка"
    btn_support = WebElement(css_selector='.b-header-b-sec-menu-e-link[href="/support/"]')
    # Кнопка "1990 Пунктов самовывоза"
    btn_maps = WebElement(css_selector='.b-header-b-sec-menu-e-link[href="/maps/"]')
    # Кнопка "Скидки"
    btn_sale = WebElement(css_selector='.b-header-b-sec-menu-e-link[href="/sale/"]')
    # Кнопка "Клуб"
    btn_club = WebElement(css_selector='.b-header-b-menu-e-text[href="/club/"]')
    # Кнопка "выбора города"
    btn_geolock = WebElement(css_selector='.b-header-b-menu-e-text.js-header-menu-region-name')
    # Строка выбора города
    input_city = WebElement(id='region-post')
    city_title = WebElement(css_selector='.region-location-icon-txt')

    btn_to_cart = WebElement(id='buy819919')

    btn_ofform_close = WebElement(css_selector='.b-basket-popinfo-close[href="javascript:void(0);"]')
    cart_btn = WebElement(css_selector='.b-header-b-personal-e-link.top-link-main.analytics-click-js.cart-icon-js[href="/cart/"]')


    # Кнопка "Больше книг со скидкой"
    more_books_sale = WebElement(css_selector='.btn.btn-not-avaliable.autodiscounts__btn.autodiscounts__padding[href="/best/sale/"]')
    # Сообщение "Введенного кода не существует"
    message_no_code = WebElement(xpath='//small[contains(text(),"Введенного кода не существует")]')

    # Кнопка убрать в отложено
    like_defer = WebElement(css_selector='.icon-fave.track-tooltip.js-open-deferred-block[data-id_book="751513"]')
    # кнопка поиск
    btn_search_two = WebElement(css_selector='.b-header-b-search-e-btn')
    # в корзину
    basket = WebElement(css_selector='.btn.buy-link.btn-primary[data-idtov="751513"]')
    # python book
    python_book = WebElement(css_selector='.product.need-watch.watched[data-product-id="751513"]')
    # Книга в отложенном
    book_python_pending = WebElement(css_selector='.product.need-watch.product_labeled.product-cart.watched[data-product-id="751513"]')
    # кнопка лайк в отложенном (для того чтобы убрать из "отложено" для прохождения повторных тестов)
    like_button = WebElement(css_selector='.icon-fave.track-tooltip.js-open-deferred-block.js-deferred-remove.hovering[data-id_book="751513"]')

    btn_my_lab = WebElement(css_selector='.b-header-b-personal-e-link.top-link-main.top-link-main_cabinet.js-b-autofade-wrap[href="#"]')
    # Поле для ввода авторизации(первичное)
    fild_email = WebElement(css_selector='.new-auth__full-input.full-input.js-full-input.js-autofocus.js-input-email .full-input__input.formvalidate-error')
    # Строка email после ввода
    email_pod = WebElement(css_selector='.js-new-form.js-auth-email-sent.auth-header__module.auth-header__module_show input[name="email"]')
    # Кнопка входа для авторизации (первичная)
    btn_enter = WebElement(id='g-recap-0-btn')
    # Поле ввода кода скидки для авторизации
    input_code_email = WebElement(css_selector='.full-input__input.formvalidate-error[type="text"]')
    # Кнопка проверить и войти
    button_assert_and_enter = WebElement(xpath='//*[@id="auth-email-sent"]/input[5]')

    # Кнопка Все книги в списке книги
    btn_books_all = WebElement(xpath='//*[@id="header-genres"]/div/ul/li[3]/a')
    # Кнопка Молодежная литература в списке книги
    btn_mbooks = WebElement(xpath='//*[@id="header-genres"]/div/ul/li[7]/a')
    # Кнопка Периодические издания в списке книги
    btn_pbooks = WebElement(xpath='//*[@id="header-genres"]/div/ul/li[9]/a')

    # Кнопка детские в списке книги
    btn_dbooks = WebElement(xpath='//*[@id="header-genres"]/div/ul/li[5]/span')
    # Кнопка все книги в списке книги детские
    btn_dbooks_all = WebElement(xpath='//*[@id="header-genres"]/div/ul/li[5]/ul/li[3]/a')
    # Кнопка комиксы в списке книги
    btn_kbooks = WebElement(xpath='//*[@id="header-genres"]/div/ul/li[6]/span')
    # Кнопка комиксы в списке комиксы
    btn_kbooks_kom = WebElement(xpath='//*[@id="header-genres"]/div/ul/li[6]/ul/li[5]/a')
    # Кнопка артбуки в списке комиксы
    btn_artbooks_kom = WebElement(xpath='//*[@id="header-genres"]/div/ul/li[6]/ul/li[4]/a')
    # Кнопка комиксы для детей в списке комиксы
    btn_childbooks_kom = WebElement(xpath='//*[@id="header-genres"]/div/ul/li[6]/ul/li[6]/a')
    # Кнопка Новеллизации в списке комиксы
    btn_nowdbooks_kom = WebElement(xpath='//*[@id="header-genres"]/div/ul/li[6]/ul/li[9]/a')
    # Кнопка Образовательные комиксы в списке комиксы
    btn_obrdbooks_kom = WebElement(xpath='//*[@id="header-genres"]/div/ul/li[6]/ul/li[10]/a')
    # Кнопка Ранобэ в списке комиксы
    btn_randbooks_kom = WebElement(xpath='//*[@id="header-genres"]/div/ul/li[6]/ul/li[11]/a')
    # Кнопка Фан-сувениры в списке комиксы
    btn_fandbooks_kom = WebElement(xpath='//*[@id="header-genres"]/div/ul/li[6]/ul/li[12]/a')
    # Кнопка Нехудожественная литература в списке
    btn_non_ficbooks = WebElement(xpath='//*[@id="header-genres"]/div/ul/li[8]/span')
    # Кнопка Бизнес.Экономика в списке Нехудожественная литература
    btn_eco_non_ficbooks = WebElement(xpath='//*[@id="header-genres"]/div/ul/li[8]/ul/li[4]/a')
    # Кнопка Домоводство в списке Нехудожественная литература
    btn_hebooks = WebElement(xpath='//*[@id="header-genres"]/div/ul/li[8]/ul/li[7]/a')
    # Кнопка Естественные науки в списке Нехудожественная литература
    btn_scienbooks = WebElement(xpath='//*[@id="header-genres"]/div/ul/li[8]/ul/li[8]/a')
    # Кнопка Информационные технологии в списке Нехудожественная литература
    btn_inftechnbooks = WebElement(xpath='//*[@id="header-genres"]/div/ul/li[8]/ul/li[9]/a')
    # Кнопка Графика. Дизайн. Проектирование в списке Информационные технологии
    btn_inftechnbooks_gr = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[2]/div/div[3]/ul[2]/li[2]/a')
    # Кнопка Кулинария в списке Нехудожественная литература
    btn_cookingbooks = WebElement(xpath='//*[@id="header-genres"]/div/ul/li[8]/ul/li[14]/a')
    # Кнопка Кулинария в списке Нехудожественная литература
    btn_artbooks = WebElement(xpath='//*[@id="header-genres"]/div/ul/li[8]/ul/li[15]/a')
    # Кнопка Медицина и здоровье в списке Нехудожественная литература
    btn_healthbooks = WebElement(xpath='//*[@id="header-genres"]/div/ul/li[8]/ul/li[16]/a')
    # Кнопка Охота. Рыбалка. Собирательство в списке Нехудожественная литература
    btn_huntbooks = WebElement(xpath='//*[@id="header-genres"]/div/ul/li[8]/ul/li[17]/a')
    # Кнопка Психология в списке Нехудожественная литература
    btn_psybooks = WebElement(xpath='//*[@id="header-genres"]/div/ul/li[8]/ul/li[18]/a')
    # Кнопка Публицистика в списке Нехудожественная литература
    btn_publbooks = WebElement(xpath='//*[@id="header-genres"]/div/ul/li[8]/ul/li[19]/a')
