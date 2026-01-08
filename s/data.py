import requests
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import datetime

load_dotenv()

API_KEY = os.getenv("GOOGLE_SHEET_API")

def fetch_data():
    res = requests.get(f'https://script.google.com/macros/s/{API_KEY}/exec')
    data = res.json()
    if data['status'] == "success":
        titles = ""
        for x in data['data']:
            titles = f"{x['title']};\n"
        return titles
    return 'No existing blog'

def save_data(content):
    soup = BeautifulSoup(f"""{content['content']}""", 'html.parser')
    img = soup.find_all('img')[0]
    image = img.get('src')
    data = {
        "title": content['title'],
        "description": content['meta_description'],
        "image": image,
        "createdAt": datetime.datetime.now().isoformat()
    }
    req = requests.post(f'https://script.google.com/macros/s/{API_KEY}/exec', json=data)
    # if res['status'] == "success":
    #    print("Data saved to excel successfully")
    # print("failed to save data to excel")
    print(req.text)

