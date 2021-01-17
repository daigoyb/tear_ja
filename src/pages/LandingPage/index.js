import React from 'react';
import 'materialize-css';
import { 
        Button, Card, Row, Col, Navbar, Container, NavItem
    } from 'react-materialize';
import firstPagebg from '../../Assets/Mask.png';

const landingPage = () => {
    return (
        <>  
            <Navbar>
                <Col>
                    <NavItem>Icon</NavItem>
                </Col>
                <Col>
                    <NavItem>Fale Conosco</NavItem>
                </Col>
            </Navbar>
            <Row>
                <Container style={pageStyle.initContainer}>
                    
                </Container>
            </Row>
        </>
    )
}

var sectionStyle = {
    backgroundImage: `url(${firstPagebg})`,
    backgroundSize: 'cover',
    backgroundPosition: 'fixed'
};

const pageStyle = {
    initContainer:{
        position: 'absolute',
        height: '564px',
        left: '0%',
        right: '0%',
        top: '64px',
        color: '#00695C'
    },
    navBarStyle:{
        position: 'absolute',
        width: '1440px',
        height: '64px',
        left: '0px',
        top: '0px',
    }
}
export default landingPage; 