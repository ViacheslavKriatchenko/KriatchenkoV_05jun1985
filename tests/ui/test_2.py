from ui.main_page import MainPage


def test_add_item_to_cart(driver):

    main = MainPage(driver)

    main.open_the_page()
    main.click_on_catalog()
    main.click_on_DHL()
    added_item = main.add_item_to_cart()
    # print(added_item)
    cart_item = main.added_to_cart()
    # print(cart_item)
    assert added_item == cart_item
    main.click_button_element()
    main.delete_items_in_cart()
    cart_item = main.added_to_cart()
    assert cart_item == 0
