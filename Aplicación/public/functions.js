function move_to_info(){
    var home_container = document.getElementById('home_container');
    home_container.style.display = 'none'
    var info_container = document.getElementById('info_container');
    info_container.style.display = 'block'
}
function move_to_camera(){
    var info_container = document.getElementById('info_container');
    info_container.style.display = 'none'
    var camera_container = document.getElementById('camera_container');
    camera_container.style.display = 'block'
}
function move_to_main(){
    var info_container = document.getElementById('info_container');
    info_container.style.display = 'none'
    var home_container = document.getElementById('home_container');
    home_container.style.display = 'block'
}

function move_to_success(){
    var camera_container = document.getElementById('camera_container');
    camera_container.style.display = 'none'
    var success_container = document.getElementById('success_container');
    success_container.style.display = 'block'
}

function move_to_failure(){
    var camera_container = document.getElementById('camera_container');
    camera_container.style.display = 'none'
    var failure_container = document.getElementById('failure_container');
    failure_container.style.display = 'block'
}

function move_to_camera_ff(){
    var failure_container = document.getElementById('failure_container');
    failure_container.style.display = 'none'
    var info_container = document.getElementById('info_container');
    info_container.style.display = 'block'
}
function callFaceVerification(){
    var xhttp = new XMLHttpRequest();
    console.log('hola')
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("next").innerHTML = this.responseText;
        }
      };
    xhttp.open("GET", "http://localhost:3000/face_verification", true);
    xhttp.send();
} 