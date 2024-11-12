from typing import Dict, List, Any
import yaml
import logging
from pathlib import Path

class StoryParser:
    """Parses and validates user stories from YAML files."""
    
    REQUIRED_FIELDS = {
        'type', 'title', 'as_a', 'i_want', 
        'so_that', 'priority', 'labels', 
        'acceptance_criteria'
    }
    
    def __init__(self, yaml_path: str):
        self.yaml_path = Path(yaml_path)
        if not self.yaml_path.exists():
            raise FileNotFoundError(f"YAML file not found: {yaml_path}")
    
    def parse_stories(self) -> List[Dict[str, Any]]:
        """
        Reads and validates stories from YAML file.
        Returns a list of validated story dictionaries.
        """
        try:
            with open(self.yaml_path, 'r') as file:
                data = yaml.safe_load(file)
                
            if not data or 'stories' not in data:
                raise ValueError("No stories found in YAML file")
                
            stories = data['stories']
            validated_stories = []
            
            for story in stories:
                self._validate_story(story)
                formatted_story = self._format_story(story)
                validated_stories.append(formatted_story)
                
            return validated_stories
            
        except yaml.YAMLError as e:
            logging.error(f"Error parsing YAML file: {e}")
            raise
    
    def _validate_story(self, story: Dict[str, Any]) -> None:
        """Validates that a story contains all required fields."""
        missing_fields = self.REQUIRED_FIELDS - set(story.keys())
        if missing_fields:
            raise ValueError(f"Story missing required fields: {missing_fields}")
            
        if not isinstance(story['labels'], list):
            raise ValueError("Labels must be a list")
            
        if not isinstance(story['acceptance_criteria'], list):
            raise ValueError("Acceptance criteria must be a list")
    
    def _format_story(self, story: Dict[str, Any]) -> Dict[str, Any]:
        """
        Formats a story dictionary into GitHub issue format.
        Returns a dictionary with 'title' and 'body' keys.
        """
        body = f"""**As a** {story['as_a']}
**I want** {story['i_want']}
**So that** {story['so_that']}

**Type:** {story['type']}
**Priority:** {story['priority']}

**Acceptance Criteria:**
"""
        
        for criterion in story['acceptance_criteria']:
            body += f"- [ ] {criterion}\n"
            
        return {
            'title': story['title'],
            'body': body,
            'labels': story['labels']
        } 