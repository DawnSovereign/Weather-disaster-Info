from flask import Flask, render_template, request
import requests
from flask_bootstrap import Bootstrap5


app = Flask(__name__)       
bootstrap = Bootstrap5(app)

@app.route('/')
def home():
    return render_template('Air.html')

@app.route('/search', methods=['GET'])
def search():
    location = request.args.get('location')
    if location:
        api_key = '80745c411c034e788af778b4d36e6ffa'
        url = f"http://api.weatherbit.io/v2.0/current/airquality?key={api_key}&city={location}"
        response = requests.get(url)
        data = response.json()
        return render_template('Air.html', data=data)
    else:
        return render_template('Air.html')

if __name__ == '__main__':
    app.run()
