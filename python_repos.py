import requests

# Make an API call and store the response
url = 'https://api.github.com/search/repositories?q=languages:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)