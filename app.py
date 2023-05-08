from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
import requests, json
app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/tornado')
def tornado():
    return render_template("tornado.html")

@app.route('/earthquakes', methods=['GET'])
def earthquakes():
    start_date = '2023-02-01'
    end_date = '2023-02-28'
    url = f'https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={start_date}&endtime={end_date}'
    
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

    return render_template('earthquakes.html', earthquakes=earthquakes, data=data)


 

@app.route('/handle_selection', methods = ['GET', 'POST'])
def handle_selection():
    selected_option = request.form.get('selected_option')

    if selected_option == 'tornado':
        return redirect(url_for('tornado'))
    
    elif selected_option == 'earthquakes':
        return redirect(url_for('earthquakes'))

    return redirect(url_for('home'))  # Home page is redirected if no option is selected 


