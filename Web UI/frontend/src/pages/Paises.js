import React from 'react'
import '../index.css';
import axios from 'axios';
import PaisesU from '../components/Pais';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Form,FormControl,Button} from 'react-bootstrap'
import { axiosInstance } from '../axiosConfig';

export default class Paises extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            paises: []
        }
        this.getPaises = this.getPaises.bind(this);
    }

    async getPaises() {
        
      const res = await axiosInstance.get('/get_paises');
      this.setState({paises: res.data})
        
    }


    componentDidMount(){

        this.getPaises();
    }


    render() {
        return (
        
            <div >

                <div class="form-group row">
                    <div class="col-2">
                    <Button variant="outline-dark" >Maximos promedios generales</Button>
                    </div>
                    <div class="col-2">
                    <Button variant="outline-dark">Minimos promedios generales</Button>
                    </div>
                </div>

                <div class = "btn-toolbar pull-right" >
                
                </div>
                <div className='botonBusqueda'>
                  <Form inline>
                    <FormControl type="text" placeholder="Search" className="mr-sm-2" />
                    <Button  variant="outline-dark">Search</Button>
                 </Form>
                 </div>
                <br/>
                <br/>
                <br/>
                <ul className='list-group'>
                    <div id='listaPaises-div'>
                    {
                        this.state.paises.map(pais => 
                            
                            (<PaisesU {...pais} key={pais.pais} ></PaisesU>)
                            
                            
                            )

                        

                    }
                    </div>
                </ul>
                
            </div>
        )
    }
}



