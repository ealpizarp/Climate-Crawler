const {Router} =require('express');
const router = Router();


const{getContinentes_deca_temp,getCont_pais_var_max,getCont_pais_var_min,getContinentes_deca_temp_busqueda
} = require('../controllers/continentes.controllers');


router.route('/get_continentes_deca_temp').get(getContinentes_deca_temp);

router.route('/get_continente_pais_var_max').get(getCont_pais_var_max);

router.route('/get_continente_pais_var_min').get(getCont_pais_var_min);

router.route('/get_continentes_deca_temp_busqueda/:nombre_cont').get(getContinentes_deca_temp_busqueda);


module.exports =router;