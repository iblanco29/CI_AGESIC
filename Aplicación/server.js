var express = require("express");
var app     = express();
var path    = require("path");
var mysql = require("mysql");
const ps = require('python-shell')

var con = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "2924814"
});

con.connect(function(err) {
  if (err) throw err;
  console.log("Connected!");
});

//connection.query("INSERT INTO `data`(`name`, `date`, `status`, `ci`) VALUES ('Nacho','2018-09-18','1','47730676')")
app.use(express.static(__dirname + '/public'));

app.get('/',function(req,res){
  res.sendFile(path.join(__dirname+'/public/index.html'));
  //__dirname : It will resolve to your project folder.
});

app.get('/about',function(req,res){
  res.sendFile(path.join(__dirname+'/about.html'));
});

app.get('/sitemap',function(req,res){
  res.sendFile(path.join(__dirname+'/sitemap.html'));
});


app.get('/face_verification', function (req, res) {
    ps.PythonShell.run('/public/face_verification.py',null,function (err, data) {
    if (err) res.send(err);
    res.send(data)
  });
});

app.get('/hola',function(req,res){
	console.log('hola')
})

app.listen(3000);

console.log("Running at Port 3000");


