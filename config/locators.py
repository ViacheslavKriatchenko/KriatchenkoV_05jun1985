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
    CART_BUTTON = ('xpath', '//div[@class="header__basket js-basket-wrapper"]')
    DELETE_CART_BUTTON = ('xpath', '//button[@class="dropdown-close js-item-delete"]')
    PLACE_AN_ORDER = ('xpath', '//div[@class="dropdown-offer dropdown-padding"]')


class CartPageLocators:
    ALL_CART_ITEMS = (
        'xpath', '//div[@class="basket__item js-cart-item"]'
        )
