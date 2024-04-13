import requests as req
import pandas as pd

url = "https://api.themoviedb.org/3/authentication"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer"
}

response = requests.get(url, headers=headers)

print(response.text)