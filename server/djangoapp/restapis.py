# Uncomment the imports below before you add the function code
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")

def get_request(endpoint, **kwargs):
    params = ""
    if(kwargs):
        for key,value in kwargs.items():
            params=params+key+"="+str(value)+"&"

    request_url = backend_url+endpoint+"?"+params

    print("GET from {} ".format(request_url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as e:
        # If any error occurs
        print("Network exception occurred:", e)
        return {"error": "Network exception occurred"}

def analyze_review_sentiments(text):
    # Remove any special characters and encode the text for URL
    import urllib.parse
    encoded_text = urllib.parse.quote(text)
    request_url = sentiment_analyzer_url + "analyze/" + encoded_text
    
    print(f"Analyzing sentiment from {request_url}")
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        print(f"Sentiment response: {response.status_code}")
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"API returned status code {response.status_code}"}
    except Exception as err:
        print(f"Unexpected error: {err}, type: {type(err)}")
        return {"error": "Network exception occurred"}

def post_review(data_dict):
    request_url = backend_url + "/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        print(f"Status code: {response.status_code}")
        print(f"Response: {response.text}")
        return response.json()
    except Exception as e:
        print("Network exception occurred:", e)
        return {"error": "Network exception occurred"}