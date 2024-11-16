# GitHub User Story Creator

This project automates the creation of GitHub issues for a blog project's user stories. It leverages the GitHub API to streamline the process of populating user stories as issues in a GitHub repository.

## Project Overview

The GitHub User Story Creator is designed to read user stories from a YAML configuration file and create corresponding issues in a specified GitHub repository. This automation helps in managing project tasks efficiently by ensuring that all user stories are tracked as issues.

## Features

- **YAML Story Parsing**: Reads and validates user stories from a YAML file.
- **GitHub API Integration**: Uses PyGithub to interact with the GitHub API.
- **Environment Variable Management**: Manages sensitive information like API tokens using environment variables.
- **Error Handling and Logging**: Implements robust error handling and logging for better debugging and monitoring.
- **Type Hinting**: Utilizes type hints for improved code clarity and maintainability.

## Project Structure

## Project Structure

```
GitHubUserStoryCreator/
    ├── .env                    # Environment variables
    ├── requirements.txt        # Project dependencies
    ├── stories.yaml            # User story configurations
    ├── src/
    │   ├── __init__.py
    │   ├── github_client.py    # GitHub API client class
    │   ├── story_parser.py     # YAML parsing and validation
    │   ├── issue_creator.py    # Issue creation logic
    │   └── main.py             # Script entry point
```


## How It Works

1. **Setup**: Configure your environment by setting up a virtual environment and installing dependencies listed in `requirements.txt`. Populate the `.env` file with your GitHub API token.

2. **YAML Parsing**: The `story_parser.py` module reads and validates user stories from `stories.yaml`. It ensures all required fields are present and formats the stories for GitHub. Take your user stories and give them to an llm along with the template.yaml file. Then add the output to the stories.yaml file.

3. **Issue Creation**: The `issue_creator.py` module takes the formatted stories and creates issues in the specified GitHub repository using the GitHub API.

4. **Execution**: Run the `main.py` script to execute the entire process, which combines all components and provides progress feedback.

## Usage

1. **Clone the Repository**: 
   ```bash
   git clone https://github.com/GuyMitchy/github-user-story-populator.git
   cd github-user-story-populator
   ```

2. **Set Up Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**: 
   - Create a `.env` file in the root directory.
   - Add your GitHub API token:
     ```
     GITHUB_TOKEN=your_github_token
     ```
   - Add your GitHub repository name:
     ```
     GITHUB_REPOSITORY=your_github_repository_name
     ```

4. **Run the Script**:
   ```bash
   python main.py
   ```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

