import React from 'react'
import '../index.css';
import axios from 'axios';
import Ano_var_pais from '../components/Pais_var_max_min';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Button,Form,FormControl} from 'react-bootstrap'
import { axiosInstance } from '../axiosConfig';

export default class Estacion extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            estaciones: [],
            busquedaXT :""
        }
        this.getMax = this.getMax.bind(this);
        this.min_pro = this.min_pro.bind(this);
        this.max_pro = this.max_pro.bind(this);
        this.getMin = this.getMin.bind(this);
        this.busquedaEstacion = this.busquedaEstacion.bind(this);
        this.valor_buscar = this.valor_buscar.bind(this);
    }

    async getMax() {
        
      const res = await axiosInstance.get('/get_estacion_max');
      this.setState({estaciones: res.data})
        
    }

    async getMin(){
        const res = await axiosInstance.get('/get_estacion_min');
        this.setState({estaciones: res.data})
    }

    async busquedaEstacion(event){
        event.preventDefault();
        const res = await axiosInstance.get('/get_estacion_busq/'+this.state.busquedaXT);
        this.setState({estaciones: res.data})


    }

    valor_buscar(event){
       
        this.setState({busquedaXT : event.target.value});
        

    }


    min_pro(even){
        this.getMin()

    }

    max_pro(even){
        this.getMax()
    }


    componentDidMount(){

        this.getMax();
    }


    render() {
        return (
        
            <div >

                <div className="form-group row">
                    <div className="col-2">
                    <Button variant="outline-dark" onClick={this.max_pro} >Estacion con variables maxima</Button>
                    </div>
                    <div className="col-2">
                    <Button variant="outline-dark"onClick={this.min_pro} >Estacion con variables minima</Button>
                    </div>
                </div>
                <div className='botonBusqueda'>
                  <Form inline>
                    <FormControl type="text" placeholder="Search" onChange={this.valor_buscar} className="mr-sm-2" />
                    <Button  variant="outline-dark" type="submit" onClick={this.busquedaEstacion}>Search</Button>
                 </Form>
                 </div>
                 <br/>
                 <br/>
                <br/>
                <ul className='list-group'>
                    <div id='listaPaises-div'>
                    {
                        this.state.estaciones.map(estacion => 
                            
                            (<Ano_var_pais {...estacion} key={estacion.id} ></Ano_var_pais>)
                            
                            
                            )

                        

                    }
                    </div>
                </ul>
                
            </div>
        )
    }
}
