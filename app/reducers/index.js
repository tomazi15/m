import { combineReducers } from 'redux'
import basketReducer from './basket';
import productsReducer from './products';

const rootReducer = combineReducers({
    basket: basketReducer,
    products: productsReducer,
});

export default rootReducer;
