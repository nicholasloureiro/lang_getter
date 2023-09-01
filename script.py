import requests as r
import pandas as pd

access_token = 'insert you api token here'
headers = {'x-GitHub-Api-Version': '2022-11-28', 'Authorization':'Bearer ' + access_token}
api_base_url = 'https://api.github.com'
owner = 'oracle'
url = f'{api_base_url}/users/{owner}/repos'


repos_list = []
for page_num in range(1,10):
    try:
        url_page = f'{url}?page={page_num}'
        response = r.get(url_page,headers=headers)
        repos_list.append(response.json())
    except:
        repos_list.append(None)


print(repos_list[1][2]['language'])

repos_name = []
for page in repos_list:
    for repo in page:
        repos_name.append(repo['name'])
#print(repos_name)

repos_lang = []
for page in repos_list:
    for repo in page:
        repos_lang.append(repo['language'])
df = pd.DataFrame()
df['name'] = repos_name
df['language'] = repos_lang
print(df['language'].dropna().mode())


