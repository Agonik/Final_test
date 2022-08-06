В данном репозитории представлен проект по тестированию сайта книжного магазина "Лабиринт" https://www.labirint.ru/.
Для тестирование используется паттерн Smart PageObject Осуществляется тестиование кнопок главной страницы, авторизацию пользователя, смена геолокации,разделы всплывающего меню. Тесты осуществляют запуск через Run,с использованиеь фикстур.
В файле test_button.py - находятся проверки основных кнопок и смена геолокации. В файле test_main.py - находятся проверки авторизации.
команды для запуска python -m pytest -v --driver Chrome --driver-path (*/chromedriver.exe)  tests/test_button.py,  
python -m pytest -v --driver Chrome --driver-path (*/chromedriver.exe)  tests/test_main.py,  где (*/chromedriver.exe) -путь к драйверу
