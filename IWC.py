from flask import Flask, jsonify
from time import sleep
import requests

# Configuration variables
URL = "" # Enter sublink/URL
UPDATE_INTERVAL = 5 * 60  # Delay
shost, sport = "127.0.0.1", 5000
app = Flask(__name__)

# Global variable to store cached data
cached_data = None

def fetch_url(url):
  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for non-200 status codes
    return response.content
  except requests.exceptions.RequestException as e:
    print(f"Error fetching URL: {e}")
    return None

def update_cache():
  global cached_data
  data = fetch_url(URL)
  if data:
    cached_data = data

@app.route("/")
def get_cached_data():
  if cached_data:
    return jsonify(data=cached_data.decode())  # Decode bytes to string
  else:
    # return jsonify(error="No data available yet. Try again later."), 503
    return "vmess://ew0KICAidiI6ICIyIiwNCiAgInBzIjogIkNhY2hpbmcgRGF0YSAuLi4iLA0KICAiYWRkIjogIklXQy5ORVQiLA0KICAicG9ydCI6ICIxIiwNCiAgImlkIjogIjEiLA0KICAiYWlkIjogIjAiLA0KICAic2N5IjogImF1dG8iLA0KICAibmV0IjogInRjcCIsDQogICJ0eXBlIjogIm5vbmUiLA0KICAiaG9zdCI6ICIiLA0KICAicGF0aCI6ICIiLA0KICAidGxzIjogIiIsDQogICJzbmkiOiAiIiwNCiAgImFscG4iOiAiIg0KfQ== vmess://ew0KICAidiI6ICIyIiwNCiAgInBzIjogIlVwZGF0ZSBpbiBhIGZldyBzZXhvbmRzIiwNCiAgImFkZCI6ICJJV0MuTkVUIiwNCiAgInBvcnQiOiAiMSIsDQogICJpZCI6ICIxIiwNCiAgImFpZCI6ICIwIiwNCiAgInNjeSI6ICJhdXRvIiwNCiAgIm5ldCI6ICJ0Y3AiLA0KICAidHlwZSI6ICJub25lIiwNCiAgImhvc3QiOiAiIiwNCiAgInBhdGgiOiAiIiwNCiAgInRscyI6ICIiLA0KICAic25pIjogIiIsDQogICJhbHBuIjogIiINCn0="

if __name__ == "__main__":
  from threading import Thread
  thread = Thread(target=update_cache)
  thread.daemon = True  # Set thread as daemon to avoid blocking exit
  thread.start()
  app.run(debug=True, port=sport, host=shost)
