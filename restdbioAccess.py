import requests
import json


def save_email_address(email_address):
    url = "https://geschaeftskonto-63c9.restdb.io/rest/emailadresses"

    payload = json.dumps( {"value": email_address} )
    headers = {
        'content-type': "application/json",
        'x-apikey': "4f8638adb04e2f50ea7ac21b82cc802fc6019",
        'cache-control': "no-cache"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)
