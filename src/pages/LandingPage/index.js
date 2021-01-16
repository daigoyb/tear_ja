import React from 'react';

import './style.css';
import firstPagebg from '../../Assets/Mask.png';

var sectionStyle = {
    backgroundImage: `url(${firstPagebg})`,
    backgroundSize: 'cover',
    backgroundPosition: 'fixed'
};

const landingPage = () => {
    return (
        <>
            <nav>
                <div className="nav-wrapper">
                    <a href="#!" color="#BF360C" class="brand-logo">
                        <p className="brand">
                            abraba
                        </p>
                    </a>
                    <ul className="right hide-on-med-and-down">
                        <li className="li">
                            <p>Já tem uma conta?</p>
                            <a href="sass.html" className="bold">Entre aqui</a>
                        </li>
                        <li className="navButton">
                            <a class="waves-effect waves-light btn">Comece agora</a>
                        </li>
                    </ul>
                </div>
            </nav>

            <div style={sectionStyle} className="firstPage fixed">
                <div className="d-flex">
                    <h1>
                        Prepare-se, jovem aprendiz
                    </h1>
                    <h2>
                        Vamos te ajudar a lançar a braba e conseguir seu primeiro emprego!
                    </h2>

                    <div className="d-flex2">
                        <a className="waves-effect waves-light btn">
                            <p className="brand2">
                                Começar agora
                            </p>
                        </a>
                        <a>Saiba como</a>
                    </div>

                </div>
            </div>

            <div style={{ backgroundColor: '#00695C' }} className="firstPage fixed">
                <div className="display-flex">
                    <div className="display-flex">
                        <h1 style={{ overflowX: 'hidden' }}>
                            Veja como abraba promove a sua inclusão:
                    </h1>
                    </div>

                    <div className="d-flex">
                        <div className="card">
                            <div className="card-reveal">
                                <span class="card-title grey-text text-darken-4">Card Title<i class="material-icons right">close</i></span>
                                <p>Here is some more information about this product that is only revealed once clicked on.</p>
                            </div>
                            <div className="card-reveal">
                                <span className="card-title grey-text text-darken-4">Card Title<i class="material-icons right">close</i></span>
                                <p>Here is some more information about this product that is only revealed once clicked on.</p>
                            </div>
                            <div className="card-reveal">
                                <span className="card-title grey-text text-darken-4">Card Title<i class="material-icons right">close</i></span>
                                <p>Here is some more information about this product that is only revealed once clicked on.</p>
                            </div>
                        </div>
                    </div>


                </div>
            </div>
        </>
    )
}

export default landingPage; 