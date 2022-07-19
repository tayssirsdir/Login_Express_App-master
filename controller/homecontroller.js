
const indexView =(req,res,next)=>{
    res.render('home');
}
const downloadfileView =(req,res,next)=>{
    res.render('downloadfile');
}
const serverconnectivtyView =(req,res,next)=>{
    res.render('serverconnectivty');
}
const addserverView =(req,res,next)=>{
    res.render('addserver');
}
const listeoffilesView =(req,res,next)=>{
    res.render('listeoffiles');
}
module.exports={
    indexView,
    downloadfileView,
    serverconnectivtyView,
    addserverView,
    listeoffilesView
}