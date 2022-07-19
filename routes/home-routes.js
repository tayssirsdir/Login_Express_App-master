const express = require('express');
const{indexView, downloadfileView, serverconnectivtyView ,addserverView,listeoffilesView} = require('../controller/homecontroller');
const router = express.Router();
const services = require('../services/addserverrender');

const controller = require('../controller/addservercontroller');

//API 
router.post('/api/addserver',controller.create) 

router.get('/api/addserver',controller.find)
//router.get('/api/addserver',controller.find)





   

router.get('/',indexView);
router.get('/downloadfile',downloadfileView);
router.get('/serverconnectivty',serverconnectivtyView);
router.get('/addserver',addserverView);
router.get('/listeoffiles',listeoffilesView);
module.exports={
    routes:router
}
