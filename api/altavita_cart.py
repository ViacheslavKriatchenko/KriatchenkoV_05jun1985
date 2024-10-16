import requests


class Cart:

    def add_item_to_cart(prod_id: int, count: int):
        # prod_id = 6930

        URL = "https://altaivita.ru/engine/cart/add_products_to_cart_from_preview.php"
        data = {
            "product_id": prod_id,
            "LANG_key": "ru",
            "S_wh": 1,
            "S_CID": "972abbabc3cb4b74ce5a3a00b1199588",
            "S_cur_code": "usd",
            "S_koef": 0.01273,
            "quantity": count,
            "S_hint_code": "eur",
            "S_customerID": ""
        }

        response = requests.post(
            url=URL,
            data=data,
            headers={
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8"
            }
        )

        if response.status_code == 200:
            return response
        else:
            raise Exception(
                f"API request failed with status code {response.status_code}"
            )
