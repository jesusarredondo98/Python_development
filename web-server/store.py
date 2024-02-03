import requests
import pandas as pd
import json

def get_categories():
    r = requests.get("https://api.escuelajs.co/api/v1/categories")
    categories = json.loads(r.text) #Obtenemos el resultado en formato json
    return pd.DataFrame(categories).to_html()