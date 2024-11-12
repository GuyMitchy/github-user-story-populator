from typing import List, Dict, Any
import logging
from src.github_client import GitHubClient
from src.story_parser import StoryParser

class IssueCreator:
    """Handles the creation of GitHub issues from parsed stories."""
    
    def __init__(self, yaml_path: str):
        self.github_client = GitHubClient()
        self.story_parser = StoryParser(yaml_path)
        
    def create_issues_from_stories(self) -> None:
        """
        Main method to create GitHub issues from all stories in the YAML file.
        """
        try:
            stories = self.story_parser.parse_stories()
            self._create_issues(stories)
            logging.info(f"Successfully created {len(stories)} issues")
        except Exception as e:
            logging.error(f"Failed to create issues: {e}")
            raise
            
    def _create_issues(self, stories: List[Dict[str, Any]]) -> None:
        """Creates GitHub issues from formatted stories."""
        for story in stories:
            try:
                self.github_client.create_issue(
                    title=story['title'],
                    body=story['body'],
                    labels=story['labels']
                )
                logging.info(f"Created issue: {story['title']}")
            except Exception as e:
                logging.error(f"Failed to create issue '{story['title']}': {e}")
                raise 