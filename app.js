const express = require('express');
require('./database/connection');
require('dotenv').config()
const expressLayouts =require('express-ejs-layouts');
const path =require('path');
const homeRoutes = require('./routes/home-routes');
const bodyparser = require('body-parser');
const morgan = require('morgan');
const connectDB =require('./database/connection');
app=express()
require('dotenv').config()



app.use(expressLayouts);
app.set('view engine','ejs');
app.use(morgan('tiny'));

app.use(bodyparser.urlencoded({extended:true}));

app.use(express.static(path.join(__dirname,'public')));
app.use(homeRoutes.routes);
const PORT = process.env.PORT || 3000
app.listen(PORT, ()=>{ console.log("Lostening to the server on http://localhost:3000")});