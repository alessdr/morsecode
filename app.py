from flask import Flask, render_template, session, copy_current_request_context
from flask_socketio import SocketIO, emit, disconnect
from decouple import config


async_mode = None
# Temporary fix to debug in pycharm
app = Flask(__name__, instance_path="/{project_folder_abs_path}/instance")
app.config['SECRET_KEY'] = config('SECRET')
socketio = SocketIO(app, async_mode=async_mode)


@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)


@socketio.on('mc_event', namespace='/morse-code-interpreter')
def receive_message(message):
    emit('mc_response', {'data': message['data']})


@socketio.on('disconnect_request', namespace='/morse-code-interpreter')
def disconnect_request():
    @copy_current_request_context
    def can_disconnect():
        disconnect()

    emit('mc_response', {'data': 'Disconnected!'}, callback=can_disconnect)


if __name__ == '__main__':
    '''
    environment = config('ENVIRONMENT')
    port = config('PORT')
    '''
    socketio.run(app, debug=True)
