# contributors.py
# create a Personal GitHub API token
# add the line GITHUB_API_TOKEN=<your token here> to the .env file at the root of the project

import requests
import time
import re
import os
import dotenv

dotenv.read_dotenv()

#TODO
# Add people that are assigned issues?

comments_url = 'https://api.github.com/repos/codefordurham/school-navigator/issues/comments?page={page}'
user_url = 'https://api.github.com/users/{user}'
token = os.environ['GITHUB_API_TOKEN']

def main():
    page = 1
    headers = {'Authorization': 'token {token}'.format(token=token)}
    users = set()
    ignored_users = set(['coveralls', 'github'])
    while 1:
        comments_page_url = comments_url.format(page=str(page))
        r = requests.get(comments_page_url, headers=headers)
        if r.status_code != 200:
            print(r.status_code)
            print(r.body)
            return
        if not r.json():
            #last page returns [ ]
            break
        for comment in r.json():
            users.add(comment['user']['login'])
            for m in re.findall(r'@\w+', comment['body']):
                users.add(m[1:])
        page += 1
        time.sleep(.25)
    users.difference_update(ignored_users)
    for u in users:
        r = requests.get(user_url.format(user=u), headers=headers)
        if r.status_code != 200:
            name = ''
        else:
            name = r.json()['name']
        if name:
            print('{name} ({username})'.format(name=name, username=u))
        else:
            print(u)

if __name__ == "__main__":
    main()
