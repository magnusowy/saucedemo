import pytest
from pages.base_page import basePage
from pages.inventory_page import inventoryPage
from pages.product_page import productPage

@pytest.fixture
def base_page(driver):
    return basePage(driver)

@pytest.fixture
def inventory_page(driver):
    return inventoryPage(driver)

@pytest.fixture
def product_page(driver):
    return productPage(driver)

