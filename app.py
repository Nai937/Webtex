import os
import time
from flask import Flask, request, jsonify, send_from_directory
from flask_socketio import SocketIO

app = Flask(__name__, static_folder='.', static_url_path='')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'valentine-secret-key')

socketio = SocketIO(app, cors_allowed_origins="*")

# In-memory message storage
messages = []


# ========================================
# Static file serving
# ========================================
@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')


@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)


# ========================================
# REST API
# ========================================
@app.route('/api/messages', methods=['GET'])
def get_messages():
    return jsonify(messages)


@app.route('/api/messages', methods=['POST'])
def add_message():
    data = request.get_json()
    msg = {
        'id': int(time.time() * 1000),
        'text': data.get('text', ''),
        'name': data.get('name', ''),
        'highlighted': data.get('highlighted', False),
        'timestamp': data.get('timestamp', '')
    }
    messages.append(msg)
    socketio.emit('new_message', msg)
    return jsonify(msg), 201


@app.route('/api/messages/<int:msg_id>', methods=['DELETE'])
def delete_message(msg_id):
    global messages
    messages = [m for m in messages if m['id'] != msg_id]
    socketio.emit('delete_message', {'id': msg_id})
    return jsonify({'ok': True})


@app.route('/api/messages', methods=['DELETE'])
def clear_messages():
    global messages
    messages = []
    socketio.emit('clear_messages')
    return jsonify({'ok': True})


# ========================================
# WebSocket events
# ========================================
@socketio.on('connect')
def handle_connect():
    print('Client connected')


@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    socketio.run(app, host='0.0.0.0', port=port, debug=True)
