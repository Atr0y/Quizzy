import requests

PARAMETERS = {
    "amount": 10,
    "type": "boolean"
}
response = requests.get('https://opentdb.com/api.php', params=PARAMETERS)
data = response.json()
question_data = data['results']
