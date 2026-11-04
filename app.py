from flask import *
import requests
import datetime as dt

app = Flask(__name__)

url = "https://cert.cyber.gouv.fr/avis/json/"

api = requests.get(url)

cert_avis = api.json()[-50:]
cert_avis = sorted(cert_avis, key=lambda x: x['last_revision_date'], reverse=True) ## récupère les 50 derniers avis du CERT-FR dans l'ordre décroissant de date de révision

for avis in cert_avis:
    avis['last_revision_date'] = dt.datetime.fromisoformat(avis['last_revision_date']).strftime('%d/%m/%Y')  ## formatage de la date de révision pour l'affichage

@app.route("/")
def render_main_page():
    return render_template("index.html", avis=cert_avis)