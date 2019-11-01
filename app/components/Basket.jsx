import React, { Component } from 'react';
import { connect } from 'react-redux'

import * as basketActions from '../actions/basket';

export class Basket extends Component {

    render() {

        const { products, basket, title, getBasket, userItems } = this.props;

        const isBasketPopulated  = (basket) => {
            return Object.keys(basket.items).length;
        }

        const extractBasketItems = (basket) => {
            const result = Object.values(basket.items).map(({ itemId, quantity }) => ({ itemId, quantity }));

            return result;
        }

        return (
            <div className="mr-4">
                {
                    (isBasketPopulated(basket) > 0) ?
                        <div className='basket'> 
                            <h3>{ title }</h3>
                            <ul className="list-group">
                                { extractBasketItems(basket).map(item => {
                                        return <li key={item.itemId} className="list-group-item d-flex justify-content-between align-items-center">
                                            Item: { item.itemId }
                                            <span className="badge badge-primary badge-pill">{ item.quantity}</span>
                                        </li>
                                }) }
                            </ul>
                        </div> :
                        <div className="alert alert-primary" role="alert">
                            <p>Please add item to basket</p>
                        </div>
                }
            </div>
        )
    }

}

export function mapStateToProps({ basket, products }) {
    return {
        products,
        basket
    }
}

export default connect(mapStateToProps, basketActions)(Basket);
