const mongoose = require('mongoose');

var schema = new mongoose.Schema({
    username : {
        type : String,
        required: true
    },
    password : {
        type: String,
        required: true,
        unique: true
    },
    hostname : {
        type: String,
        required: true,
        unique: true
    },
    path: {
        type: String,
        required: true,
        unique: true
    }
})

const addserver = mongoose.model('addserver', schema);

module.exports = addserver;