from typing import Optional
from github import Github, Repository
from github.GithubException import GithubException
import logging
import os
from dotenv import load_dotenv

class GitHubClient:
    """Handles GitHub API interactions."""
    
    def __init__(self):
        load_dotenv()
        self.token = os.getenv('GITHUB_TOKEN')
        self.repo_name = os.getenv('GITHUB_REPOSITORY')
        
        if not self.token or not self.repo_name:
            raise ValueError("GitHub token and repository name are required")
            
        self.github = Github(self.token)
        self.repo: Optional[Repository] = None
        self._connect_to_repo()
        
    def _connect_to_repo(self) -> None:
        """Establishes connection to the GitHub repository."""
        try:
            self.repo = self.github.get_repo(self.repo_name)
        except GithubException as e:
            logging.error(f"Failed to connect to repository: {e}")
            raise
            
    def create_issue(self, title: str, body: str, labels: list[str]) -> None:
        """Creates a new issue in the repository."""
        try:
            self.repo.create_issue(
                title=title,
                body=body,
                labels=labels
            )
        except GithubException as e:
            logging.error(f"Failed to create issue: {e}")
            raise 