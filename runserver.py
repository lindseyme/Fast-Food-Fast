from api import APP
from api.urls import Urls

Urls.fetch_urls(APP)

if __name__ == '__main__':
    APP.run(debug=True)

