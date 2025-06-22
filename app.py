from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    value = float(request.form['value'])
    unit_from = request.form['unit_from']
    unit_to = request.form['unit_to']

    # Example conversion logic
    if unit_from == 'pounds' and unit_to == 'kilos':
        result = value * 0.453592
    elif unit_from == 'kilos' and unit_to == 'pounds':
        result = value / 0.453592
    else:
        result = "Unsupported conversion"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host="0.0.0.0", port=port)

