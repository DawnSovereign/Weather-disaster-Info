from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_bootstrap import Bootstrap5
import urllib.request, json
import json
import os
import requests

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/wind', methods=['GET', 'POST'])
def wind():
    if request.method == 'POST':
        city = request.form.get('city')
        return redirect(url_for('wind_info', city=city))

    return render_template("wind.html")

@app.route('/wind_info')
def wind_info():
    api_key = '41d5f679408f743b97da7258b9457d56'
    city = request.args.get('city', 'New York')
    units = 'f'
    url = f'http://api.weatherstack.com/current?access_key={api_key}&query={city}&units={units}'
    response = requests.get(url)
    weather_data = response.json()

    return render_template("wind_info.html", weather_data=weather_data)

@app.route('/handle_selection', methods=['POST'])
def handle_selection():
    selected_option = request.form.get('selected_option')

    if selected_option == 'wind':
        return redirect(url_for('wind'))

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)


