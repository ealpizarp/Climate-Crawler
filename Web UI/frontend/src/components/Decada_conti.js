import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../index.css';

 export default class Decada_conti extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            show: true
            }
           
        }
        
        render() {
    
            return (
                <div class='max_prom' >
                <div className="bg-white shadow overflow-hidden sm:rounded-lg">
              <div className="px-4 py-3 sm:px-6">
                <h3 className="text-lg leading-6 font-medium text-gray-900">{this.props.continente}</h3>

              </div>
              <div className="border-t border-gray-200">
                <dl>
                  <div className="bg-gray-50 px-4 py-3 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                    <dt className="text-sm font-medium text-gray-500">Decada</dt>
                    <dd className="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">{this.props.decada}</dd>
                  </div>
                  <div className="bg-gray-50 px-4 py-3 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                    <dt className="text-sm font-medium text-gray-500">Temperatura</dt>
                    <dd className="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">{this.props.temperatura}</dd>
                  </div>
                </dl>
              </div>
              </div>
              
              
              </div>
    
            );
        }
    }
