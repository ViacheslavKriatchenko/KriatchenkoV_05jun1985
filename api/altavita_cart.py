import requests


class Cart():

    def get_cart_info():
        response = requests.post(url="",
                                json="",
                                )

        if response.status_code == 200:
                return response.json()
        else:
            raise Exception(
                f"API request failed with status code {response.status_code}"
                )