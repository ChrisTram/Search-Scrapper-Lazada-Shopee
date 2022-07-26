import React, { Component } from 'react';
import { Table } from 'react-bootstrap';
import { AddProdModal } from './AddProductModal';
import { EditProdModal } from './EditProductModal';

import { Button, ButtonToolbar } from 'react-bootstrap';
import { createSearchParams } from 'react-router-dom';
import Chart from 'chart.js/auto';


export class Products extends Component {

    constructor(props) {
        super(props);
        this.state = { products: [], addProdShow: false, editProdShow: false }
        this.chartRef = React.createRef();


    }

    refreshList() {
        fetch(process.env.REACT_APP_API + 'products')
            .then(response => response.json())
            .then(data => {
                this.setState({ products: data });
            });
    }

    createChar() {
        const labels = [
            'January',
            'February',
            'March',
            'April',
            'May',
            'June',
          ];
        
          const data = {
            labels: labels,
            datasets: [{
              label: 'My First dataset',
              backgroundColor: 'rgb(255, 99, 132)',
              borderColor: 'rgb(255, 99, 132)',
              data: [0, 10, 5, 2, 20, 30, 45],
            }]
          };
        
          const config = {
            type: 'line',
            data: data,
            options: {}
          };
        
          const ctx = this.chartRef.current.getContext('2d');        

          if(this.myChart != null) this.myChart.destroy()

        this.myChart = new Chart(
            ctx,
            config
          );
    }

    componentDidMount() {
        this.createChar()
        
        this.refreshList();
    }

    componentDidUpdate() {
        //this.refreshList();
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
        this.refreshList();
    }

    render() {
        const { products, prodid, prodname, prodbrand } = this.state;
        let addModalClose = () => {this.setState({ addModalShow: false }); this.refreshList()};
        let editModalClose = () => {this.setState({ editModalShow: false }); this.refreshList()};
        

        return (
            <div>
                <canvas ref={this.chartRef}/>

                <Table className="mt-4" striped bordered hover size="sm">
                    <thead>
                        <tr>
                            <th>Product Name</th>
                            <th>Product Brand</th>
                            <th>Website</th>
                            <th>Option</th>
                        </tr>
                    </thead>
                    <tbody>
                        {products.map(prod =>
                            <tr key={prod.productID}>
                                <td>{prod.ProductName}</td>
                                <td>{prod.ProductBrand}</td>
                                <td>{prod.ProductWeb}</td>
                                <td>
                                    <ButtonToolbar>
                                        <Button className="mr-2" variant="info"
                                            onClick={() => this.setState({
                                                editModalShow: true,
                                                prodid: prod.ProductID, prodname: prod.ProductName, prodbrand: prod.ProductBrand
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
                                                prodbrand={prodbrand} />
                                        }
                                    </ButtonToolbar>

                                </td>

                            </tr>)}
                    </tbody>

                </Table>
                <ButtonToolbar>
                    <Button variant='primary'
                        onClick={() => this.setState({ addModalShow: true })}>
                        Add Product</Button>

                    <AddProdModal show={this.state.addModalShow}
                        onHide={addModalClose} />
                </ButtonToolbar>
            </div>
        )
    }
}