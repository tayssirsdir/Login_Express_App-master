const addserver = require('../model/modeladdserver');


// create and save new server
exports.create = (req,res)=> {
    // validate request
    if(!req.body){
        res.status(400).send({ message : "Content can not be emtpy!"});
        return;
    }
     // new user
     const server = new addserver({
        username : req.body.username,
        password : req.body.password,
        hostname: req.body.hostname,
        path : req.body.path
        
    })

    // save user in the database
    server
        .save(server)
        .then(server => {
         //res.send(server)
           res.redirect('/addserver');
        })
        .catch(err =>{
            res.status(500).send({
                message : err.message || "Some error occurred while creating a create operation"
            });
        });

}
// retrieve and return all servers / retrive and return a single server
exports.find = (req, res)=>{

   

        addserver.find(username)
            .then(allserver =>{
                res.send(allserver)
               
            })
            .catch(err =>{
                res.status(500).send({ message:err.message|| "Erro retrieving server with id " })
            })


    
}

// retrieve and return all users/ retrive and return a single user
exports.find = (req, res)=>{
;
        
         addserver.find({},{"username":1,"_id":0})
            .then(usernameserver =>{
                res.send(usernameserver)
        } )
            .then(usernameserver =>{
                if(!usernameserver){
                    res.status(404).send({ message : "Not found server with id "})
                }else{
                    res.send(server)
                }
            })
            .catch(err =>{
                res.status(500).send({ message: "Erro retrieving server with id " })
            })

  
            .catch(err => {
                res.status(500).send({ message : err.message || "Error Occurred while retriving server information" })
            })
    }

    
