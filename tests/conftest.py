import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests (chrome/firefox/edge)"
    )

@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser").lower()
    logger.info(f"Setting up {browser_name} browser")
    
    try:
        if browser_name == "chrome":
            options = webdriver.ChromeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()),
                options=options
            )
        elif browser_name == "firefox":
            options = webdriver.FirefoxOptions()
            driver = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install()),
                options=options
            )
        elif browser_name == "edge":
            options = webdriver.EdgeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            driver = webdriver.Edge(
                service=EdgeService(EdgeChromiumDriverManager().install()),
                options=options
            )
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")
        
        driver.maximize_window()
        logger.info(f"Successfully initialized {browser_name} browser")
        yield driver
        
    except Exception as e:
        logger.error(f"Failed to initialize {browser_name} browser: {str(e)}")
        raise
    finally:
        logger.info(f"Closing {browser_name} browser")
        if 'driver' in locals():
            driver.quit()