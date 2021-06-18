const {conn} = require("../database");


const paisesCtrl = {}


paisesCtrl.getAño_Var_Maximo = (req ,res) => {
    
    try {
        
        const query = 'select * from MAX_YEAR_VAR';
        
        conn.query(query, function (error, results, fields) {
          
            if (error) throw error ;
            let results_array = [];
            results.forEach(result => {
                results_array.push({

                    id: result.ID,
                    pais: result.country,
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


paisesCtrl.getAño_Var_Minimo = (req ,res) => {
    
    try {
        
        const query = 'select * from MIN_YEAR_VAR';
        
        conn.query(query, function (error, results, fields) {
          
            if (error) throw error ;
            let results_array = [];
            results.forEach(result => {
                results_array.push({

                    id: result.ID,
                    pais: result.country,
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




paisesCtrl.pais_maximo_prome_gene = (req ,res) => {

    try {
        
        const query = 'select * from MAX_AVG_COUNTRY_TEMP order by temperature  DESC LIMIT 0 ,10';

        conn.query(query, function (error, results, fields) {
            if (error) throw error;
            let results_array = [];
            results.forEach(result => {
                results_array.push({
                    id: result.ID,
                    pais: result.country,
                    promedio: result.temperature
                });

            })
            return res.send(JSON.stringify(results_array));

        });


    } catch (error) {
        console.log(err)
        return res.status(400).jason({
        msg: ' '})
    }


}


paisesCtrl.pais_minimo_prome_gene = (req ,res) => {

    try {
        
        const query = 'select * from MAX_AVG_COUNTRY_TEMP order by temperature  ASC LIMIT 0 ,10';

        conn.query(query, function (error, results, fields) {
            if (error) throw error;
            let results_array = [];
            results.forEach(result => {
                results_array.push({
                
                    id: result.ID,
                    pais: result.country,
                    promedio: result.temperature

                });

            })
            return res.send(JSON.stringify(results_array));

        });


    } catch (error) {
        console.log(err)
        return res.status(400).jason({
        msg: ' '})
    }


}


paisesCtrl.busqueda_pais = async (req ,res) => {

    try { 
        var s = "'"+req.params.pais+"'"
        var query = 'SELECT pais_prome_general.pais , pais_prome_general.promedio, pais_con_estacion_maxima.estacion_maxima , pais_con_estacion_minima.estacion_minima,var_maxima_por_pais.ano_variable_maxima,var_minima_por_pais.ano_variable_minima FROM pais_prome_general,pais_con_estacion_maxima ,pais_con_estacion_minima ,var_minima_por_pais,var_maxima_por_pais WHERE pais_prome_general.pais = pais_con_estacion_minima.pais AND pais_prome_general.pais = pais_con_estacion_maxima.pais AND pais_prome_general.pais = var_minima_por_pais.pais AND pais_prome_general.pais = var_maxima_por_pais.pais AND pais_prome_general.pais = ?';
        console.log(query)
       await conn.query(query , [req.params.pais],function (error, results, fields){
            
            if (error) throw error;
            if(results.length != 0){
                const pais = {
                pais: result[0].pais,
                promedio: result[0].promedio,
                estacion_maxima: result[0].estacion_maxima,
                estacion_minima: result[0].estacion_minima,
                ano_variable_maxima: result[0].ano_variable_maxima,
                ano_variable_minimo: result[0].ano_variable_minima
                }

                return res.send(JSON.stringify(pais)) 

            }
            else {
                return res.send('Cannot find the contry with the given id');
            }

        })

        
    } catch (error) {
        console.log(err)
        return res.status(400).jason({
            msg: 'Error ocurred while trying to find contry'
        })
    }

}


paisesCtrl.getEstaciones_max = (req ,res) => {
    
    try {
        
        const query = 'select * from STATION_MAX_VAR';
        
        conn.query(query, function (error, results, fields) {
          
            if (error) throw error ;
            let results_array = [];
            results.forEach(result => {
                results_array.push({

                    id: result.ID,
                    pais: result.country,
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


paisesCtrl.getEstaciones_min = (req ,res) => {
    
    try {
        
        const query = 'select * from STATION_MIN_VAR';
        
        conn.query(query, function (error, results, fields) {
          
            if (error) throw error ;
            let results_array = [];
            results.forEach(result => {
                results_array.push({

                    id: result.ID,
                    pais: result.country,
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




//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////






module.exports = paisesCtrl