import products from './products';

describe('products', () => {

    it('should return a list of products', () => {
        const list = products();

        expect(list).toHaveLength(3);
    });

});
