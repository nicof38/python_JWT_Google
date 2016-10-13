from oauth2client.service_account import ServiceAccountCredentials
import json
from urllib.request import urlopen
from urllib.parse import urlencode

# Settings
json_key_file = 'my_google_credential.json'
scope = ['https://mail.google.com']


# Load the private key associated with the Google service account
with open(json_key_file) as json_file:
    json_data = json.load(json_file)

# Get and sign JWT
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_key_file, scope)
jwt_complete = credentials._generate_assertion()

# Get token from server
data = {'grant_type': 'urn:ietf:params:oauth:grant-type:jwt-bearer', 
    'assertion': jwt_complete}
with urlopen("https://accounts.google.com/o/oauth2/token", urlencode(data).encode('ascii')) as response:
	html = response.read()
	print(html)
