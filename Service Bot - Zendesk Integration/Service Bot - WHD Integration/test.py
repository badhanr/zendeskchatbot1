import json
import requests

id = '18'

# Package the data in a dictionary matching the expected JSON
js = json.load(open('ticket.json'))
#data = {"ticket": js}
data = {"ticket": {"priority": "urgent"}}
# Encode the data to create a JSON payload
payload = json.dumps(data)

# Set the request parameters
#url = 'https://servicebot.zendesk.com/api/v2/tickets.json'

url = 'https://servicebot.zendesk.com/api/v2/tickets/' + id + '.json'
user = 'rukshan4u4ever@gmail.com'
pwd = 'Rukhshan@1'
headers = {'content-type': 'application/json'}

# Do the HTTP post request
response = requests.put(url, data=payload, auth=(user, pwd), headers=headers)

# Check for HTTP codes other than 201 (Created)
if response.status_code != 201:
    print('Status:', response.status_code, 'Problem with the request. Exiting.')
    for i in range(0, 7):
        print(i)
    exit()

# Report success
print('Successfully created the ticket.')
print(response.text)

