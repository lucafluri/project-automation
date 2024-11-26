import sys
import os
import json


config = open("./config.json")
file = json.load(config)
path = file["paths"][0] 

foldername = str(sys.argv[1])
# path = os.environ.get('mp')
custom_path = sys.argv[2] if len(sys.argv) > 2 else path
_dir = custom_path + '/' + foldername

try:
    os.mkdir(_dir)
    os.chdir(_dir)
    os.system('git init')
    os.system(f'echo "# {foldername}" > README.md')
    os.system('git add README.md')
    os.system('git commit -m "first commit"')


    print(f'{foldername} created locally')
    os.startfile(_dir)
    os.system('code .')


except:
    print("create <project_name> l")
