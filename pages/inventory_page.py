from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pages.base_page import basePage

class inventoryPage(basePage):
    ADD_BACKPACK_TO_CARD_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    SAUCE_LABS_BACKPACK_IMG = (By.CSS_SELECTOR, 'img[alt="Sauce Labs Backpack"]')
    SAUCE_LABS_BACKPACK_TITLE = (By.XPATH, '//div[@class="inventory_item_name " and text()="Sauce Labs Backpack"]') # bug with class name, extra character
    SAUCE_LABS_BACKPACK_TEXT = (By.XPATH, "//div[@class='inventory_item_name ' and text()='Sauce Labs Backpack']/ancestor::div[@class='inventory_item_label']/div[@class='inventory_item_desc']")
    ADD_BIKE_LIGHT_TO_CARD_BUTTON = (By.ID, "add-to-cart-sauce-labs-bike-light")
    ADD_TSHIRT_TO_CARD_BUTTON = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ADD_FLEECE_JACKET_TO_CARD_BUTTON = (By.ID, "add-to-cart-sauce-labs-fleece-jacket")
    ADD_ONESIE_TO_CARD_BUTTON = (By.ID, "add-to-cart-sauce-labs-onesie")
    ADD_RED_TSHIRT_TO_CARD_BUTTON = (By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")

    REMOVE_BACKPACK_FROM_CARD_BUTTON = (By.ID, "remove-sauce-labs-backpack")
    REMOVE_BIKE_LIGHT_FROM_CARD_BUTTON = (By.ID, "remove-sauce-labs-bike-light")
    REMOVE_TSHIRT_FROM_CARD_BUTTON = (By.ID, "remove-sauce-labs-bolt-t-shirt")
    REMOVE_FLEECE_JACKET_FROM_CARD_BUTTON = (By.ID, "remove-sauce-labs-fleece-jacket")
    REMOVE_ONESIE_FROM_CARD_BUTTON = (By.ID, "remove-sauce-labs-onesie")
    REMOVE_RED_TSHIRT_FROM_CARD_BUTTON = (By.ID, "remove-test.allthethings()-t-shirt-(red)")

    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    SORT_VALUES = {"name_a_to_z" : "az",
                   "name_z_to_a" : "za",
                   "price_low_to_high" : "lohi",
                   "price_high_to_low" : "hilo"}

    INVENTORY_ITEM_PRICES_ALL = (By.CLASS_NAME, "inventory_item_price")
    INVENTORY_ITEM_NAMES_ALL = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver):
        self.driver = driver

    def get_cart_count(self) -> int:
        try:
            badge = self.find_element(self.CART_BADGE)
            return int(badge.text)
        except NoSuchElementException:
            return 0

    def is_card_badge_visible(self) -> bool:
        elements = self.find_elements(self.CART_BADGE)
        return elements[0].is_displayed() if elements else False

    def get_all_product_prices(self) -> list[float]:
        element_price = self.find_elements(self.INVENTORY_ITEM_PRICES_ALL)
        return [float(element.text.replace("$", "")) for element in element_price] # element.text for get DOM text

    def get_all_product_names(self) -> list[str]:
        element_price = self.find_elements(self.INVENTORY_ITEM_NAMES_ALL)
        return [str(element.text.replace("$", "")) for element in element_price]


