from flask import Flask, jsonify, request

app = Flask(__name__)

# Correct way to disable JSON key sorting in Flask 3.x
app.json.sort_keys = False

@app.route('/')
def home():
    return jsonify({
        "application": "Menu-Driven Calculator API",
        "version": "1.0.0",
        "supported_operations": ["add", "subtract"]
    }), 200

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/add', methods=['GET'])
def add():
    try:
        num1 = float(request.args.get('num1', 0))
        num2 = float(request.args.get('num2', 0))
        return jsonify({"operation": "addition", "num1": num1, "num2": num2, "result": num1 + num2}), 200
    except ValueError:
        return jsonify({"error": "Invalid numerical parameters"}), 400

@app.route('/subtract', methods=['GET'])
def subtract():
    try:
        num1 = float(request.args.get('num1', 0))
        num2 = float(request.args.get('num2', 0))
        return jsonify({"operation": "subtraction", "num1": num1, "num2": num2, "result": num1 - num2}), 200
    except ValueError:
        return jsonify({"error": "Invalid numerical parameters"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
