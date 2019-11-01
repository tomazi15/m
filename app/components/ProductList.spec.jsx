import React from 'react';
import { shallow } from 'enzyme';

import ProductList from './ProductList';

describe('<ProductList />', () => {

    it('should render a list of products', () => {
        // Given
        const products = [
            { id: 1, name: 'A' },
            { id: 2, name: 'B' }
        ];

        const addToBasket = jest.fn();

        // When
        const render = shallow(<ProductList products={products} addToBasket={addToBasket} />);
        const listItems = render.find('li');
        
        // Then
        expect(listItems).toHaveLength(2);
        expect(listItems.first().find('span').text()).toContain('A');
        expect(listItems.at(1).find('span').text()).toContain('B');
    });

    it('should trigger addToBasket with the right productId', () => {
        // Given
        const products = [
            { id: 1, name: 'A' },
            { id: 2, name: 'B' }
        ];

        const addToBasket = jest.fn();

        // When
        const render = shallow(<ProductList products={products} addToBasket={addToBasket} />);
        render.find('button').first().simulate('click');

        // Then
        expect(addToBasket).toHaveBeenCalledWith(products[0].id);
    });

});
