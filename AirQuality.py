from flask import Flask, render_template
import requests, _json
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap5 = Bootstrap5(app)

api_key = '6fc459c195d2f30852cf3074447bdeafa7a0eb202abc1fbb18a9b4ba882d5b1f'

payload = {
  'api_key': api_key
}

endpoint = 'https://api.ambeedata.com/latest/by-lat-lng?lat=12&lng=77'


try:
    r = requests.get(endpoint, params=payload)
    local = r.json()
    ozone = local['OZONE']
except Exception as e:
    print('Error: ', e)


@app.route('/')
def main():
    
    try:
        print('ran')
        r = requests.get(endpoint, params=payload)
        data = r.json()
        
        print(data)

    except:
        print('please try again')
    return render_template('Air.html', data=data) 