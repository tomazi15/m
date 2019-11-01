# Frontend Coding test
Shopping cart component that allows a user to manage their basket

## Getting started

The app is dockerised, run `docker-compose up --build` to bring up the application. This will spin up the backend api and start the front end application on http://localhost:3000. It uses webpack devserver and supports hot reloading to make development as easy as possible.

The backend api will be running at `http://localhost:4567`

## Running the test suite

Run the test suite:
```sh
docker exec -it shopping-basket_app_1 npm test
```

Run test suite and generate coverage report:
```sh
docker exec -it shopping-basket_app_1 npm run coverage
```

## Api Documentation

The following api endpoints are available:

##### Create a new cart
- Method: POST
- Path: `/cart`
- Response Body:

```JSON
    {
        "cartId": 1,
        "cartItems": {}
    }
```


##### Get an existing cart:
- Method: POST
- Path: `/cart/<int:cart_id>`
- Response Body:

```JSON
    {
        "cartId": 1,
        "cartItems": {
          "1": {
            "itemId": 1,
            "quantity": 1
          }
        }
    }
```


##### Clear a cart
- Method: POST
- Path: `/cart/<int:cart_id>/clear`
- Responds with 204 No Content and an empty body


##### Add an item to a cart:
- Method: POST
- Path: `/cart/<int:cart_id>/item/<int:item_id>`
- Request Body:

```JSON
    {
      "quantity": 1
    }
```

- Response Body:

```JSON
    {
        "cartId": 1,
        "cartItems": {
          "1": {
            "itemId": 1,
            "quantity": 1
          }
        }
    }
```

##### Increment quantity of item in a cart:
- Method: POST
- Path: `cart/<int:cart_id>/item/<int:item_id>/increment`
- Response Body:

```JSON
    {
        "cartId": 1,
        "cartItems": {
          "1": {
            "itemId": 1,
            "quantity": 2
          }
        }
    }
```

##### Decrement quantity of item in a cart:
- Method: POST
- Path: `/cart/<int:cart_id>/item/<int:item_id>/decrement`
- Response Body:

```JSON
    {
        "cartId": 1,
        "cartItems": {
          "1": {
            "itemId": 1,
            "quantity": 1
          }
        }
    }
```

##### Delete an item from a cart:
- Method: DELETE
- Path: `/cart/<int:cart_id>/item/<int:item_id>`
- Responds with 204 No Content and an empty body
