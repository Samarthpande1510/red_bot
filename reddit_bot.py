import requests
from datetime import datetime

# 1. Use the live Reddit URL with .json at the end
url = "https://www.reddit.com/r/cats/new.json"

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
}

try:
    # 3. Fetch the data
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()

    # 4. Navigate the Reddit JSON structure: data -> children -> data
    posts = data['data']['children']

    for p in posts:
        post = p['data']
        title = post['title']
        score = post['score']
        author = post['author']
        
        # Convert the 'created_utc' to a readable 2026 date
        created = datetime.fromtimestamp(post['created_utc']).strftime('%Y-%m-%d %H:%M')

        print(f"[{created}] [{score}] {title} by u/{author}")

except Exception as e:
    print(f"Error: {e}")