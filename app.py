from flask import Flask, url_for, render_template, redirect
from flask_bootstrap import Bootstrap5

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

import requests
import json
from pprint import pprint

app = Flask(__name__)
bootstrap = Bootstrap5(app)

