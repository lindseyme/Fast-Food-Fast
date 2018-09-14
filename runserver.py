from place_a_new_order_for_food_api import APP
from place_a_new_order_for_food_api.urls import Urls

Urls.fetch_urls(APP)

if __name__ == '__main__':
    APP.run(debug=True)

