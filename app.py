from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_bootstrap import Bootstrap5
from forecast import ZipcodeForm, getForecastData
import requests
app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config['SECRET_KEY'] = 'csumb-otter'

current_weather_api = '7c66fb6dc5b98966d3c9709307417f82'
forecastinfo = None

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
    response = request.get(url)
    weather_data = response.json()

    return render_template("wind_info.html", weather_data=weather_data)
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
    response = request.get(url)
    weather_data = response.json()

    return render_template("wind_info.html", weather_data=weather_data)

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
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)




