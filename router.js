var express = require("express");
var router = express.Router();

//const  credential = {
    //email : "admin@gmail.com",
    //password : "admin123"
//}
//const scp = require('node-scp')
//var fs = require('fs');

var local_file_path = '/slev5/conf/ mdservices.ini';
var detination_file_path = ' C:\slev5';
var fs = require('fs')
, ini = require('ini')

var config = ini.parse(fs.readFileSync('./config.ini', 'utf-8'))
// login user
const { exec } = require("child_process");
//var a=config.host;
//var b=config.password;
//var command= "start putty.exe -ssh " +config.username+"@"+config.ip+ " -pw " +config.password ;
var command= "start putty.exe -ssh " +config.usernameMDS+"@"+config.ipMDS+ " -pw " +config.passwordMDS ;
 //var command= "start scp tswx01@10.215.10.131: ~/slev5/conf/ slev5swxess.ini";

//var command3= " start scp "+config.username+"@"+config.ip+":"+config.pathsw ;
var command3= "start scp " +config.usernameMDS+"@"+config.ipMDS+":"+config.pathsw+" mdsold.ini ";
//const command = require("nodemon/lib/config/command");
//const childini = exec ('ini',['config.ini']);
router.post('/login', (req, res)=>{
    //if(req.body.username == config.username && req.body.password == config.password){
       // req.session.user = req.body.username;
        res.redirect('/route/dashboard');
        exec(command, (error, stdout, stderr) => { 
            if (error) {
                console.log(`error: ${error.message}`);
                return;
            }
            if (stderr) {
                console.log(`stderr: ${stderr}`);
                return;
            }
            console.log(`stdout: ${stdout}`);
        });
        //res.end("Login Successful...!");
   // }else{
       // res.end("Invalid Username")
   // }
});


router.post('/download', (req, res)=>{
    //if(req.body.username == config.username && req.body.password == config.password){
       // req.session.user = req.body.username;
        res.redirect('/upload');
        exec(command3, (error, stdout, stderr) => { 
            
            if (error) {
                console.log(`error: ${error.message}`);
                return;
            }
            if (stderr) {
                console.log(`stderr: ${stderr}`);
                return;
            }
            //console.log(`stdout: ${stdout}`);
        });
        //res.end("Login Successful...!");
   // }else{
       // res.end("Invalid Username")
   // }
});
// route for dashboard
router.get('/dashboard', (req, res) => {
    //if(req.session.user){
        res.render('base');
   // }else{
       // res.send("Unauthorize User")
   // }
})

// route for logout
router.get('/logout', (req ,res)=>{
    req.session.destroy(function(err){
        if(err){
            console.log(err);
            res.send("Error")
        }else{
            res.render('base', { title: "Express", logout : "logout Successfully...!"})
        }
    })
})

module.exports = router;