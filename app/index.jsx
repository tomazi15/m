import React from 'react';
import {render} from 'react-dom';
import {Provider} from 'react-redux';

import BasketPage from './container/BasketPage';
import store from './store';

render(
    <Provider store={store}>
        <BasketPage />
    </Provider>,
    document.querySelector('.app')
);
