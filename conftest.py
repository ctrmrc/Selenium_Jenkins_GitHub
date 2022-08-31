from selenium import webdriver
import pytest

def pytest_addoption(parser):
    parser.addoption('--lang', action='store', default='en-gb',
                     help='Please choose language from this list: ru, en-gb')

@pytest.fixture(scope='function')
def driver(request):
    ChooseLang = request.config.getoption('lang')
    print('\n!---TEST START---!')
    url = f'http://selenium1py.pythonanywhere.com/{ChooseLang}/'
    driver = webdriver.Chrome()
    driver.get(url)
    yield driver
    print('\n!---TEST FINISH---!')
    driver.quit()