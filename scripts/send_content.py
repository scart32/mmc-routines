import json
import urllib.request

with open('/tmp/mmc_content.txt', 'r') as f:
    content = f.read()

data = json.dumps({
    'token': 'mmc-routines-2026',
    'docId': '19i5h8QGaAm5vrpUi3bVfJOECn8F9mmXwfxC6fhrE-v4',
    'content': content
}).encode()

req = urllib.request.Request(
    'https://script.google.com/macros/s/AKfycbzJQDq-P9qif_nbw6vHulMJjb__AD0lVLhhKN3ZCltIx5zvG1JaOY2CE_TXKpYrQz8OzA/exec',
    data=data,
    headers={'Content-Type': 'application/json'},
    method='POST'
)

try:
    resp = urllib.request.urlopen(req, timeout=30)
    print(resp.read().decode())
except urllib.error.HTTPError as e:
    body = e.read().decode()
    print(f'HTTP {e.code}: {body}')
except Exception as e:
    print(f'Error: {e}')
