# Fast Food Fast
Fast Food Fast is a food delivery service app for a restaurant.

## Badges
### Travis badge
[![Build Status](https://travis-ci.org/lindseyme/Fast-Food-Fast.svg?branch=ft-challenge-three)](https://travis-ci.org/lindseyme/Fast-Food-Fast)
### Code climate
[![Maintainability](https://api.codeclimate.com/v1/badges/d394577ec343cf74808c/maintainability)](https://codeclimate.com/github/lindseyme/Fast-Food-Fast/maintainability)
coveralls
[![Coverage Status](https://coveralls.io/repos/github/lindseyme/Fast-Food-Fast/badge.svg?branch=api_ci)](https://coveralls.io/github/lindseyme/Fast-Food-Fast?branch=api_ci)
## Functionality
- Create user accounts that can signin/signout from the app.
- Place an order for food.
- Get list of orders.
- Get a specific order.
- Update the status of an order.
- Get the menu.
- Add food option to the menu.
- View the order history for a particular user.

## Api end points
| Method  | Endpoint          | Description                      |
| --------|:-----------------:| --------------------------------:|
| POST     | auth/signup      | Register a user                  |
| POST     | auth/login       | Login a user                     | 
| POST     | users/orders     | Place an order for food.         |
| GET      | users/orders     | Get the order history for a particular user.|
| GET      | /orders/         | Get all orders                   |
| GET      |/orders/<orderId> | Fetch a specific order by an admin |
| PUT      |/orders /<orderId>| Update the status of an order by an admin |
| GET      | /menu            | Get available menu               |
| POST     | /menu            | Add a meal option to the menu. |

## Prerequisites
- Set up the postgresql database.
- Configure the database name, password and portnumber.

## installed packages
- Python 3.4.4

- Install necessary requirements

  ```
  $ pip install -r requirements.txt
  ```

- Run development server
  ```
  $ python runserver.py
  ```

This site should now be running at http://localhost:5000

### Run Tests

- Make sure pytest is installed

  ```
  $pip install -U pytest
  ```
  
- Run the test by

  ```
  $ pytest
  ```
