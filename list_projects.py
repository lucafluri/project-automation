import os
import json
import msvcrt
import subprocess

# Load configuration
def load_config(config_path):
    with open(config_path, 'r') as file:
        return json.load(file)

# List all projects in the specified directory
def list_projects(projects_path):
    return [d for d in os.listdir(projects_path) if os.path.isdir(os.path.join(projects_path, d))]

# Display projects with cursor and pagination
def display_projects(projects, index, page, page_size, projects_path):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Project List:")
    print(f"Path: {projects_path}\n")
    start = page * page_size
    end = start + page_size
    for i in range(start, min(end, len(projects))):
        cursor = '->' if i == index else '  '
        print(f"{cursor} {projects[i]}")
    print(f"\nPage {page + 1}/{(len(projects) - 1) // page_size + 1}")
    print("Use 'w/s' or arrow keys to navigate, 'Enter' to open, 'q' to quit, 'f' to fuzzy search, 'p' to switch paths, 'n' to create a new project.")

# Simple fuzzy search implementation
def fuzzy_search(projects, query):
    query = query.lower()
    results = [proj for proj in projects if query in proj.lower()]
    return results

# Navigate through search results
def navigate_results(projects_path, results):
    index = 0
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Search Results:")
        print(f"Path: {projects_path}\n")
        for i, result in enumerate(results):
            cursor = '->' if i == index else '  '
            print(f"{cursor} {result}")
        print("Use 'w/s' or arrow keys to navigate, 'Enter' to open, 'q' to quit.")
        key = msvcrt.getch()
        if key in (b'q', b'Q'):
            break
        elif key in (b'\r', b'\n'):  # Enter key
            os.startfile(os.path.join(projects_path, results[index]))
            return True
        elif key in (b'w', b'W', b'H'):  # 'w' or up arrow
            index = (index - 1) % len(results)
        elif key in (b's', b'S', b'P'):  # 's' or down arrow
            index = (index + 1) % len(results)
    return False

# Create a new project
def create_new_project(projects_path):
    project_name = input("Enter the new project name: ")
    print("Choose project type: (l)ocal or (r)emote")
    project_type = input("Enter 'l' or 'r': ").lower()
    if project_type == 'l':
        subprocess.run(['python', 'local.py', project_name, projects_path], cwd=os.getcwd())
    elif project_type == 'r':
        subprocess.run(['python', 'remote.py', project_name, projects_path], cwd=os.getcwd())
    else:
        print("Invalid option. Returning to project list.")

# Main function
def main():
    config = load_config('config.json')
    project_paths = config.get('paths', ['G:/Projects'])
    current_path_index = 0
    
    while True:
        projects_path = project_paths[current_path_index]
        projects = list_projects(projects_path)
        if not projects:
            print("No projects found.")
            return
        
        index = 0
        page = 0
        page_size = 10
        while True:
            display_projects(projects, index, page, page_size, projects_path)
            key = msvcrt.getch()
            if key in (b'q', b'Q'):
                return
            elif key in (b'\r', b'\n'):  # Enter key
                os.startfile(os.path.join(projects_path, projects[index]))
                return
            elif key in (b'w', b'W', b'H'):  # 'w' or up arrow
                index = (index - 1) % len(projects)
                if index < page * page_size:
                    page = (page - 1) % ((len(projects) - 1) // page_size + 1)
            elif key in (b's', b'S', b'P'):  # 's' or down arrow
                index = (index + 1) % len(projects)
                if index >= (page + 1) * page_size:
                    page = (page + 1) % ((len(projects) - 1) // page_size + 1)
            elif key in (b'a', b'A', b'K'):  # 'a' or left arrow
                page = (page - 1) % ((len(projects) - 1) // page_size + 1)
                index = page * page_size
            elif key in (b'd', b'D', b'M'):  # 'd' or right arrow
                page = (page + 1) % ((len(projects) - 1) // page_size + 1)
                index = page * page_size
            elif key in (b'f', b'F'):  # 'f' for fuzzy search
                query = input("Enter search query: ")
                results = fuzzy_search(projects, query)
                if results:
                    if navigate_results(projects_path, results):
                        return
                else:
                    print("No matches found.")
                    input("\nPress any key to return to the list...")
            elif key in (b'p', b'P'):  # 'p' to switch paths
                current_path_index = (current_path_index + 1) % len(project_paths)
                break
            elif key in (b'n', b'N'):  # 'n' to create a new project
                create_new_project(projects_path)
                projects = list_projects(projects_path)
                index = 0
                page = 0

if __name__ == "__main__":
    main()
