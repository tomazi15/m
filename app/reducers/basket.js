import { BASKET_LOADED, BASKET_ADD_ITEM, BASKET_GET_ITEMS, BASKET_INCREMENT } from '../actions/basket';

function basketReducer(state={ items: {} }, action) {

    switch(action.type) {
        case BASKET_LOADED:
            return {
                ...state, 
                id: action.cartId,
                items: action.cartItems,
            }
        case BASKET_ADD_ITEM: 
            return {
                ...state,
                id: action.cartId,
                items: action.cartItems,
            }
        case BASKET_GET_ITEMS:
            return {
                ...state,
                id: action.cartId,
                items: action.cartItems,
            }
        case BASKET_INCREMENT:
            return {
                ...state,
                id: action.cartId,
                items: action.cartItems,
            }            
        default:
            return state;
    }

}

export default basketReducer;
BASKET_INCREMENT