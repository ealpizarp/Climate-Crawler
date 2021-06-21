import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../index.css';

 export default class Max_prom_gene extends React.Component {

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
                <h3 className="text-lg leading-6 font-medium text-gray-900">{this.props.pais} </h3>
              </div>
              <div className="border-t border-gray-200">
                <dl>
                  <div className="bg-gray-50 px-4 py-3 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                    <dt className="text-sm font-medium text-gray-500">Promedio General</dt>
                    <dd className="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">{this.props.promedio}</dd>
                  </div>
                </dl>
              </div>
              </div>
              
              
              </div>
    
            );
        }
    }
