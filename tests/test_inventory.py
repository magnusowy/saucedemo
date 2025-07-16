import pytest
from pages.inventory_page import inventoryPage

def test_add_and_remove_one_element_to_buy(driver, session_user_login, inventory_page):

    inventory_page.click_on_element(inventoryPage.ADD_BACKPACK_TO_CARD_BUTTON)
    inventory_page.wait_for_element(inventoryPage.REMOVE_BACKPACK_FROM_CARD_BUTTON)
    assert inventory_page.get_cart_count() == 1, f'Card badge count is wrong !=1'
    inventory_page.click_on_element(inventoryPage.REMOVE_BACKPACK_FROM_CARD_BUTTON)
    assert not inventory_page.is_card_badge_visible(), f'Card badge count is still visible'

### Extend with add two, three, etc. if needed

def test_add_and_remove_all_elements_to_buy(driver, session_user_login, inventory_page):
    inventory_page.click_on_element(inventoryPage.ADD_BACKPACK_TO_CARD_BUTTON)
    inventory_page.click_on_element(inventoryPage.ADD_BIKE_LIGHT_TO_CARD_BUTTON)
    inventory_page.click_on_element(inventoryPage.ADD_TSHIRT_TO_CARD_BUTTON)
    inventory_page.click_on_element(inventoryPage.ADD_FLEECE_JACKET_TO_CARD_BUTTON)
    inventory_page.click_on_element(inventoryPage.ADD_ONESIE_TO_CARD_BUTTON)
    inventory_page.click_on_element(inventoryPage.ADD_RED_TSHIRT_TO_CARD_BUTTON)
    inventory_page.wait_for_element(inventoryPage.REMOVE_BACKPACK_FROM_CARD_BUTTON)

    assert inventory_page.get_cart_count() == 6, f'Card badge count is wrong !=6'

    inventory_page.click_on_element(inventoryPage.REMOVE_BACKPACK_FROM_CARD_BUTTON)
    inventory_page.click_on_element(inventoryPage.REMOVE_BIKE_LIGHT_FROM_CARD_BUTTON)
    inventory_page.click_on_element(inventoryPage.REMOVE_TSHIRT_FROM_CARD_BUTTON)
    inventory_page.click_on_element(inventoryPage.REMOVE_FLEECE_JACKET_FROM_CARD_BUTTON)
    inventory_page.click_on_element(inventoryPage.REMOVE_ONESIE_FROM_CARD_BUTTON)
    inventory_page.click_on_element(inventoryPage.REMOVE_RED_TSHIRT_FROM_CARD_BUTTON)

    assert not inventory_page.is_card_badge_visible(), f'Card badge is visible after removing elements'


@pytest.mark.sorting
def test_sort_by_price_a_to_z(driver, session_user_login, inventory_page):
    inventory_page.choose_from_select(inventoryPage.SORT_DROPDOWN, inventory_page.SORT_VALUES["name_a_to_z"])
    list_of_names = inventory_page.get_all_product_names()
    assert list_of_names == sorted(list_of_names), f'Names are not sorted from alphabetic way'


@pytest.mark.sorting
def test_sort_by_price_z_to_a(driver, session_user_login, inventory_page):
    inventory_page.choose_from_select(inventoryPage.SORT_DROPDOWN, inventory_page.SORT_VALUES["name_z_to_a"])
    list_of_names = inventory_page.get_all_product_names()
    assert list_of_names == sorted(list_of_names, reverse=True), f'Names are not sorted from reversed alphabetic way'


@pytest.mark.sorting
def test_sort_by_price_high_to_low(driver, session_user_login, inventory_page):
    inventory_page.choose_from_select(inventoryPage.SORT_DROPDOWN, inventory_page.SORT_VALUES["price_high_to_low"])
    list_of_prices = inventory_page.get_all_product_prices()
    assert list_of_prices == sorted(list_of_prices, reverse=True), f'Prices are not sorted from high to low'


@pytest.mark.sorting
def test_sort_by_price_low_to_high(driver, session_user_login, inventory_page):
    inventory_page.choose_from_select(inventoryPage.SORT_DROPDOWN, inventory_page.SORT_VALUES["price_low_to_high"])
    list_of_prices = inventory_page.get_all_product_prices()
    assert list_of_prices == sorted(list_of_prices), f'Prices are not sorted from low to high'


@pytest.mark.image
def test_check_proper_img_for_backpack(driver, session_user_login, inventory_page, product_page):
    main_page_img_source = inventory_page.get_image_src(inventory_page.SAUCE_LABS_BACKPACK_IMG)
    inventory_page.click_on_element(inventory_page.SAUCE_LABS_BACKPACK_TITLE)
    detail_src_img_source = product_page.get_product_image_src()
    assert main_page_img_source == detail_src_img_source, f"The images are different {main_page_img_source} and {detail_src_img_source}"