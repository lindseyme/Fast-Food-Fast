from update_the_order_status_api import APP
from update_the_order_status_api.urls import Urls

Urls.fetch_urls(APP)

if __name__ == '__main__':
    APP.run(debug=True)

