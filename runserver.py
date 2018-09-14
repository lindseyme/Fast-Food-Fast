from get_list_of_orders_api import APP
from get_list_of_orders_api.urls import Urls

Urls.fetch_urls(APP)

if __name__ == '__main__':
    APP.run(debug=True)

