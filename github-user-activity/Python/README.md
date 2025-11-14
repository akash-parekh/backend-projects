## Github User Activity

Use GitHub API to fetch user activity and display it in the terminal.

In this project, you will build a simple command line interface (CLI) to fetch the recent activity of a GitHub user and display it in the terminal. This project will help you practice your programming skills, including working with APIs, handling JSON data, and building a simple CLI application.

This project is part of [backend project challenges](https://roadmap.sh/projects/github-user-activity.)

## Project Structure

github_user_activity/
│
├── github_activity/
│ ├── **init**.py
│ ├── cli.py # CLI entry point (argument parsing + controller)
│ ├── api.py # GitHub API HTTP requests (built-in urllib)
│ ├── parser.py # Logic to parse/convert GitHub events → readable output
│ ├── utils.py # Helpers (time formatting, errors, constants)
│
├── tests/
│ ├── test_cli.py
│ ├── test_api.py
│ ├── test_parser.py
│
├── README.md
├── pyproject.toml # Package metadata + dependencies (none external)
├── .gitignore
└── main.py # CLI launcher (simple)
