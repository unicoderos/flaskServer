var socket = io.connect('http://' + document.domain + ':' + location.port);

socket.on('connect', function () {
    console.log('Websocket connected!');
});

socket.on('new_data', function (data) {
    //console.log(JSON.stringify(data, null, 2));
    document.getElementById('google_price').innerHTML = data['google'];
    document.getElementById('hotmail_price').innerHTML = data['hotmail'];
    document.getElementById('yahoo_price').innerHTML = data['yahoo'];
    document.getElementById('netflix_price').innerHTML = data['netflix'];
});

function getNumber() {
    console.log('Requesting Number...');
    socket.emit('getNumber', {low: 100, up: 200});
}