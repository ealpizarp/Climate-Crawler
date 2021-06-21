import React from 'react'
import '../index.css';
import axios from 'axios';
import Max_pro from '../components/Max_prom_gene';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Button} from 'react-bootstrap'
import { axiosInstance } from '../axiosConfig';

export default class Max_prome extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            paises_max_pro: []
        }
        this.getMax_prome = this.getMax_prome.bind(this);
        this.min_pro = this.min_pro.bind(this);
        this.max_pro = this.max_pro.bind(this);
    }

    async getMax_prome() {
        
      const res = await axiosInstance.get('/get_paises_promedio_general_max');
      this.setState({paises_max_pro: res.data})
        
    }

    async getMin_prome(){
        const res = await axiosInstance.get('/get_paises_promedio_general_mini');
        this.setState({paises_max_pro: res.data})
    }

    min_pro(even){
        this.getMin_prome()

    }

    max_pro(even){
        this.getMax_prome()
    }


    componentDidMount(){

        this.getMax_prome();
    }


    render() {
        return (
        
            <div >

                <div class="form-group row">
                    <div class="col-2">
                    <Button variant="outline-dark" onClick={this.max_pro} >Maximos promedios generales</Button>
                    </div>
                    <div class="col-2">
                    <Button variant="outline-dark"onClick={this.min_pro} >Minimos promedios generales</Button>
                    </div>
                </div>

                
                <br/>
                <ul className='list-group'>
                    <div id='listaPaises-div'>
                    {
                        this.state.paises_max_pro.map(pais => 
                            
                            (<Max_pro {...pais} key={pais.id} ></Max_pro>)
                            
                            
                            )

                        

                    }
                    </div>
                </ul>
                
            </div>
        )
    }
}
