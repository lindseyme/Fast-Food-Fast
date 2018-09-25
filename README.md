# Fast Food Fast

Fast Food Fast is a food delivery service app for a restaurant.

## Badges
Travis Badge
[![Build Status](https://travis-ci.org/lindseyme/Fast-Food-Fast.svg?branch=api_ci)](https://travis-ci.org/lindseyme/Fast-Food-Fast)

Coveralls
[![Coverage Status](https://coveralls.io/repos/github/lindseyme/Fast-Food-Fast/badge.svg?branch=api_ci)](https://coveralls.io/github/lindseyme/Fast-Food-Fast?branch=api_ci)

Code Climate
[![Maintainability](https://api.codeclimate.com/v1/badges/d394577ec343cf74808c/maintainability)](https://codeclimate.com/github/lindseyme/Fast-Food-Fast/maintainability)

## APIs for Fast Food Fast
These are APIs to be used to interface the fuctionality of the Fast Food Fast application

## Functionality
- Placing order for food
- Obtaining a list of orders.
- Getting a specific order.
- Updating the order status.
 
These are the endpoints:

| Method  | Endpoint          | Description                      | Body                  |
| --------|:-----------------:| -------------------------------: |----------------------:|
| GET     | /api/v1/orders/   | Get all orders|                  |                       |
| GET     | /api/v1/orders/id | Get specific orders using an id  |                       |   
|POST     | /api/v1/orders    | Place a new orders               |order_list[], username |
|PUT      | /api/v1/orders/id | Update a specific orders status  | order_status          |

APIs are Hosted at https://fast-food-fast-api-v4.herokuapp.com

Sample get all orders https://fast-food-fast-api-v4.herokuapp.com/api/v1/orders/

## Setting Up for Development

These are instructions for setting up Fast Food Fast app in a development enivornment.

### Prerequisites

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
