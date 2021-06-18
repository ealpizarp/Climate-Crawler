const {conn} = require("../database");


const contientesCtrl = {}

contientesCtrl.getContinentes_deca_temp = (req ,res) => {

    try {
        
        const query = 'select * from DECADE_AVG_TEMPERATURE order by DECADE_AVG_TEMPERATURE.continente asc';

        conn.query(query, function (error, results, fields) {
            
            if (error) throw error;
            let results_array = [];
            results.forEach(result => {
                results_array.push({

                    id: result.ID,
                    continente: result.continente,
                    decada: result.decada,
                    temperatura: result.temperatura

                });

            })
            return res.send(JSON.stringify(results_array));

        });



    } catch (error) {
        
    }


}


contientesCtrl.getCont_pais_var_max = (req ,res) => {
    
    try {
        
        const query = 'select * from MAX_COUNTRY_VAR';
        
        conn.query(query, function (error, results, fields) {
          
            if (error) throw error ;
            let results_array = [];
            results.forEach(result => {
                results_array.push({

                    id: result.ID,
                    pais: result.continent,
                    t: result.T,
                    tM: result.TMax,
                    tm: result.Tmin,
                    pp: result.PP,
                    v: result.V,
                    ra: result.RA,
                    sn : result.SN,
                    ts : result.TS,
                    fg : result.FG,
                    tn : result.TN,
                    gr : result.GR


                });

            })
            
            return res.send(JSON.stringify(results_array));

        });



    } catch (error) {
        console.log(error)
    }


}

contientesCtrl.getCont_pais_var_min = (req ,res) => {
    
    try {
        
        const query = 'select * from MIN_COUNTRY_VAR';
        
        conn.query(query, function (error, results, fields) {
          
            if (error) throw error ;
            let results_array = [];
            results.forEach(result => {
                results_array.push({

                    id: result.ID,
                    pais: result.continent,
                    t: result.T,
                    tM: result.TMax,
                    tm: result.Tmin,
                    pp: result.PP,
                    v: result.V,
                    ra: result.RA,
                    sn : result.SN,
                    ts : result.TS,
                    fg : result.FG,
                    tn : result.TN,
                    gr : result.GR


                });

            })
            
            return res.send(JSON.stringify(results_array));

        });



    } catch (error) {
        console.log(error)
    }


}





module.exports = contientesCtrl