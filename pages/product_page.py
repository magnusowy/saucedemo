from selenium.webdriver.common.by import By
from pages.base_page import basePage

class productPage(basePage):
    DETAIL_IMAGE = (By.CLASS_NAME, "inventory_details_img")

    def get_product_image_src(self) -> str:
        return self.get_image_src(self.DETAIL_IMAGE)