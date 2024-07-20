import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightStyle as LS
# Make an API call and store the response
url = 'https://api.github.com/search/repositories?q=languages:python&sort=stars'
r = requests.get(url)
print("\nStatus code:", r.status_code)

# Store API response in a variable
response_dict = r.json()

# Process results.
#print(response_dict.keys())

print("Total repositories:", response_dict['total_count'])

# Explore information about repositories.
repo_dicts = response_dict['items']

colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF', '#00FFFF', '#FFA500', '#800080', '#008080', '#800000'] # Add as many colors as needed


names, stars, plot_dicts = [], [], []
for i, repo_dict in enumerate(repo_dicts):
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict["name"],
        'xlink': repo_dict['html_url'],
        'color': colors[i % len(colors)]
    }
    plot_dicts.append(plot_dict)




# Make visualization.
my_style = LS(base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False, tooltip_fancy_mode=True, truncate_label=15)
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names

chart.add('', plot_dicts)

chart.render_to_file('python_repo.svg')





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
    
    description = repo_dict.get('description', 'None')
    # Check if description is not None
    if description and len(description) > 500:  
        description = description[:400] + "..."

    print("Description:\n", description, "\n\n")


