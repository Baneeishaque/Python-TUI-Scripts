#!/usr/bin/env python3
"""
Script to add GitHub topics to the repository.

This script uses the GitHub REST API to add recommended topics to the repository.
It requires a GitHub Personal Access Token with 'repo' scope.

Usage:
    python add_github_topics.py [--token YOUR_GITHUB_TOKEN]

If token is not provided via command line, it will look for GITHUB_TOKEN environment variable.
"""

import json
import os
import sys
import argparse
try:
    import urllib.request
    import urllib.error
except ImportError:
    print("Error: urllib is not available")
    sys.exit(1)


# Recommended topics for this repository
RECOMMENDED_TOPICS = [
    "python",
    "python-scripts",
    "automation",
    "cli-tools",
    "utilities",
    "pillow",
    "google-keep",
    "gkeepapi",
    "google-oauth",
    "homebrew",
    "docker",
    "vagrant",
    "azure-pipelines",
    "ci-cd",
    "developer-tools",
    "scripts",
    "python3",
    "image-processing",
    "google-api",
    "devops"
]

REPO_OWNER = "Baneeishaque"
REPO_NAME = "Python-TUI-Scripts"


def get_current_topics(token):
    """Get current topics from the repository."""
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/topics"
    
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"token {token}",
    }
    
    request = urllib.request.Request(url, headers=headers)
    
    try:
        with urllib.request.urlopen(request) as response:
            data = json.loads(response.read().decode())
            return data.get("names", [])
    except urllib.error.HTTPError as e:
        print(f"Error getting current topics: {e.code} {e.reason}")
        print(f"Response: {e.read().decode()}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


def set_topics(token, topics):
    """Set topics for the repository."""
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/topics"
    
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"token {token}",
        "Content-Type": "application/json",
    }
    
    data = json.dumps({"names": topics}).encode('utf-8')
    
    request = urllib.request.Request(url, data=data, headers=headers, method='PUT')
    
    try:
        with urllib.request.urlopen(request) as response:
            result = json.loads(response.read().decode())
            return result.get("names", [])
    except urllib.error.HTTPError as e:
        print(f"Error setting topics: {e.code} {e.reason}")
        print(f"Response: {e.read().decode()}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


def main():
    parser = argparse.ArgumentParser(
        description='Add GitHub topics to the repository',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python add_github_topics.py --token ghp_xxxxx
  GITHUB_TOKEN=ghp_xxxxx python add_github_topics.py
  python add_github_topics.py --dry-run
        """
    )
    parser.add_argument(
        '--token',
        help='GitHub Personal Access Token (or set GITHUB_TOKEN env var)',
        default=os.environ.get('GITHUB_TOKEN')
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be done without making changes'
    )
    
    args = parser.parse_args()
    
    if not args.token and not args.dry_run:
        print("Error: GitHub token is required")
        print("Provide it via --token argument or GITHUB_TOKEN environment variable")
        print("\nTo create a token:")
        print("1. Go to https://github.com/settings/tokens")
        print("2. Click 'Generate new token (classic)'")
        print("3. Select 'repo' scope")
        print("4. Generate and copy the token")
        sys.exit(1)
    
    print(f"Repository: {REPO_OWNER}/{REPO_NAME}")
    print(f"Recommended topics ({len(RECOMMENDED_TOPICS)}):")
    for topic in RECOMMENDED_TOPICS:
        print(f"  - {topic}")
    
    if args.dry_run:
        print("\n[DRY RUN MODE - No changes will be made]")
        return
    
    print("\nFetching current topics...")
    current_topics = get_current_topics(args.token)
    
    if current_topics is None:
        print("Failed to get current topics")
        sys.exit(1)
    
    if current_topics:
        print(f"\nCurrent topics ({len(current_topics)}):")
        for topic in current_topics:
            print(f"  - {topic}")
    else:
        print("\nNo topics currently set")
    
    # Check if topics are already set correctly
    if set(current_topics) == set(RECOMMENDED_TOPICS):
        print("\n✓ Topics are already up to date!")
        return
    
    print("\nSetting new topics...")
    new_topics = set_topics(args.token, RECOMMENDED_TOPICS)
    
    if new_topics is None:
        print("Failed to set topics")
        sys.exit(1)
    
    print(f"\n✓ Successfully updated topics! ({len(new_topics)} topics set)")
    print("\nNew topics:")
    for topic in new_topics:
        print(f"  - {topic}")
    
    print(f"\nView repository: https://github.com/{REPO_OWNER}/{REPO_NAME}")


if __name__ == "__main__":
    main()
