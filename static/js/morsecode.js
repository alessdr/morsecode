const namespace = '/morse-code-interpreter';
const socket = io(namespace);

document.addEventListener("DOMContentLoaded", function(event) {
    socket.on('connect', function() {
        socket.emit('mc_event', {data: 'Connected to the SocketServer...'});
    });

    socket.on('mc_response', function(msg, callBack) {
        let log = document.getElementById('log');
        log.innerHTML = '<br><div><span>logs: ' + msg.data + '</span></div>';
        if (callBack) callBack();
    });
});

function sendMessage() {
    let msg = document.getElementById('emit_data').value;
    socket.emit('mc_event', {data: msg});
}

function disconnect() {
    socket.emit('disconnect_request');
}
