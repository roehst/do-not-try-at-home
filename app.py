# app.py

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

TODOS = []

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('execute_py')
def handle_execute_py(data):
    global TODOS
    # Show the code being executed
    print("Executing code:")
    print(data['code'])
    # Create a local context with necessary variables
    local_context = {'emit': emit, 'TODOS': TODOS, 'data': data}
    # Execute the code
    exec(data['code'], globals(), local_context)
    # No need to update TODOS as it's mutable and changes are reflected

if __name__ == '__main__':
    socketio.run(app)