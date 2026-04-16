import json
import subprocess

with open('/tmp/mmc_brief.txt', 'r') as f:
    content = f.read()

payload = json.dumps({
    'token': 'mmc-routines-2026',
    'docId': '19i5h8QGaAm5vrpUi3bVfJOECn8F9mmXwfxC6fhrE-v4',
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
