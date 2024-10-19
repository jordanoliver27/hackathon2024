from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "AIzaSyAUFLMdWmt-p5IlHPuXAsdI_JWTHL-XY-U"  # Replace with your actual API key
BASE_URL_REP = "https://www.googleapis.com/civicinfo/v2/representatives"
BASE_URL_ELEC = "https://www.googleapis.com/civicinfo/v2/elections"

@app.route('/')
def home():
    return render_template('votingweb.html')  # Change to your HTML file name

@app.route('/get_info', methods=['POST'])
def get_info():
    data = request.get_json()  # Use get_json() to receive JSON data
    address = data['address']
    
    # Get representatives
    rep_url = f"{BASE_URL_REP}?address={address}&key={API_KEY}"
    rep_response = requests.get(rep_url)

    # Get elections
    elec_response = requests.get(BASE_URL_ELEC + '?key=' + API_KEY)

    if rep_response.status_code == 200 and elec_response.status_code == 200:
        rep_data = rep_response.json()
        elec_data = elec_response.json()

        # Process representatives
        officials = rep_data.get('officials', [])
        results = []

        if officials:
            for official in officials:
                official_info = {
                    'name': official.get('name'),
                    'party': official.get('party'),
                    'phone': official.get('phones', ['No phone available'])[0],  # Default message if no phone is available
                    'urls': official.get('urls', [])
                }
                results.append(official_info)

        # Process elections
        elections = elec_data.get('elections', [])

        return jsonify({'officials': results, 'elections': elections})
    else:
        return jsonify({'error': 'Unable to fetch data'})

if __name__ == '__main__':
    app.run(debug=True)
