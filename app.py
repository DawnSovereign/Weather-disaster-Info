from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from forecast import ZipcodeForm, getForecastData
app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config['SECRET_KEY'] = 'csumb-otter'

current_weather_api = '7c66fb6dc5b98966d3c9709307417f82'
forecastinfo = None

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/tornado')
def tornado():
    return render_template("tornado.html")

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

    if selected_option == 'tornado':
        return redirect(url_for('tornado'))
    if selected_option == 'weather_forecast':
        return redirect(url_for('forecast'))

    return redirect(url_for('home'))  # Home page is redirected if no option is selected 

if __name__ == '__main__':
    app.run(debug=True)
