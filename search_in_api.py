import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl
import jmespath

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def main():
    '''
    NoneType -> NoneType
    Launch the module
    '''
    print('')

    acct = input('Enter Twitter Account: ')
    inf = input('Enter key of the dict: ')

    if (len(acct) < 1):
        break

    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '5'})
    connection = urllib.request.urlopen(url, context = ctx)
    data = connection.read().decode()

    js = json.loads(data)
    res = jmespath.search('users'.*.inf, js)
    result = json.dumps(res, indent = 4, ensure_ascii = False)
    print(result)

    headers = dict(connection.getheaders())
    print('Remaining', headers['x-rate-limit-remaining'])