import requests

from operator import itemgetter

# Make and API call and store response
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)

# process information for each submission
submission_ids = r.json
submission_dict = []
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission
    url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json')
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json

    submission_dict = {
        'title' : response_dic['title'],
        'link' : 'https://news.hackerio.com/item?id=' + str(submission_id),
        'comments': response_dict.get('descendants',0)
    }
submission_dicts = stored(submission_dicts, key=itemgetter('comments'), reversed = True)

for submission_dist in submission_dicts:
    print("\Title:", submission_dict['title'])
    print("Discussion link:", submission_dict['link'])
    print("Comments:", submission_dict['comments'])