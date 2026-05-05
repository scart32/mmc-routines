import requests

with open('/tmp/mmc_content.txt', 'r') as f:
    content = f.read()

payload = {
    'token': 'mmc-routines-2026',
    'action': 'append_doc',
    'docId': '19i5h8QGaAm5vrpUi3bVfJOECn8F9mmXwfxC6fhrE-v4',
    'content': content
}

url = 'https://script.google.com/macros/s/AKfycbzg4JAUEJE94-jxV9hkIN7fiG_pSGyaW5YyaBAEfXbbIXZ3ZhK9jvQRhDSZtsAYh9o_TQ/exec'

try:
    resp = requests.post(url, json=payload, timeout=30)
    print(resp.text)
except Exception as e:
    print(f'Error: {e}')
