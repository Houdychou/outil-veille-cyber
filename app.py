from flask import *
import requests

app = Flask(__name__)

url = "https://cert.cyber.gouv.fr/avis/json/"

api = requests.get(url)

cert_avis = api.json()[-5:] ## récupère les 5 derniers avis du CERT-FR

@app.route("/")
def render_main_page():
    return render_template("index.html", avis=cert_avis)