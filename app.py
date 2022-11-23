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

    ayet_info = soup.find('div', {'class': 'ayet'}).find_next_sibling("div").find(
        'p', {'class': 'alt-sure-title'}).text.strip()

    dua = soup.find('div', {'class': 'dua'}).find(
        'p', {'class': 'ahd-content-text'}).text.strip()

    dua_info = soup.find('div', {'class': 'dua'}).find(
        'p', {'class': 'alt-sure-title'}).text.strip()

    hadis = soup.find('div', {'class': 'hadis'}).find(
        'p', {'class': 'ahd-content-text'}).text.strip()

    hadis_info = soup.find('div', {'class': 'hadis'}).find_next_sibling("div").find(
        'p', {'class': 'alt-sure-title'}).text.strip()

    data = {'ayet': ayet, 'ayet_info': ayet_info, 'dua': dua, 'dua_info': dua_info, 'hadis': hadis, 'hadis_info': hadis_info}
    return data


@app.route('/api/diyanet')
def diyanet():
    diyanet_data = fetch_data()
    return jsonify(diyanet_data)


app.run(host='0.0.0.0', port=80)
