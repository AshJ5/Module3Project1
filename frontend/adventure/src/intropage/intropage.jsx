// this page is to generate the intro leading into the main page opening
import React from 'react';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import './intropage.css'; 

function IntroPage({ onAnimationComplete }) {
    const handleAnimationEnd = (e) => {
        // Only trigger on the last animation (row-3)
        if (e.target.classList.contains('row-3')) {
            onAnimationComplete();
        }
    };

    return (
        <>
        <div id= 'wrap'>
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
            <Row 
                className='rolling animate-row row-3'
                onAnimationEnd={handleAnimationEnd}
            >
                <Col md={{span: 3, offset: 9}}>
                Welcome to...
                </Col>
            </Row>
        </Container>
        </div>
        </>
    );
}

export default IntroPage;