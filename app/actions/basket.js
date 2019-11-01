export const BASKET_LOADING = 'BASKET_LOADING';
export const BASKET_LOADED = 'BASKET_LOADED';
export const BASKET_ADD_ITEM = 'BASKET_ADD_ITEM';
export const BASKET_GET_ITEMS = 'BASKET_GET_ITEMS';
export const BASKET_INCREMENT = 'BASKET_INCREMENT';



export function loadBasket() {
    return async (dispatch, _, config) => {
        dispatch({ type: BASKET_LOADING });

        const response = await fetch(config.cartApi, { method: 'POST', body: JSON.stringify({}) });
        const basket = await response.json();

        dispatch({
            type: BASKET_LOADED,
            ...basket,
        })
    };
}

export function addToBasket (basketId, itemId) {
    return async (dispatch, _, config) => {
        
        let body =  {
            quantity:  1
        }

        let api = `${config.cartApi}/${basketId}/item/${itemId}`;

        const response = await fetch(api, { method: 'POST' , body: JSON.stringify(body) });
        const basket = await response.json();

        dispatch({
            type: BASKET_ADD_ITEM,
            ...basket
        })
    };   
}

export function getBasket (basketId) {
    return async (dispatch, _, config) => {
    
        let api = `${config.cartApi}/${basketId}`;

        const response = await fetch(api, { method: 'GET' });
        const basket = await response.json();

        dispatch({
            type: BASKET_GET_ITEMS,
            ...basket
        })
    };   
}

export function incrementQuantity (basketId) {
    return async (dispatch, _, config) => {
    
        let api = `${config.cartApi}/${basketId}/item/${itemId}/increment`;

        const response = await fetch(api, { method: 'POST', body: JSON.stringify(body) });
        const basket = await response.json();

        dispatch({
            type: BASKET_INCREMENT,
            ...basket
        })
    };   
}


