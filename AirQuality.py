from flask import Flask, render_template
import requests
from flask_bootstrap import Bootstrap5
import os

app = Flask(__name__)
bootstrap = Bootstrap5(app)

WEATHERBIT_API_KEY = os.environ.get('WEATHERBIT_API_KEY')
WEATHERBIT_API_URL = 'http://api.weatherbit.io/v2.0/current/airquality'

def get_air_quality_data(city):
    params = {
        'city': city,
        'key': WEATHERBIT_API_KEY
    }
    response = requests.get(WEATHERBIT_API_URL, params=params)
    response.raise_for_status()
    data = response.json()
    return data['data'][0]

@app.route('/')
def index():
    city = 'New York'  # Replace with user input or use a default value
    try:
        air_quality_data = get_air_quality_data(city)
    except requests.exceptions.HTTPError as error:
        air_quality_data = None
        print(f"Error: {error}")
    return render_template('Air.html', data=air_quality_data)