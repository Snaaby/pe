from flask import Flask, request, jsonify
from calculator import add, subtract, multiply, divide, square

app = Flask(__name__)

API_KEY = "calculator-secret-key"

@app.route("/")
def index():
    return jsonify({
        "name": "Calculator API",
        "endpoints": {
            "POST /api/add": "Сложение",
            "POST /api/subtract": "Вычитание", 
            "POST /api/multiply": "Умножение",
            "POST /api/divide": "Деление",
            "POST /api/square": "Квадрат"
        }
    })

@app.route("/api/add", methods=["POST"])
def api_add():
    data = request.get_json()
    result = add(data["a"], data["b"])
    return jsonify({"result": result})

@app.route("/api/subtract", methods=["POST"])
def api_subtract():
    data = request.get_json()
    result = subtract(data["a"], data["b"])
    return jsonify({"result": result})

@app.route("/api/multiply", methods=["POST"])
def api_multiply():
    data = request.get_json()
    result = multiply(data["a"], data["b"])
    return jsonify({"result": result})

@app.route("/api/divide", methods=["POST"])
def api_divide():
    data = request.get_json()
    result = divide(data["a"], data["b"])
    return jsonify({"result": result})

@app.route("/api/square", methods=["POST"])
def api_square():
    data = request.get_json()
    result = square(data["a"])
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
