import React from 'react';

const ProductList = ({ products, basket, addToBasket }) => (
    <div className="mr-4">
        <h2>Products</h2>
        <ul className="list-group">
            {
                
                products.map(product =>{
                    return (
                        <li className="list-group-item d-flex justify-content-between" key={product.name}>
                            <span>{product.name}</span>
                            <button className="btn btn-outline-primary btn-sm" type="button" onClick={() => addToBasket(basket.id, product.id)}>Add</button>
                        </li>
                    )
                }) 
            }
        </ul>
    </div>
);

export default ProductList;
