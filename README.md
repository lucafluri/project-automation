### pre-setup:
Create ./config.json in project dir that contains the following. Must be kept Secret!
```json
{
    "token": "GITHUB_API_TOKEN",
    "path": "PATH_TO_PROJECTS_DIR"
}
```

### setup: 
```bash
pip install -r requirements.txt
```

### Usage:
```bash
Command to run the program type

'create <project_name>'       - Creates local and remote repo
'create <project_name> l'     - for just locally
'create <project_name> g'     - for just pushing local repo to new GitHub repo
```
