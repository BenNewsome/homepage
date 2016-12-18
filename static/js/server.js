
function show_server(){
	serverHTML = " \
<p> This is the server html </p>	\
<div id='serverRam'>Ram usage here</div>\
"
	

	document.getElementById("content").innerHTML=serverHTML;
}
$(document).ready(function(){
    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    var numbers_received = [];


    // recive the menu for the house

    //receive details from server
    socket.on('newnumber', function(msg) {
        console.log("Received number" + msg.number);
        //maintain a list of ten numbers
        if (numbers_received.length >= 1){
            numbers_received.shift()
        }
        numbers_received.push(msg.number);
        numbers_string = '';
        for (var i = 0; i < numbers_received.length; i++){
            numbers_string = numbers_string + '<p>' + numbers_received[i].toString() + '</p>';
        }
        $('#serverRam').html(numbers_string);
    });

});
