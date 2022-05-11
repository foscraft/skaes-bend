from flask import Flask
from skae_app.skae.views import skae

app = Flask(__name__)
app.register_blueprint(skae)