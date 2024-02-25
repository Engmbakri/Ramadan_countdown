from flask import Flask, render_template, jsonify
import datetime
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_time_remaining')
def get_time_remaining():
    ramadan_date = datetime.datetime(2024, 3, 11)
    now = datetime.datetime.now()
    time_remaining = max(ramadan_date - now, datetime.timedelta())
    return jsonify({'time_remaining': str(time_remaining)})

if __name__ == '__main__':
    app.run(debug=True)
