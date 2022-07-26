import React, { Component } from 'react';
import { Modal, Button, Row, Col, Form } from 'react-bootstrap';

export class AddProdModal extends Component {
    constructor(props) {
        super(props);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleSubmit(event) {
        event.preventDefault();
        fetch(process.env.REACT_APP_API + 'products/', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                ProductId: null,
                ProductName: event.target.ProductName.value,
                ProductBrand: event.target.ProductBrand.value,
                ProductWeb: event.target.ProductWeb.value
            })
        })
            .then(res => res.json())
            .then((result) => {
                alert(result);
            },
                (error) => {
                    alert('Failed');
                })
    }
    render() {
        return (
            <div className="container">

                <Modal
                    {...this.props}
                    size="lg"
                    aria-labelledby="contained-modal-title-vcenter"
                    centered
                >
                    <Modal.Header clooseButton>
                        <Modal.Title id="contained-modal-title-vcenter">
                            Add Product
                        </Modal.Title>
                    </Modal.Header>
                    <Modal.Body>

                        <Row>
                            <Col sm={6}>
                                <Form onSubmit={this.handleSubmit}>
                                    <Form.Group controlId="ProductName">
                                        <Form.Label>ProductName</Form.Label>
                                        <Form.Control type="text" name="ProductName" required
                                            placeholder="ProductName" />
                                    </Form.Group>
                                    <Form.Group controlId="ProductBrand">
                                        <Form.Label>ProductBrand</Form.Label>
                                        <Form.Control type="text" name="ProductBrand" required
                                            placeholder="ProductBrand" />
                                    </Form.Group>
                                    <Form.Group controlId="ProductWeb">
                                        <Form.Label>Website</Form.Label>
                                        <Form.Control type="text" name="ProductWeb" required
                                            placeholder="ProductWeb" />
                                    </Form.Group>

                                    <Form.Group>
                                        <Button variant="primary" type="submit">
                                            Add Product
                                        </Button>
                                    </Form.Group>
                                </Form>
                            </Col>
                        </Row>
                    </Modal.Body>

                    <Modal.Footer>
                        <Button variant="danger" onClick={this.props.onHide}>Close</Button>
                    </Modal.Footer>

                </Modal>

            </div>
        )
    }

}