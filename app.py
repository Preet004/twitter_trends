from flask import Flask, render_template, jsonify
from selenium_driver.scraper import fetch_trends
from database.trend_model import store_trends, get_latest_trends

app = Flask(__name__)

@app.route('/')
def index():
    record = get_latest_trends()
    return render_template('index.html', record=record)

@app.route('/run-script')
def run_script():
    trend_data = fetch_trends()
    store_trends(trend_data)
    return render_template('index.html', record=trend_data)

if __name__ == '__main__':
    app.run(debug=True)
