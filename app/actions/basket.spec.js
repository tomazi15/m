import configureMockStore from 'redux-mock-store';
import thunk from 'redux-thunk';
import fetchMock from 'fetch-mock';
import * as actions from './basket';


const config = { 'cartApi': '/cart' };
const middlewares = [thunk.withExtraArgument(config)];
const mockStore = configureMockStore(middlewares);

describe('basket actions', () => {

    describe('loadBasket', () => {

        afterEach(() => {
            fetchMock.reset()
            fetchMock.restore()
        });

        it('creates a basket when BASKET_LOADED is dispatched', async () => {
            // Given
            fetchMock.postOnce('/cart', { body: { cartId: '', items: []}});

            // When
            const store = mockStore({});
            await store.dispatch(actions.loadBasket());

            // Then
            expect(store.getActions()).toEqual([
                { type: actions.BASKET_LOADING },
                { type: actions.BASKET_LOADED, cartId: '', items: [] },
            ]);
        });

    });

});
