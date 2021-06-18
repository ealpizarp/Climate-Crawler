const mysql = require('mysql');
const conn  = mysql.createPool({
  connectionLimit : 10,
  host            : '34.66.197.163',
  port            :  '3306',
  user            : 'admin',
  password        : 'adminpass',
  database        : 'DB2_PR2'
});
 
conn.query('SELECT 1 + 1 AS solution', function (error, results, fields) {
  if (error) throw error;
  console.log('The solution is: ', results[0].solution);
}
);

module.exports = {conn}