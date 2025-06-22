import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    # Create driver inside fixture
    chrome_driver = webdriver.Chrome()

    print("Title in Chrome:", chrome_driver.title)
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(10)
    
    # Yield the driver for test use
    yield chrome_driver
    
    # Quit browser after test completes
    #chrome_driver.quit()