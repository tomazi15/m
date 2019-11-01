# Python Backend Coding Test

Cart Service that provides a selection of endpoints for interacting with a shopping cart.

### Endpoints


##### Service Healthcheck:
- Method: GET
- Path: `/health`
- Response Body:

```JSON
    {
        "healthy": true
    }
```


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

##### Add multiple items to a cart:
- Method: POST
- Path: `/cart/<int:cart_id>/items`
- Request Body:

```JSON
    [
        {
          "item_id": 2, 
          "quantity": 1
        },
        {
          "item_id": 3, 
          "quantity": 4
        }
    ]
```

- Success response Body:

```JSON
    {
        "cartId": 1,
        "cartItems": {
          "2": {
            "itemId": 2,
            "quantity": 1
          },
          "3": {
            "itemId": 3,
            "quantity": 4
          }
        }
    }
```
- Error response Body:
```JSON
    [
      { 
        "index": 2, 
        "error": "Missing item ID"
      }
    ]
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


### Running

The service is dockerised, run `docker-compose up` to bring up the service on http://localhost:4567
