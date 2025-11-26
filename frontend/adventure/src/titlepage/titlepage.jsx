import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import logo from '../assets/banner/logo.png';
import './titlepage.css';


// will change to the app itself
// function MyButton (){
//     const ClickButt
// }

function TitlePage({ onStart }){
    const handleClick = () => {
        console.log('Button clicked!');
        if (onStart) {
            onStart();
        }
    };

    return (
        <>
        <Container>
            <Row>
                <img src={logo} alt="banner" id='banner' />
            </Row>
            <Row style={{height: '375px'}}></Row>
            <Row>
                <Col md={{span: 3, offset: 5}}>
                <button onClick={handleClick} style={{cursor: 'pointer', zIndex: 1000}}>
                Start
                </button>
                </Col>
            </Row>
        </Container>
        </>
    )   
}

export default TitlePage;