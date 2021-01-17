import React from 'react';
import 'materialize-css';
import { 
        Icon, Navbar, Button, Row, Col
    } from 'react-materialize';


import './style.css';
import estudante from '../../Assets/estudante.png'
import mockup1 from '../../Assets/mockup1.png'
import mockup2 from '../../Assets/mockup2.png'
import mockup3 from '../../Assets/mockup3.png'
import mockup4 from '../../Assets/mockup4.png'


const landingPage = () => {
    return (
        <>  
            <Navbar
                alignLinks="right"
                brand={<a id='logo' className="brand-logo" href="/">abraba></a>}
                centerChildren
                id="mobile-nav"
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
                    Comece agora
                </Button>
                <a><Icon class="material-icons large">menu</Icon></a>
            </Navbar>
            <div id='main'>
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
                                        Comece agora
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
                <div id='container_inclusao'>
                    <div className='container'>
                        <Row>
                            <Col l={10} offset={'l1'}>
                                <div id='container_texto_inclusao'>
                                    <span id='text_container_inclusao'>Veja como a<span id='logo_text_white'>&ensp;abraba>&ensp;</span>promove a sua inclusão:</span>
                                </div>
                            </Col>
                        </Row>
                        <Row>
                            <Col l={12}>
                                <div id='container_mockups_inclusao'>
                                    <div id='card_mockup'>
                                        <img src={mockup1}></img>
                                        <p id='p_small_bold'>Cadastro Fácil</p>
                                        <p id='text_helper'>E seu currículo fica <br/> pronto em um instante</p>
                                        <Button>Saiba mais</Button>
                                    </div>
                                    <div id='card_mockup'>
                                        <img src={mockup2}></img>
                                        <p id='p_small_bold'>Match de <br/>Habilidades!</p>
                                        <p id='text_helper'>Você nos conta sobre <br/> suas habilidades e nós <br/> procuramos a vaga <br/> perfeita pra você</p>
                                        <Button>Saiba Mais</Button>
                                    </div>
                                    <div id='card_mockup'>
                                        <img src={mockup3}></img>
                                        <p id='p_small_bold'>Capacitação</p>
                                        <p id='text_helper'>Cursos gratuitos recomendados pra você ser o profissional que as empresas estão buscando</p>
                                        <Button>Saiba Mais</Button>
                                    </div>
                                    <div id='card_mockup'>
                                        <img src={mockup4}></img>
                                        <p id='p_small_bold'>Mentorias</p>
                                        <p id='text_helper'>Saiba como sua empresa pode se beneficiar ao incentivar a capacitação do jovem aprendiz!</p>
                                        <Button>Saiba Mais</Button>
                                    </div>
                                </div>
                            </Col>
                        </Row>
                    </div>
                </div>
            </div>
        </>
    )
}


export default landingPage; 