import React, { Component } from 'react'
import {Navbar,Nav} from 'react-bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css';
import { CloudLightningRain } from 'react-bootstrap-icons';
import '../index.css'


export default class Navigation extends Component {
    render() {
        return (
          <div>
            <Navbar bg="dark" variant="dark">
             <CloudLightningRain className="ml-1" />
             
            <Navbar.Brand href="/Decada_continente">Climate Crawler</Navbar.Brand>
            <Nav className="mr-auto">

             <Nav.Link href="/Decada_continente">Continentes</Nav.Link>
             <Nav.Link href="/cont_pais_var">Estadisticas por continente</Nav.Link>
              <Nav.Link href="/max_prome">Promedios</Nav.Link>
              <Nav.Link href="/estacion">Estacion</Nav.Link>
              <Nav.Link href="/ano_min_max_var">Estadisticas por año</Nav.Link>
              
              
              
            </Nav>
          </Navbar>
          

          </div>

              
        );
    }
}



