import json
import urllib.request

url = 'https://script.google.com/macros/s/AKfycbzg4JAUEJE94-jxV9hkIN7fiG_pSGyaW5YyaBAEfXbbIXZ3ZhK9jvQRhDSZtsAYh9o_TQ/exec'

data = json.dumps({
    'token': 'mmc-routines-2026',
    'action': 'read_doc',
    'docId': '1vfxZh6PCDjS7AIa595QSJ5Tn_qKmxeIfojU6uLOb77c'
}).encode()

req = urllib.request.Request(
    url,
    data=data,
    headers={'Content-Type': 'application/json'},
    method='POST'
)

try:
    resp = urllib.request.urlopen(req, timeout=30)
    result = json.loads(resp.read().decode())
    if result.get('success'):
        print(result.get('content', ''))
    else:
        print(f'Error: {result.get("error", "Unknown error")}')
except urllib.error.HTTPError as e:
    body = e.read().decode()
    print(f'HTTP {e.code}: {body}')
except Exception as e:
    print(f'Error: {e}')
