from api.altavita_cart import Cart


def test_add_item_to_cart():
    response = Cart.add_item_to_cart(6930, 2)
    print(response.json(), end='\n')
    assert response.status_code == 200
    assert response.json()['new_quantity'] == 2
