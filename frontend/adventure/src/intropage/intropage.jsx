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
            <Row className='animate-row row-1'>
                <Col className='rolling'>
                In the mythical land of
                </Col>
            </Row>
            <Row className='animate-row row-2'>
                <Col md={{span: 3, offset: 5}}>
                <h1 className="boldonse-regular">AMERICA</h1>
                </Col>
            </Row>
            <Row className='rolling animate-row row-3'>
                <Col md={{span: 3, offset: 11}}>
                Welcome to...
                </Col>
            </Row>
        </Container>
        </>
    );
}

export default IntroPage;