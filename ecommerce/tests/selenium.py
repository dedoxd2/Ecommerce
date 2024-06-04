import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

@pytest.fixture(scope="function")
def gecko_browser_instance(request):
    """
    Provide a selenium webdriver instance
    """
    options = Options()
    options.headless = False
    browser = webdriver.Firefox(options=options)

    yield browser
    browser.close()



