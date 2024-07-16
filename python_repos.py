import requests

# Make an API call and store the response
url = 'https://api.github.com/search/repositories?q=languages:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# Store API response in a variable
response_dict = r.json()

# Process results.
#print(response_dict.keys())

print("Total repositories:", response_dict['total_count'])

# Explore information about repositories.
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

# Examine the first repository
#repo_dicts = repo_dicts[1]

print("\nSelected information about each repository")
for repo_dict in repo_dicts:
    print("Name:", repo_dict['name'])
    print("Owner:", repo_dict['owner']['login'])
    print("Stars:",repo_dict['stargazers_count'])
    print("Repository URL:", repo_dict['html_url'])
    print("Created", repo_dict['created_at'])
    print("Updated:", repo_dict['updated_at'])
    
    description = repo_dict['description']
    if description:  # Check if description is not None
        print("Description:\n", description[:500] + "...")
    else:
        print("Description:\n None")
    print("\n\n")

# print("\nKeys:", len(repo_dicts))
# for key in repo_dicts.keys():
#    print(key)