import pytest
from selenium import webdriver

chromeDriver = webdriver.Chrome()
chromeDriver.maximize_window()


@pytest.fixture()
def setup(request):
    request.cls.driver = chromeDriver

