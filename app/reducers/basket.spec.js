import * as actions from '../actions/basket';
import basketReducer from './basket';

describe('basketReducer', () => {

    it('should return an empty initial state', () => {
        expect(basketReducer(undefined, {})).toEqual({ items: {} });
    });


    it('should store basket id and cartItems when basket is loaded', () => {
        const action = {
            type: actions.BASKET_LOADED,
            cartId: 123,
            cartItems: {}
        };

        expect(basketReducer(undefined, action)).toEqual({
            id: 123,
            items: {},
        });
    });

});
