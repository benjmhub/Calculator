from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def calculator():
    return render_template('calculator.html')

@app.route('/evaluate', methods=['POST'])
def evaluate():
    try:
        expression = request.form['expression']
        result = eval(expression)
        return str(result)
    except Exception as e:
        return "Error"

if __name__ == '__main__':
    app.run(debug=True)
