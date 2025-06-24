from flask import Flask, render_template, request
from flask_socketio import SocketIO, join_room, leave_room, emit
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'secret!')
app.config['REDIS_URL'] = os.environ.get(
    'REDIS_URL', 'redis://localhost:6379/0')

# Initialize SocketIO with Redis message queue
socketio = SocketIO(app, cors_allowed_origins="*",
                    message_queue=app.config['REDIS_URL'])

# Global room name
GLOBAL_ROOM = 'global-chat'


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('join')
def handle_join(data):
    username = data.get('username')
    join_room(GLOBAL_ROOM)
    emit('status', {'msg': f"{username} has joined the chat."},
         room=GLOBAL_ROOM)


@socketio.on('leave')
def handle_leave(data):
    username = data.get('username')
    leave_room(GLOBAL_ROOM)
    emit('status', {'msg': f"{username} has left the chat."}, room=GLOBAL_ROOM)


@socketio.on('message')
def handle_message(data):
    username = data.get('username')
    msg = data.get('msg')
    emit('message', {'username': username, 'msg': msg}, room=GLOBAL_ROOM)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
