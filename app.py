import requests
from flask import Flask, jsonify
from flask_cors import CORS
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False

URL = 'https://www.diyanet.gov.tr/tr-TR'


def fetch_data():
    body = requests.get(URL)
    soup = BeautifulSoup(body.text, 'html.parser')
    ayet = soup.find('div', {'class': 'ayet'}).find(
        'p', {'class': 'ahd-content-text'}).text.strip()
    hadis = soup.find('div', {'class': 'hadis'}).find(
        'p', {'class': 'ahd-content-text'}).text.strip()
    dua = soup.find('div', {'class': 'dua'}).find(
        'p', {'class': 'ahd-content-text'}).text.strip()
    data = {'ayet': ayet, 'dua': dua, 'hadis': hadis}
    return data


@app.route('/api/diyanet')
def diyanet():
    diyanet_data = fetch_data()
    return jsonify(diyanet_data)


app.run(host='0.0.0.0', port=80)
