import React from 'react';
import 'materialize-css';
import { 
        Icon, Navbar, NavItem, Button, Row, Col
    } from 'react-materialize';
import './style.css';
import estudante from '../../Assets/estudante.png'

const landingPage = () => {
    return (
        <>  
            <Navbar
                alignLinks="right"
                brand={<a id='logo' className="brand-logo" href="/">abraba></a>}
                centerChildren
                id="mobile-nav"
                style ={{
                    marginBottom: '40px'
                }}
                className='grey darken-4'
                menuIcon={<Icon class="material-icons large">menu</Icon>}
                options={{
                    draggable: true,
                    edge: 'left',
                    inDuration: 250,
                    onCloseEnd: null,
                    onCloseStart: null,
                    onOpenEnd: null,
                    onOpenStart: null,
                    outDuration: 200,
                    preventScrolling: true
                }}>
                <Button
                    flat
                    node="button"
                    className='white-text'
                    style={{
                        marginRight: '5px'
                    }}
                    >
                    Login
                </Button>
                <Button
                    node="button"
                    id='button-header'
                    style={{
                        marginRight: '5px'
                    }}
                    >
                    Comece agora!
                </Button>
                <a><Icon class="material-icons large">menu</Icon></a>
            </Navbar>
            <div id='header_container'>
                <div className='container'>
                    <Row >
                        <Col l={10} offset={'l1'}>
                            <div>
                                <h3 id='h3_maincall'>Prepare-se, jovem aprendiz</h3>
                            </div>
                        </Col>
                    </Row>
                    <Row>
                        <Col l={8}>
                            <div id='header_subcall'>
                                <span id='h5_subcall'>Vamos te ajudar a lançar <span id='logo_text'>abraba></span> <br/> 
                                e conseguir seu primeiro emprego!</span>
                            </div>
                            <div id='header_subcall_2'>
                                <Button
                                    large
                                    node="a"
                                    id='button-header'
                                    waves="light"
                                    style={{
                                    marginLeft: '10%'
                                }}>
                                    COMECE AGORA!
                                </Button>
                                <small id='header_saiba_como' className='white-text'>Saiba Como</small>
                            </div>
                        </Col>
                        <Col l={4}>
                            <div id='header_foto_div'>
                                <img src={estudante} alt='estudante_dab' id='foto_subcall'></img>
                            </div>
                        </Col>
                    </Row>
                </div>
            </div>
        </>
    )
}


export default landingPage; 