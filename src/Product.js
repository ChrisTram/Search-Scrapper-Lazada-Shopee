import React, { Component } from 'react';
import { Table } from 'react-bootstrap';
import { AddProdModal } from './AddProductModal';
import { EditProdModal } from './EditProductModal';
import Form from 'react-bootstrap/Form';
import { Button, ButtonToolbar } from 'react-bootstrap';
import { createSearchParams } from 'react-router-dom';
import Chart from 'chart.js/auto';


export class Products extends Component {

    constructor(props) {
        super(props);
        this.state = { products: [], addProdShow: false, editProdShow: false }
        this.chartRef = React.createRef();
        [this.dataShopee, this.dataLazada, this.brands] = [[], [], []];
        this.search = "";
    }

    refreshList() {
        fetch('apiproducts')
            .then(response => response.json())
            .then(data => {
                this.setState({ products: data });
                [this.dataShopee, this.dataLazada, this.brands] = this.createData(data);
                this.createChar(this.dataShopee, this.dataLazada, this.brands);
            });
    }

    createData(data) { //Can be easily extend to support several shops, just did the most straightforward method
        var productsShopee = [], productsLazada = [];
        var dataShopee = [], dataLazada = [];
        var brands = [];
        console.log("create data")
        data.forEach(prod => {
            if (prod.ProductWeb == "Shopee") {
                productsShopee.push(prod);
            } else if (prod.ProductWeb == "Lazada") {
                productsLazada.push(prod);
            } else { } //Parasit data
            if (!brands.includes(prod.ProductBrand)) {
                brands.push(prod.ProductBrand)
            }
        });
        var n = productsShopee.length + productsLazada.length; //To be sure no parasit data 
        console.log(n)
        brands.forEach(brand => {
            dataShopee.push((Math.round(((productsShopee.filter(({ ProductBrand }) => ProductBrand === brand).length) / n) * 100) * 100) / 100)
            dataLazada.push((Math.round(((productsLazada.filter(({ ProductBrand }) => ProductBrand === brand).length) / n) * 100) * 100) / 100)
        });
        return [dataShopee, dataLazada, brands];
    }

    handleSearch = event => {
        event.preventDefault();
        this.search = event.target.Search.value.toLowerCase();
        this.requestResearch();
    };

    requestResearch() {
        fetch('searchProducts/' + this.search)
        .then(response => response.json())
        .then(data => {
            this.setState({ products: data });
            [this.dataShopee, this.dataLazada, this.brands] = this.createData(data);
            this.createChar(this.dataShopee, this.dataLazada, this.brands);
        });
    }

    createChar(dataShopee, dataLazada, brands) {

        console.log("createChar")
        console.log(brands)
        const ctx = this.chartRef.current.getContext('2d');

        if (this.myChart != null) this.myChart.destroy()
        this.myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: brands,
                datasets: [{
                    label: '% Shopee',
                    data: dataShopee,
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                    ],
                    borderColor: [
                        'rgba(255, 99, 132, 1)',
                    ],
                    borderWidth: 1
                },
                {
                    label: '% Lazada',
                    data: dataLazada,
                    backgroundColor: [
                        'rgba(153, 102, 255, 0.2)',
                    ],
                    borderColor: [
                        'rgba(153, 102, 255, 1)',
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }

                }
            }
        })
    }

    componentDidMount() {
        this.refreshList();

    }

    componentDidUpdate() {
        //this.refreshList();

    }

    deleteProduct(id) {
        if (window.confirm('Are you sure?')) {
            fetch('product/' + id, {
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
        let addModalClose = () => { this.setState({ addModalShow: false }); this.refreshList() };
        let editModalClose = () => { this.setState({ editModalShow: false }); this.refreshList() };


        return (
            <div>
                <Form onSubmit={this.handleSearch}>
                    <Form.Group controlId="Search">
                        <Form.Label>Search Products (perfumes / clothes / smartphones). Any other request will be random.</Form.Label>
                        <Form.Control type="text" name="Search" required
                            placeholder="Search" />
                    </Form.Group>
                    <Button variant="outline-primary" type="submit">Search</Button>
                </Form>
                <canvas ref={this.chartRef} />
                <ButtonToolbar>
                    <Button variant='primary'
                        onClick={() => this.setState({ addModalShow: true })}>
                        Add Product</Button>

                    <AddProdModal show={this.state.addModalShow}
                        onHide={addModalClose} />
                </ButtonToolbar>
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
            </div>
        )
    }
}