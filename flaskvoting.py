from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "AIzaSyAUFLMdWmt-p5IlHPuXAsdI_JWTHL-XY-U"  # Replace with your actual API key
BASE_URL = "https://www.googleapis.com/civicinfo/v2/representatives"

@app.route('/')
def home():
    return render_template('votingweb.html')  # Change to your HTML file name

@app.route('/get_representatives', methods=['POST'])
def get_representatives():
    data = request.get_json()  # Use get_json() to receive JSON data
    address = data['address']
    url = f"{BASE_URL}?address={address}&key={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    else:
        return jsonify({'error': 'Unable to fetch data'})

if __name__ == '__main__':
    app.run(debug=True)