var express = require("express");
var app     = express();
var path    = require("path");
var mysql = require("mysql");
var PythonShell = require("python-shell");

var connection = mysql.createConnection({
	host: 'localhost',
	user: 'root',
	password: '2924814',
	database: 'autentiddb'
});

connection.connect(function(error){
	if(!!error){
		console.log('ERROR');
	}else{
		console.log('CONNECTED');
	}
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
  PythonShell.run('./face_verification.py',function (err, data) {
    if (err) res.send(err);
    res.send(data.toString())
  });
});

app.listen(3000);

console.log("Running at Port 3000");


