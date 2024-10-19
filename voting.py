import requests

# Define the API key and base URL
API_KEY = "AIzaSyAUFLMdWmt-p5IlHPuXAsdI_JWTHL-XY-U"
BASE_URL = "https://www.googleapis.com/civicinfo/v2/representatives"

# Take user input for the address
address = input("Please enter the address (e.g., 1600 Pennsylvania Ave NW, Washington, DC): ")

# Create a request URL
url = f"{BASE_URL}?address={address}&key={API_KEY}"

# Make the request
response = requests.get(url)

# Parse the response
if response.status_code == 200:
    data = response.json()
    print(data)  # Print or process the JSON data
    
    officials = data.get('officials', [])
    if officials:
        for official in officials:
            name = official.get('name')
            party = official.get('party')
            phone = official.get('phones', ['No phone available'])[0]  # Default message if no phone is available
            urls = official.get('urls', [])
            print(f"Name: {name}")
            print(f"Party: {party}")
            print(f"Phone: {phone}")
            print("URLs:")
            for url in urls:
                print(f" - {url}")
            print("\n")
    else:
        print("No officials found for this address.")
else:
    print(f"Error: {response.status_code}")
