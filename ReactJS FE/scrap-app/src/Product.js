import React, { Component } from 'react';
import { Table } from 'react-bootstrap';
import {AddProdModal} from './AddProductModal';
import {EditProdModal} from './EditProductModal';

import { Button, ButtonToolbar } from 'react-bootstrap';

export class Products extends Component {

    constructor(props) {
        super(props);
        this.state = { products: [], addProdShow:false, editProdShow:false }
    }

    refreshList() {
        fetch(process.env.REACT_APP_API + 'products')
            .then(response => response.json())
            .then(data => {
                this.setState({ products: data });
            });
    }

    componentDidMount() {
        this.refreshList();
    }

    componentDidUpdate() {
        this.refreshList();
    }

    deleteProduct(id) {
        if (window.confirm('Are you sure?')) {
            fetch(process.env.REACT_APP_API + 'product/' + id, {
                method: 'DELETE',
                header: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                }
            })
        }
    }

    render() {
        const { products, prodid, prodname, prodbrand } = this.state;
        let addModalClose=()=>this.setState({addModalShow:false});
        let editModalClose=()=>this.setState({editModalShow:false});
        return (
            <div>
                <Table className="mt-4" striped bordered hover size="sm">
                    <thead>
                        <tr>
                            <th>ProductID</th>
                            <th>ProductName</th>
                            <th>Options</th>
                        </tr>
                    </thead>
                    <tbody>
                        {products.map(prod =>
                            <tr key={prod.ProductID}>
                                <td>{prod.ProductName}</td>
                                <td>{prod.ProductBrand}</td>
                                <td>
                                    <ButtonToolbar>
                                        <Button className="mr-2" variant="info"
                                            onClick={() => this.setState({
                                                editModalShow: true,
                                                prodid: prod.ProductID, prodname: prod.ProductName, prodbrand:prod.ProductBrand
                                            })}>
                                            Edit
                                        </Button>

                                        <Button className="mr-2" variant="danger"
                                            onClick={() => this.deleteProduct(prod.ProductID)}>
                                            Delete
                                        </Button>
                                        {
                                        <EditProdModal show={this.state.editModalShow}
                                             onHide={editModalClose}
                                             prodid={prodid}
                                             prodname={prodname}
                                             prodbrand={prodbrand}/>  
                                        }
                                    </ButtonToolbar>

                                </td>

                            </tr>)}
                    </tbody>

                </Table>
                <ButtonToolbar>
                    <Button variant='primary'
                    onClick={()=>this.setState({addModalShow:true})}>
                    Add Product</Button>

                    <AddProdModal show={this.state.addModalShow}
                    onHide={addModalClose}/>
                </ButtonToolbar>
            </div>
        )
    }
}