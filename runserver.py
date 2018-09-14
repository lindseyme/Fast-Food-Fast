from fetch_a_specific_order_api import APP
from fetch_a_specific_order_api.urls import Urls

Urls.fetch_urls(APP)

if __name__ == '__main__':
    APP.run(debug=True)

