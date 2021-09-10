import os
import sys
import requests
import secrets
import string

def cls():
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')

def gen(length, email=False):
    final = ''
    final = final.join(secrets.choice(string.ascii_letters + string.digits) for x in range(length)).lower()

    if email == True:
        final = final + '@gmail.com'
    
    return final

cls()
print('Spotify Account Creator')
print('Don\'t put anything in if you want to use a random string.\n')

username = input('Username: ') or gen(10)
password = input('Password: ') or gen(15)
email = input('Email: ') or gen(15, True)

res = requests.post('https://spclient.wg.spotify.com/signup/public/v1/account', data={
    'birth_day': '1',
    'birth_month': '01',
    'birth_year': '1970',
    'collect_personal_info': 'undefined',
    'creation_flow': '',
    'creation_point': 'https://www.spotify.com/uk/',
    'displayname': username,
    'username': username,
    'gender': 'male',
    'iagree': '1',
    'key': 'a1e486e2729f46d6bb368d6b2bcda326',
    'platform': 'www',
    'referrer': 'https://www.spotify.com/uk/',
    'send-email': '0',
    'thirdpartyemail': '0',
    'email': email,
    'password': password,
    'password_repeat': password
}, headers={
    'accept': '*/*',
    'accept-language': 'en-uk,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sec-gpc': '1',
    'referer': 'https://www.spotify.com/',
    'referrer-policy': 'strict-origin-when-cross-origin'
}).json()

if res['status'] == 1:
    cls()
    print('Successfully created your account!\n')
    print(f'Username: {username}\nPassword: {password}\nEmail: {email}\n')
else:
    cls()
    for error in res['errors']:
        print(f"{error} - {res['errors'][error]}")