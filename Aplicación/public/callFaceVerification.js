var PythonShell = require("python-shell");
app.get('/face_verification', callFace_verification);

function callFace_verification(req, res) {
  PythonShell.run('./face_verification.py',function (err, data) {
    if (err) res.send(err);
    res.send(data.toString())
  });
}