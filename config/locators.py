class MainPageLocators:

    CATALOG = (
        'xpath', '//a[contains(@class, "header__menu-link")]'
        )
    DHL = (
        'xpath', '//a[contains(text(), "DHL")]'
        )
    ALL_BUY_BUTTONS = (
        'xpath', '//div[@class="product__buy"]'
        )  # 12
    CART_ITEM_NUMBER = ('xpath', '//div[@class="count-box"]//span')


class CartPageLocators:
    ALL_CART_ITEMS = (
        'xpath', '//div[@class="basket__item js-cart-item"]'
        )
