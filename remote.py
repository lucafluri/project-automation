import sys
import os
from github import Github
import json

#load token
config = open("./config.json")
file = json.load(config)
token = file["token"]
path = file["path"] 

foldername = str(sys.argv[1])
# path = os.environ.get('mp')         # add projects dirctory to the env vars
# token = os.environ.get('gt')        # add github token to the env vars
_dir = path + '/' + foldername

githubOnly = len(sys.argv) > 2 and sys.argv[2] == "g"

# print(githubOnly)

g = Github(token)
user = g.get_user()
login = user.login
repo = user.create_repo(foldername, private=True)

title = f'# {repo.name}'


if not githubOnly:

    commands = [f'echo {title} >> README.md',
                'git init',
                f'git remote add origin https://github.com/{login}/{foldername}.git',
                'git add .',
                'git commit -m "Initial commit"',
                'git push -u origin master']

    os.mkdir(_dir)
    os.chdir(_dir)

    for c in commands:
        os.system(c)

    print()
    print(f'{foldername} created locally and on Github:')
    print(f'https://github.com/{login}/{foldername}.git')
    os.system('code .')

else:
    commands = [f'git remote add origin https://github.com/{login}/{foldername}.git',
                'git push -u origin master']

    os.chdir(_dir)

    for c in commands:
        os.system(c)

    print()
    print(f'{foldername} created and pushed on Github:')
    print(f'https://github.com/{login}/{foldername}.git')