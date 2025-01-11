from flask import Flask, request, jsonify
import math

app = Flask(__name__)

def numerical_integration(lower, upper):
    L = []  # Store results for different N
    N = 1
    while len(L) < 6:
        N *= 10  # Increase the number of intervals
        width = (upper - lower) / N
        total_area = 0.0
        for i in range(N):
            x = lower + i * width
            height = abs(math.sin(x))
            total_area += height * width
        L.append(total_area)
    return L
@app.route('/')
def home():
    return "Welcome to the Numerical Integration API! Use /integrate?lower=<value>&upper=<value> to calculate."

@app.route('/integrate', methods=['GET'])
def integrate():
    try:
        lower = float(request.args.get('lower', 0))
        upper = float(request.args.get('upper', math.pi))
        result = numerical_integration(lower, upper)
        
        return jsonify({
            "lower": lower,
            "upper": upper,
            "results": result
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
