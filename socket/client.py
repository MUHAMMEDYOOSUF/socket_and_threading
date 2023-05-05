import socketio
import random 
sio = socketio.Client()

# Connect to the server
@sio.on('connect')
def on_connect():
    print('Connected to the server')

# Handle server messages
@sio.on('server_message')
def on_server_message(data):
    print(f"Received message from server: {data['message']}")

if __name__ == '__main__':
    # Connect the client to the server
    sio.connect('http://localhost:5000')

    # Send a message to the server
    random_value = random.randint(1, 100)
    sio.emit('client_message', {'random_value': random_value})

    # Wait for the response from the server
    sio.wait()
