from flask import Flask, render_template
import requests, json
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap5 = Bootstrap5(app)