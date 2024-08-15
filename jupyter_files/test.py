import requests
import json

valores = {
    'L_NO_ESPECIFICADO_E': 10,
    'L_POSPAGOC_E': 50,
    'L_PREPAGO_E': 40,
    'L_TOTAL_E': 50
}

url = 'http://localhost:9696/predict'
response = requests.post(url, json=valores)
print(response.json())