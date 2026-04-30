import json
import urllib.request

with open('/tmp/mmc_brief.txt', 'r') as f:
    content = f.read()

data = json.dumps({
    'token': 'mmc-routines-2026',
    'docId': '1vfxZh6PCDjS7AIa595QSJ5Tn_qKmxeIfojU6uLOb77c',
    'content': content
}).encode()

url = 'https://script.google.com/macros/s/AKfycbzg4JAUEJE94-jxV9hkIN7fiG_pSGyaW5YyaBAEfXbbIXZ3ZhK9jvQRhDSZtsAYh9o_TQ/exec'


req = urllib.request.Request(
    url,
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
