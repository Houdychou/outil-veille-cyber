from flask import *
import requests

app = Flask(__name__)

url = "https://cert.cyber.gouv.fr/avis/json/"

api = requests.get(url)

for i in range(5):
    avis = api.json()[i]
    print(avis["title"])
    print(avis["last_revision_date"])

@app.route("/")
def render_main_page():
    return render_template("index.html")