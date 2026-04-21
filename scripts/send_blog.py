import json
import urllib.request
import sys

with open('/tmp/mmc_blog.json', 'r') as f:
    post_data = f.read()

try:
    post = json.loads(post_data)
except json.JSONDecodeError as e:
    print(f'Error: Invalid JSON — {e}')
    sys.exit(1)

post['token'] = 'mmc-routines-2026'
post['action'] = 'publish_blog'

data = json.dumps(post).encode()

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
