
import requests
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from pprint import pprint

#By Dylan Uribe

#API key for weather forecast

forecast_api_key = '7c66fb6dc5b98966d3c9709307417f82'

#Flask form that asks user for a zipcode

class ZipcodeForm(FlaskForm):
        user_zip = StringField(
            'Enter your ZipCode:', 
            validators= [DataRequired()]
        )
   

def getForecastData(userinput):
    """This function will take in user
    input, which should be a zipcode from somewhere in the
    US. This function will then return a dictionary of weather
    information, or return None if a error occurs"""
    location_link = f'http://api.openweathermap.org/geo/1.0/zip?zip={userinput}&appid={forecast_api_key}'
    try:
        r = requests.get(location_link)
        local = r.json()
        lat = local['lat']
        lon = local['lon']
        forecast_link = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={forecast_api_key}&units=imperial'
    except Exception as e:
        print("Error on zipcode:", e) 
    try:
        r = requests.get(forecast_link)
        data = r.json()
        return data
    except Exception as e:
        print("Error on forecast: ", e)
    return None

# Testing purposes, run this file on its own to test the functions.
# ans = input("Enter a zipcode ")
# data = getForecastData(ans)
# pprint(data)