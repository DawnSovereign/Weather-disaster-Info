from flask import Flask, render_template, request
import requests
from flask_bootstrap import Bootstrap5


app = Flask(__name__)       
bootstrap = Bootstrap5(app)


