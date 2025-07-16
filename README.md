<h1>Demo</h1>

<h2>I would like to present my approach to UI testing. I didn't create full 
test coverage but only give an example.</h2>

I used https://www.saucedemo.com to showcase my testing approach."
Tested with chromedriver. To use it add into path /drivers/chromedriver/chromedriver

I saw some html multiple problems like:
//div[@class="inventory_item_name " - problem with white character
<div class="inventory_item_desc"> ... </div> - problem with naming
add-to-cart-test.allthethings()-t-shirt-(red) 
problems with name and descriptions in elements. 
problem with possibility to order nothing etc. etc.

I added some examples makros like

usage: 
pytest -c pytest.ini -s tests/
or
pytest -c pytest.ini -s tests/test_inventory.py
or
pytest -c pytest.ini -m image -s tests/test_inventory.py