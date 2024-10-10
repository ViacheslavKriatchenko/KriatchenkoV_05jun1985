from ui.main_page import MainPage
from ui.cart_page import CartPage
from time import sleep


def test_add_item_to_cart(driver):

    main = MainPage(driver)
    cart = CartPage(driver)

    main.open_the_page()
    main.click_on_catalog()
    main.click_on_DHL()
    added_item = main.add_item_to_cart()
    # print(added_item)
    cart_item = main.added_to_cart()
    # print(cart_item)
    assert added_item == cart_item
    cart.open_the_page()
    total = cart.basket()
    assert total is not None
    cart.delete_items_in_cart()
    sleep(2)
    total = int(cart.basket().split()[0])
    assert total == 0
