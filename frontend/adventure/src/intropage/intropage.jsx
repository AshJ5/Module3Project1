// this page is to generate the intro leading into the main page opening
import React from 'react';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import './intropage.css'; 

function IntroPage() {
    return (
        <>
        <Container>
            <Row>
                <Col md={4} className="offset-md-4">
                In the mythical land of
                </Col>
            </Row>
            <Row>
                <Col>
                AMERICA
                </Col>
            </Row>
            <Row>
                <Col>
                Welcome to...
                </Col>
            </Row>
        {/* <p>In the mythical land of</p>
        <h1>AMERICA</h1>
        <p>Welcome to...</p> */}
        </Container>
        </>
    );
}

export default IntroPage;