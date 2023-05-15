from flask import Flask, render_template
import requests
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def home():
    # Make the API request
    api_key = '80745c411c034e788af778b4d36e6ffa'
    latitude = 35.7721
    longitude = -78.63861
    url = f"http://api.weatherbit.io/v2.0/current/airquality?key={api_key}&lat={latitude}&lon={longitude}"
    response = requests.get(url)
    data = response.json()

    # Extract the required data from the response
    city = data['city_name']
    country = data['country_code']
    aqi = data['data'][0]['aqi']
    pm25 = data['data'][0]['pm25']

    # Render the template with the data
    return render_template('Air.html', city=city, country=country, aqi=aqi, pm25=pm25)

if __name__ == '__main__':
    app.run()