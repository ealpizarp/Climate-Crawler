import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../index.css';

 export default class Pais extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            show: true
            }
           
        }
        
        render() {
    
            return (
                <div class='ttt' >
                <div className="bg-white shadow overflow-hidden sm:rounded-lg">
              <div className="px-4 py-3 sm:px-6">
                <h3 className="text-lg leading-6 font-medium text-gray-900">Pais                 </h3>
                <p className="mt-1 max-w-2xl text-sm text-gray-500">{this.props.pais}</p>
              </div>
              <div className="border-t border-gray-200">
                <dl>
                  <div className="bg-gray-50 px-4 py-3 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                    <dt className="text-sm font-medium text-gray-500">Promedio General</dt>
                    <dd className="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">{this.props.promedio}</dd>
                  </div>
                  <div className="bg-white px-4 py-3 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                    <dt className="text-sm font-medium text-gray-500">Estacion Con Valores Maximos</dt>
                    <dd className="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">{this.props.estacion_maxima}</dd>
                  </div>
                  <div className="bg-gray-50 px-4 py-3 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                    <dt className="text-sm font-medium text-gray-500">Estacion Con Valores Minimos</dt>
                    <dd className="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">{this.props.estacion_minima}</dd>
                  </div>
                  <div className="bg-white px-4 py-3 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                    <dt className="text-sm font-medium text-gray-500">Año donde las variables fueron las maxima</dt>
                    <dd className="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">{this.props.ano_variable_maxima}</dd>
                  </div>
                  <div className="bg-white px-4 py-3 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                    <dt className="text-sm font-medium text-gray-500">Año donde las variables fueron las minima</dt>
                    <dd className="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">{this.props.ano_variable_minimo}</dd>
                  </div>
                </dl>
              </div>
              </div>
              
              
              </div>
    
            );
        }
    }


