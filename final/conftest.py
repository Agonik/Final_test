import pytest
from selenium import webdriver

path_driver = 'C:/path/chromedriver.exe'  # Путь до драйвера


@pytest.fixture(scope="session")
def testing_driver():
   """ Фикструра для запуска тестов """
   driver = webdriver.Chrome(path_driver)  # Путь до драйвера
   driver.maximize_window()

   yield driver

   driver.quit()

