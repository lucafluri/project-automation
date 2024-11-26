@echo off

set fn=%1
set flag=%2
cd /d %~dp0

If "%1"=="" (
    echo "No project name provided. Listing all projects..."
    python list_projects.py
    exit /b 0
) 

If "%1"=="-h" (
    echo "Usage: pj <project_name> [l|g]"
    echo "  -h : Display this help message"
    echo "  <project_name> : Name of the project to create"
    echo "  l : Create a local project"
    echo "  g : Create a private GitHub repository (default)"
    echo "  No arguments : List all existing projects"
    exit /b 0
) 

if "%2"=="" (
    python remote.py %fn% g
) else (
    if "%2"=="l" (
        python local.py %fn%
    )
    if "%2"=="g" (
        python remote.py %fn% g
    )
)
