import React from 'react';
import Navigation from './components/Navigation';
import {BrowserRouter as Router,Route} from 'react-router-dom';
import Max_prome from './pages/Max_prome';
import Max_min_var_ano from './pages/Max_min_año_var';
import Deca from './pages/Decada_prom_cont';
import Estacion from './pages/Estacion';
import cont_pais_var from './pages/Contiente_pais_var';

function App() {
      return(
        <Router>
        <Navigation/>
        
        <div className='container p-4'>

          <Route path='/' exact component={Max_prome} />
          <Route path='/max_prome' exact component={Max_prome} />
          <Route path='/ano_min_max_var' exact component={Max_min_var_ano} />
          <Route path='/Decada_continente' exact component={Deca} />
          <Route path='/estacion' exact component={Estacion} />
          <Route path='/cont_pais_var' exact component={cont_pais_var} />



        </div>

        </Router>

        

      );


}

export default App;
