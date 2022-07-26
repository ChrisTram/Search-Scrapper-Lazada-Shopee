import React,{Component} from 'react';
import {Modal,Button, Row, Col, Form} from 'react-bootstrap';

export class EditProdModal extends Component{
    constructor(props){
        super(props);
        this.handleSubmit=this.handleSubmit.bind(this);
    }

    handleSubmit(event){
        event.preventDefault();
        fetch(process.env.REACT_APP_API+'products/',{
            method:'PUT',
            headers:{
                'Accept':'application/json',
                'Content-Type':'application/json'
            },
            body:JSON.stringify({
                ProductID:event.target.ProductId.value,
                ProductName:event.target.ProductName.value,
                ProductBrand:event.target.ProductBrand.value
            })
        })
        .then(res=>res.json())
        .then((result)=>{
            alert(result);
        },
        (error)=>{
            alert('Failed');
        })
    }
    render(){
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
            Edit Product
        </Modal.Title>
    </Modal.Header>
    <Modal.Body>

        <Row>
            <Col sm={6}>
                <Form onSubmit={this.handleSubmit}>
                <Form.Group controlId="ProductId">
                        <Form.Label>ProductId</Form.Label>
                        <Form.Control type="text" name="ProductId" required
                        disabled
                        defaultValue={this.props.prodid} 
                        placeholder="ProductName"/>
                    </Form.Group>

                    <Form.Group controlId="ProductName">
                        <Form.Label>ProductName</Form.Label>
                        <Form.Control type="text" name="ProductName" required 
                        defaultValue={this.props.prodname}
                        placeholder="ProductName"/>
                    </Form.Group>
                    
                    <Form.Group controlId="ProductBrand">
                        <Form.Label>ProductBrand</Form.Label>
                        <Form.Control type="text" name="ProductBrand" required 
                        defaultValue={this.props.prodbrand}
                        placeholder="ProductBrand"/>
                    </Form.Group>

                    <Form.Group>
                        <Button variant="primary" type="submit">
                            Update Product
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