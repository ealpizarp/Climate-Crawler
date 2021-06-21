const app = require('./app');
const { conn } = require('./database');
require('./database')


async function main(){

    await app.listen(app.get('port'));
    console.log('Server 5000');
    
}

main();