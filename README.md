### pre-setup:
Create `./config.json` in the project directory with the following content. This file must be kept secret!
```json
{
    "token": "GITHUB_API_TOKEN",
    "paths": [
        "PATH_TO_PROJECTS_DIR_1",
        "PATH_TO_PROJECTS_DIR_2"
    ]
}
```

### setup:
```bash
pip install -r requirements.txt
```

### Usage:
- **Project Listing and Navigation**:
  - Run `pj` with no arguments to list all projects.
  - Navigate using 'w/s' or arrow keys, 'Enter' to open, 'q' to quit, 'f' to fuzzy search, 'p' to switch directories, 'n' to create a new project.

- **Create a New Project**:
  - From the project list, press 'n' to create a new project.
  - Enter the project name and choose the type:
    - 'l' for local
    - 'r' for remote (GitHub)
  - The project will be created in the selected path.

- **Command Line**:
  - `pj <project_name>`: Creates both local and remote repositories.
  - `pj <project_name> l`: Creates a local repository only.
  - `pj <project_name> g`: Pushes the local repository to a new GitHub repository.

### Notes:
- Ensure Python and Git are installed and accessible in your PATH.
- `config.json` should contain valid paths and a GitHub token for remote operations.
