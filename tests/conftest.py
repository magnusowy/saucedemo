import os
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from config.config_loader import load_config
from pages.login_page import loginPage
from fixtures.fixtures import *

@pytest.fixture(scope="session")
def config():
    return load_config()

@pytest.fixture(scope="session")
def users(config):
    return list(config["users"].values()) # return user list

@pytest.fixture(scope="session")
def password(config):
    return config["password"]

@pytest.fixture
def session_user_login(driver, config, request):

    username = request.param
    password = config["password"]

    driver.get(config["base_url"])
    login_page = loginPage(driver)
    login_page.login_into_service(username, password)
    if login_page.is_error_displayed():
        pytest.skip(f"User '{username}' cannot log in.") # if user can't login, I skip the tests

    return login_page

@pytest.fixture(scope="function")
def driver(config) -> WebDriver:

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
    }

    options = Options()
    options.add_argument("--no-default-browser-check")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-notifications")

    # for headless - CI/CD
    #options.add_argument("--headless")  # Optional: Run in headless mode
    #options.add_argument("--disable-gpu")
    #options.add_argument("--disable-extensions")
    #options.add_argument("--ignore-certificate-errors")

    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False # removed leak detection password
    })
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    driver_path = os.path.abspath(os.path.join(os.path.dirname(__file__), config["chromedriver_path"]))
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(config["global_timeout"]) # Global timeout

    yield driver

    driver.quit()

def pytest_generate_tests(metafunc):
    if "session_user_login" in metafunc.fixturenames:
        config = load_config()
        user_values = list(config["users"].values())
        metafunc.parametrize("session_user_login", user_values, indirect=True) #indirect as a parametized login approach