from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
socketio = SocketIO(app)


@socketio.on('connect')
def on_connect():
    emit('server_message', {'message': 'Connected to the server'})

@socketio.on('client_message')
def on_client_message(data):
    print(f"Received random value from client: {data['random_value']}")
    random_value = random.randint(1, 100)
    emit('server_message', {'message': f'Server generated random value: {random_value}'})

if __name__ == '__main__':
    socketio.run(app)
