const MSG_INIT = 'Connected';
const MSG_ORIGIN_SYSTEM = 'S'
const MSG_ORIGIN_MORSE = 'M'
const MSG_ORIGIN_TEXT = 'T'
const NAMESPACE = '/morse-code-interpreter';

const socket = io(NAMESPACE);

document.addEventListener("DOMContentLoaded", function(event) {
    socket.on('connect', function() {
        socket.emit('mc_event', {data: MSG_INIT, origin: MSG_ORIGIN_SYSTEM});
    });

    socket.on('mc_response', function(msg, callBack) {
        if (msg.origin === MSG_ORIGIN_SYSTEM) {
            document.getElementById("spnStatus").textContent = msg.data;
        } else if (msg.origin === MSG_ORIGIN_MORSE){
            document.getElementById('emit_data_text').value = msg.data;
        } else {
            document.getElementById('emit_data_morse').value = msg.data;
        }
        if (callBack) callBack();
    });
});

function sendMessage(origin) {
    let msg;
    if (origin === MSG_ORIGIN_MORSE) {
        msg = document.getElementById('emit_data_morse').value;
    } else {
        msg = document.getElementById('emit_data_text').value;
    }
    socket.emit('mc_event', {data: msg, origin: origin});
}

function disconnect() {
    socket.emit('disconnect_request');
    document.getElementById('btnDisconnect').className += " hide";
    document.getElementById('btnReconnect').classList.remove("hide");
}

function reconnect() {
    window.location.reload(true);
}
