## 2. Authenticating with the API ##

# Reddit Project
headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
params  = {"t": "day"}
response = requests.get("https://oauth.reddit.com/r/python/top", headers = headers, params = params)
python_top = response.json()

## 3. Getting the Most Upvoted Post ##

python_top_articles = python_top["data"]["children"]

most_upvoted = ""
most_upvotes = 0

for each in python_top_articles:
    if each["data"]["ups"] >= most_upvotes:
        most_upvoted = each["data"]["id"]
        most_upvotes = each["data"]["ups"]


## 4. Getting Post Comments ##

comments = requests.get("https://oauth.reddit.com/r/python/comments/4b7w9u", headers = headers).json()

## 5. Getting the Most Upvoted Comment ##

comments_list = comments[1]["data"]["children"]

most_upvoted_comment = ""
most_upvotes = 0

for each in comments_list:
    if each["data"]["ups"] >= most_upvotes:
        most_upvoted_comment = each["data"]["id"]
        most_upvotes = each["data"]["ups"]

## 6. Upvoting a Comment ##

payload = {"dir": 1, "id": "d16y4ry"}
headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
respons = requests.post("https://oauth.reddit.com/api/vote", json = payload, headers = headers)
status  = respons.status_code


