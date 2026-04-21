import json
import urllib.request

with open('/tmp/mmc_content.txt', 'r') as f:
    content = f.read()

data = json.dumps({
    'token': 'mmc-routines-2026',
    'docId': '1vfxZh6PCDjS7AIa595QSJ5Tn_qKmxeIfojU6uLOb77c',
    'content': content
}).encode()

req = urllib.request.Request(
    'https://script.google.com/macros/s/AKfycbzJQDq-P9qif_nbw6vHulMJjb__AD0lVLhhKN3ZCltIx5zvG1JaOY2CE_TXKpYrQz8OzA/exec',
    data=data,
    headers={'Content-Type': 'application/json'},
    method='POST'
)

try:
    resp = urllib.request.urlopen(req)
    print(resp.read().decode())
except Exception as e:
    print(f'Error: {e}')
