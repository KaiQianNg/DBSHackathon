import React from "react";
import { Link } from "react-router-dom";
import {Col, Row, FloatingLabel, Form, Button, Container} from "react-bootstrap"

const Login = () => {

    return(
        <>
            <Container>
                <Row>
                    <h1><b>Add Courses Here</b></h1>
                    <Form>
                        <FloatingLabel
                                    controlId="floatingInput"
                                    label="Email"
                                    className="mb-3"
                                    style={{
                                        float:'left',
                                        marginRight:'10px'
                                    }}>
                            <Form.Control
                                        type="email"
                                        name="email"
                                        placeholder="Email"
                                        style={{
                                            marginLeft: '10px',
                                            float: 'right'
                                        }}
                                    />
                        </FloatingLabel>
                        <FloatingLabel
                                    controlId="floatingInput"
                                    label="Password"
                                    className="mb-3"
                                    style={{
                                        float:'left'
                                    }}>
                            <Form.Control
                                        type="password"
                                        name="password"
                                        placeholder="Password"
                                        style={{
                                            marginLeft: '10px',
                                            float: 'right'
                                        }}
                                    />
                        </FloatingLabel>
                        <br></br>
                        <Button variant="primary" type="submit" style={{marginBottom: '30px'}}>
                            Submit
                        </Button>
                    </Form>
                </Row>
            </Container>
        </>
    )

}

export default Login;