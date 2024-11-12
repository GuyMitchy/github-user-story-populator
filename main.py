import logging
import argparse
from src.issue_creator import IssueCreator

def setup_logging():
    """Configure logging settings."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description='Create GitHub issues from YAML stories'
    )
    parser.add_argument(
        '--stories',
        default='stories.yaml',
        help='Path to the YAML file containing stories'
    )
    args = parser.parse_args()
    
    setup_logging()
    
    try:
        creator = IssueCreator(args.stories)
        creator.create_issues_from_stories()
        logging.info("Successfully completed issue creation")
    except Exception as e:
        logging.error(f"Script failed: {e}")
        raise

if __name__ == "__main__":
    main() 