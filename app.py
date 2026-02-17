from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to the Minions App!"


@app.route('/add', methods=['GET'])
def add():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is None or b is None:
        return jsonify({'error': 'Missing parameters'}), 400
    return jsonify({'result': a + b})


@app.route('/subtract', methods=['GET'])
def subtract():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is None or b is None:
        return jsonify({'error': 'Missing parameters'}), 400
    return jsonify({'result': a - b})


@app.route('/multiply', methods=['GET'])
def multiply():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is None or b is None:
        return jsonify({'error': 'Missing parameters'}), 400
    return jsonify({'result': a * b})


@app.route('/divide', methods=['GET'])
def divide():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is None or b is None:
        return jsonify({'error': 'Missing parameters'}), 400
    if b == 0:
        return jsonify({'error': 'Division by zero'}), 400
    return jsonify({'result': a / b})


if __name__ == '__main__':
    app.run(debug=True)
