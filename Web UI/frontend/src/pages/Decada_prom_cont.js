import React from 'react'
import '../index.css';
import axios from 'axios';
import Decada from '../components/Decada_conti';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Button,Form,FormControl} from 'react-bootstrap'
import { axiosInstance } from '../axiosConfig';

export default class Decada_prom_cont extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            contientes: [],
            busquedaXT: ""
        }
        this.getcontinentes = this.getcontinentes.bind(this);
        this.valor_buscar = this.valor_buscar.bind(this);
        this.busquedaCont = this.busquedaCont.bind(this);
    }

    async getcontinentes() {
        
      const res = await axiosInstance.get('/get_continentes_deca_temp');
      this.setState({contientes: res.data})
        
    }

    async busquedaCont(event){
        event.preventDefault();
        const res = await axiosInstance.get('/get_continentes_deca_temp_busqueda/'+this.state.busquedaXT);
        this.setState({contientes: res.data})



    }

    valor_buscar(event){
       
        this.setState({busquedaXT : event.target.value});
        

    }
  


    componentDidMount(){

        this.getcontinentes();
    }


    render() {
        return (
        
            <div >

            
                <div className='botonBusqueda'>
                  <Form inline>
                    <FormControl type="text" placeholder="Search" onChange={this.valor_buscar} className="mr-sm-2" />
                    <Button  variant="outline-dark" type="submit" onClick={this.busquedaCont} >Search</Button>
                 </Form>
                 </div>
                 <br/>
                 <br/>
                <br/>
                <ul className='list-group'>
                    <div id='listaPaises-div'>
                    {
                        this.state.contientes.map(contiente => 
                            
                            (<Decada {...contiente} key={contiente.id} ></Decada>)
                            
                            
                            )

                        

                    }
                    </div>
                </ul>
                
            </div>
        )
    }
}
