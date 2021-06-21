const express = require('express');
const cors = require('cors');

const app = express();
//settings
app.set('port',5000);

// middlewares
app.use(cors());
app.use(express.json());

// routes
//app.get('/', (req, res)=> {
 //   res.send('Express server is up and running.');
 // })
 app.get('/', (req, res)=> {
  res.send('Express server is up and running.');
})

app.use(require('./routes/paises'));
app.use(require('./routes/continentes'));



module.exports = app;
