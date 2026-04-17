import json
import subprocess
import sys

# Read the blog post JSON written by the agent
with open('/tmp/mmc_blog.json', 'r') as f:
    post_data = f.read()

# Validate JSON
try:
    post = json.loads(post_data)
except json.JSONDecodeError as e:
    print(f"Error: Invalid JSON — {e}")
    sys.exit(1)

# Add auth and action
post['token'] = 'mmc-routines-2026'
post['action'] = 'publish_blog'

payload = json.dumps(post)

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
