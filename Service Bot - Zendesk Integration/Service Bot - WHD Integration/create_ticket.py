import json
import urllib
import requests

data = json.load(open('ticket.json'))

url = "http://localhost:8081/helpdesk/WebObjects/Helpdesk.woa//ra/Tickets/1/?username=admin&apiKey=FbRiFjLofT3cnjO4QhlvtHARHehx2UmtbHEHIF2X"
url = "http://localhost:8081/helpdesk/WebObjects/Helpdesk.woa\/ra/Tickets/1/?username=admin&?apiKey=FbRiFjLofT3cnjO4QhlvtHARHehx2UmtbHEHIF2X"
#response = urllib.urlopen(url, json.dumps(data))

apiKey="FbRiFjLofT3cnjO4QhlvtHARHehx2UmtbHEHIF2X"

def submitJsonToWhd(data):
    WhdUrl = 'http://localhost:8081/helpdesk/WebObjects/Helpdesk.woa/ra/Tickets/?username=admin&password=admin'
    headers = {'content-type': 'application/json'}

    req = requests.post(url=WhdUrl, data=data, headers=headers)

    print(req.text)

data = json.dumps(data)
submitJsonToWhd(data)

