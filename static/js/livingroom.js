
/* This is the livingroom js stuff */


function show_livingroom(){
var HTML = "";
	HTML = HTML + 
"\
<p> This is the livingroom html </p>	\
<div id='kodi'>Kodi data here</div>\
"
;
document.getElementById("content").innerHTML=HTML;
}

$(document).ready(function(){
    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/kodi');

    //receive details from server
    socket.on('newnumber', function(msg) {
        console.log("Received " + msg);
        kodi_string = '<p> + msg.title </p>';
        $('#kodi').html(kodi_string);
    });

});


