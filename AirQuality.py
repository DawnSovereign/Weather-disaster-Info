from flask import Flask, render_template
import requests

from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap5 = Bootstrap5(app)

api_key = '6fc459c195d2f30852cf3074447bdeafa7a0eb202abc1fbb18a9b4ba882d5b1f'

payload = {
  'api_key': api_key
}

endpoint = 'https://api-dashboard.getambee.com/#/'

@app.route('/')
def main():
    data = None
    try:
        print('ran')
        r = requests.get(endpoint, params=payload)
        data = r.json()
        # print(data)
        print(data)
    except Exception as e:
        print('please try again', e)
    return render_template('Air.html', data=data) 
