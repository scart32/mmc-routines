import json
import subprocess

with open('/tmp/mmc_content.txt', 'r') as f:
    content = f.read()

payload = json.dumps({
    'token': 'mmc-routines-2026',
    'docId': '1vfxZh6PCDjS7AIa595QSJ5Tn_qKmxeIfojU6uLOb77c',
    'content': content
})

result = subprocess.run(
    [
        'curl', '-sL', '-X', 'POST',
        '-H', 'Content-Type: application/json',
        '-d', payload,
        'https://script.google.com/macros/s/AKfycbzJQDq-P9qif_nbw6vHulMJjb__AD0lVLhhKN3ZCltIx5zvG1JaOY2CE_TXKpYrQz8OzA/exec'
    ],
    capture_output=True,
    text=True
)

print(result.stdout)
if result.returncode != 0:
    print('curl error:', result.stderr)
