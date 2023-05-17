from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_bootstrap import Bootstrap5
from forecast import ZipcodeForm, getForecastData
import requests
import urllib.request, json
import json
import os
import requests
#CST205 Project Final
# By Ruben Tafoya, Dylan Uribe, Aurelio Lopez, and Jason Kim

app = Flask(__name__)
bootstrap = Bootstrap5(app)

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config['SECRET_KEY'] = 'csumb-otter'

forecastinfo = None

###Functons for homepage
# By Ruben Tafoya
@app.route('/')
def home():
    return render_template("home.html")
### Functions for wind
# By Ruben Tafoya 
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

### Functions for forecast view
# By Dylan Uribe
@app.route('/forecast', methods = ['GET', 'POST'])
def forecast():
    form = ZipcodeForm()
    global forecastinfo
    if form.validate_on_submit():
        print('Form validated as submited')
        try:
            forecastinfo = getForecastData(form.user_zip.data)
            print('About to attempt redirect')
            return redirect('/forecast_view')
        except Exception as e:
            print("Error on running function: ", e)
            return redirect('/') 
    return render_template('forecastSearch.html', form = form)


@app.route('/forecast_view', methods = ['GET', 'POST'])
def forecastview():
    if forecastinfo == None:
        return redirect('/')
    else: 
        return render_template('forecastView.html', forecastinfo = forecastinfo)
    # return render_template('forecastView.html', forecastinfo = forecastinfo)

### Function for Earthquakes
# By Aurelio Lopez
@app.route('/earthquakes', methods=['GET', 'POST'])
def earthquakes():
    start_date = '2023-05-01'
    end_date = '2023-05-09'
    magnitude = '4'
    url = f'https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={start_date}&endtime={end_date}&minmagnitude={magnitude}'


    response = requests.get(url)
    data = response.json()
    # print(data)

    earthquakes = []
    features = data.get('features', [])
    for feature in features:
        place = feature['properties']['place']
        magnitude = feature['properties']['mag']
        earthquake = {'place': place, 'magnitude': magnitude}
        earthquakes.append(earthquake)

    cities = [earthquake['place'] for earthquake in earthquakes]
    magnitudes = [earthquake['magnitude'] for earthquake in earthquakes]

    return render_template('earthquakes.html', cities=cities, magnitudes=magnitudes)

### More Homepage
# By Ruben Tafoya
@app.route('/handle_selection', methods=['POST'])
def handle_selection():
    selected_option = request.form.get('selected_option')

    if selected_option == 'wind':
        return redirect(url_for('wind'))
    if selected_option == 'tornado':
        return redirect(url_for('tornado'))
    if selected_option == 'weather_forecast':
        return redirect(url_for('forecast'))
    if selected_option == 'wind':
        return redirect(url_for('wind'))
    if selected_option == 'earthquakes':
        return redirect(url_for('earthquakes'))

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

