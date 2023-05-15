from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_bootstrap import Bootstrap5
import urllib.request, json
import json
import os
import requests

app = Flask(__name__)
bootstrap = Bootstrap5(app)

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/earthquakes', methods=['GET', 'POST'])
def earthquakes():
    start_date = '2023-05-01'
    end_date = '2023-05-09'
    magnitude = '4'
    # start_date = request.args.get('start_date')
    # end_date = request.args.get('end_date')
    # magnitude = request.args.get('magnitude')
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

@app.route('/handle_selection', methods=['POST'])
def handle_selection():
    selected_option = request.form.get('selected_option')

    if selected_option == 'earthquakes':
        return redirect(url_for('earthquakes'))

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

