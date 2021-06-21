import React from 'react'
import '../index.css';
import axios from 'axios';
import Ano_var_pais from '../components/Pais_var_max_min';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Button,Form,FormControl} from 'react-bootstrap'

export default class Max_min_año_var extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            paises_max_ano: [],
            busquedaXT :""
        }
        this.getMax = this.getMax.bind(this);
        this.min_pro = this.min_pro.bind(this);
        this.max_pro = this.max_pro.bind(this);
        this.getMin = this.getMin.bind(this);
        this.valor_buscar = this.valor_buscar.bind(this);
        this.busqueda_pais_ano = this.busqueda_pais_ano.bind(this);
    }

    async getMax() {
        
      const res = await axios.get('http://localhost:5000/get_ano_var_max');
      this.setState({paises_max_ano: res.data})
        
    }

    async getMin(){
        const res = await axios.get('http://localhost:5000/get_ano_var_min');
        this.setState({paises_max_ano: res.data})
    }

    async busqueda_pais_ano(event){
        event.preventDefault();
        const res = await axios.get('http://localhost:5000/get_max_min_var_busq/'+this.state.busquedaXT);
        this.setState({paises_max_ano: res.data})


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
                    <Button variant="outline-dark" onClick={this.max_pro} >Variables Maximas Por Pais</Button>
                    </div>
                    <div className="col-2">
                    <Button variant="outline-dark"onClick={this.min_pro} >Variables Minimas Por Pais</Button>
                    </div>
                </div>
                <div className='botonBusqueda'>
                  <Form inline>
                    <FormControl type="text" placeholder="Search"  onChange={this.valor_buscar} className="mr-sm-2" />
                    <Button  variant="outline-dark" onClick={this.busqueda_pais_ano}  >Search</Button>
                 </Form>
                 </div>
                 <br/>
                 <br/>
                <br/>
                <ul className='list-group'>
                    <div id='listaPaises-div'>
                    {
                        this.state.paises_max_ano.map(pais => 
                            
                            (<Ano_var_pais {...pais} key={pais.id} ></Ano_var_pais>)
                            
                            
                            )

                        

                    }
                    </div>
                </ul>
                
            </div>
        )
    }
}
