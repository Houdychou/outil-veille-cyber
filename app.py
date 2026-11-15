from flask import *
import requests
import datetime as dt
import feedparser

app = Flask(__name__)

url_avis = "https://cert.cyber.gouv.fr/avis/json/"
url_alertes = "https://cert.cyber.gouv.fr/alerte/json/"
rss_url = "https://www.bleepingcomputer.com/feed/"

feed = feedparser.parse(rss_url)

api_avis = requests.get(url_avis)
api_alertes = requests.get(url_alertes)

cert_avis = api_avis.json()[-50:]
cert_alertes = api_alertes.json()[-50:]

cert_avis = sorted(cert_avis, key=lambda x: x['last_revision_date'], reverse=True) ## récupère les 50 derniers avis du CERT-FR dans l'ordre décroissant de date de révision

cert_alertes = sorted(cert_alertes, key=lambda x: x['last_revision_date'], reverse=True) ## récupère les 50 dernières alertes du CERT-FR dans l'ordre décroissant de date de révision

for avis in cert_avis:
    date = dt.datetime.fromisoformat(avis['last_revision_date'])
    avis['date_tri'] = date.strftime('%Y-%m-%d')
    avis['last_revision_date'] = date.strftime('%d/%m/%Y')  ## formatage de la date de révision pour l'affichage

for alert in cert_alertes:
    date = dt.datetime.fromisoformat(alert['last_revision_date'])
    alert['date_tri'] = date.strftime('%Y-%m-%d')
    alert['last_revision_date'] = date.strftime('%d/%m/%Y')  ## formatage de la date de révision pour l'affichage

for entry in feed.entries:
    date = dt.datetime(*entry.published_parsed[:6])
    entry['date_tri'] = date.strftime('%Y-%m-%d')
    entry['date_fr'] = date.strftime('%d/%m/%Y')  ## même format de date que le CERT-FR pour l'affichage

@app.route("/")
def render_main_page():
    return render_template("index.html", avis=cert_avis, alertes=cert_alertes, feed=feed.entries)