import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def browser():
    options = Options()
    options.page_load_strategy="normal"
    service = Service()
    browser = webdriver.Chrome(service=service, options=options)
    browser.maximize_window()
    yield browser
    browser.close()
