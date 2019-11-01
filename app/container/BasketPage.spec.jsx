import React from 'react';
import { shallow } from 'enzyme';

import { BasketPage, mapStateToProps } from './BasketPage';

describe('<BasketPage />', () => {

    const basket = [];
    const products = [];

    it('should start loading the basket when the basketpage gets created', () => {
        // Given
        const loadBasket = jest.fn();

        // When
        const props = { basket, products, loadBasket };
        const render = shallow(<BasketPage {...props} />);

        // Then
        expect(loadBasket).toHaveBeenCalled();
    });

    it('should display a loading message when loading the basket', () => {
        // Given
        const loadBasket = jest.fn();
        const isLoading = true;

        // When
        const props = { basket, products, isLoading, loadBasket };
        const render = shallow(<BasketPage {...props} />);

        // Then
        expect(render.find('div').text()).toContain('Loading your basket');
    });

});
