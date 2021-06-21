import React from 'react'
import '../index.css';
import axios from 'axios';
import Ano_var_pais from '../components/Pais_var_max_min';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Button,Form,FormControl} from 'react-bootstrap'

export default class Contiente_pais_var extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            cont_pais_var: []
        }
        this.getMax = this.getMax.bind(this);
        this.min_pro = this.min_pro.bind(this);
        this.max_pro = this.max_pro.bind(this);
        this.getMin = this.getMin.bind(this);
    }

    async getMax() {
        
      const res = await axios.get('http://localhost:5000/get_continente_pais_var_max');
      this.setState({cont_pais_var: res.data})
        
    }

    async getMin(){
        const res = await axios.get('http://localhost:5000/get_continente_pais_var_min');
        this.setState({cont_pais_var: res.data})
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
                    <Button variant="outline-dark" onClick={this.max_pro} >Continente los países con los valores máximos </Button>
                    </div>
                    <div className="col-2">
                    <Button variant="outline-dark"onClick={this.min_pro} >Continente los países con los valores minimo</Button>
                    </div>
                </div>
                 <br/>
                 <br/>
                <br/>
                <ul className='list-group'>
                    <div id='listaPaises-div'>
                    {
                        this.state.cont_pais_var.map(cont => 
                            
                            (<Ano_var_pais {...cont} key={cont.id} ></Ano_var_pais>)
                            
                            
                            )

                        

                    }
                    </div>
                </ul>
                
            </div>
        )
    }
}