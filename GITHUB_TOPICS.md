# GitHub Topics and Tags for Python-TUI-Scripts

This document provides recommended GitHub topics for this repository along with various methods to add them.

## Recommended GitHub Topics

Based on the analysis of this repository, the following GitHub topics are recommended:

### Primary Topics (Most Relevant)
| Topic | Reason |
|-------|--------|
| `python` | Main programming language used |
| `python3` | Python 3 specific code |
| `console-application` | Console/CLI based scripts |
| `cli` | Command-line interface tools |
| `tui` | Text User Interface scripts |
| `automation` | Automation utility scripts |
| `scripts` | Collection of scripts |

### Technology-Specific Topics
| Topic | Reason |
|-------|--------|
| `pillow` | Uses Pillow for image processing |
| `google-apis` | Integration with Google services |
| `gkeepapi` | Google Keep API integration |
| `homebrew` | Homebrew tap auditing script |

### DevOps/Infrastructure Topics
| Topic | Reason |
|-------|--------|
| `docker` | Docker containerization support |
| `vagrant` | Vagrant development environment |
| `azure-pipelines` | Azure DevOps CI/CD |

### Additional Relevant Topics
| Topic | Reason |
|-------|--------|
| `utilities` | General utility scripts |
| `devtools` | Developer tools collection |

## Complete List of Suggested Topics

```
python, python3, console-application, cli, tui, automation, scripts, pillow, google-apis, homebrew, docker, vagrant, azure-pipelines, utilities, devtools
```

## Methods to Add GitHub Topics

### Method 1: GitHub CLI (gh)

The GitHub CLI is the recommended way to programmatically add topics to a repository.

#### Installation

```bash
# macOS
brew install gh

# Windows
winget install GitHub.cli

# Ubuntu/Debian
sudo apt install gh

# Fedora
sudo dnf install gh
```

#### Authentication

```bash
gh auth login
```

#### Adding Topics

```bash
# Add individual topics
gh repo edit Baneeishaque/Python-TUI-Scripts --add-topic python
gh repo edit Baneeishaque/Python-TUI-Scripts --add-topic python3
gh repo edit Baneeishaque/Python-TUI-Scripts --add-topic console-application
gh repo edit Baneeishaque/Python-TUI-Scripts --add-topic cli
gh repo edit Baneeishaque/Python-TUI-Scripts --add-topic tui
gh repo edit Baneeishaque/Python-TUI-Scripts --add-topic automation
gh repo edit Baneeishaque/Python-TUI-Scripts --add-topic scripts
gh repo edit Baneeishaque/Python-TUI-Scripts --add-topic pillow
gh repo edit Baneeishaque/Python-TUI-Scripts --add-topic google-apis
gh repo edit Baneeishaque/Python-TUI-Scripts --add-topic homebrew
gh repo edit Baneeishaque/Python-TUI-Scripts --add-topic docker
gh repo edit Baneeishaque/Python-TUI-Scripts --add-topic vagrant
gh repo edit Baneeishaque/Python-TUI-Scripts --add-topic azure-pipelines
gh repo edit Baneeishaque/Python-TUI-Scripts --add-topic utilities
gh repo edit Baneeishaque/Python-TUI-Scripts --add-topic devtools

# Add multiple topics at once (recommended)
gh repo edit Baneeishaque/Python-TUI-Scripts \
  --add-topic python \
  --add-topic python3 \
  --add-topic console-application \
  --add-topic cli \
  --add-topic tui \
  --add-topic automation \
  --add-topic scripts \
  --add-topic pillow \
  --add-topic google-apis \
  --add-topic homebrew \
  --add-topic docker \
  --add-topic vagrant \
  --add-topic azure-pipelines \
  --add-topic utilities \
  --add-topic devtools
```

#### Removing Topics

```bash
gh repo edit Baneeishaque/Python-TUI-Scripts --remove-topic topic-name
```

#### Viewing Current Topics

```bash
gh repo view Baneeishaque/Python-TUI-Scripts --json topics
```

### Method 2: GitHub Web Interface

1. Navigate to the repository: https://github.com/Baneeishaque/Python-TUI-Scripts
2. Click the gear icon (⚙️) next to "About" on the right sidebar
3. In the "Topics" field, add the topics separated by spaces
4. Click "Save changes"

### Method 3: GitHub REST API

You can use the GitHub REST API with `curl` or any HTTP client.

#### Using curl with Personal Access Token

```bash
# Set your token
export GITHUB_TOKEN="your_personal_access_token"

# Replace all topics (this will override existing topics)
curl -X PUT \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer $GITHUB_TOKEN" \
  https://api.github.com/repos/Baneeishaque/Python-TUI-Scripts/topics \
  -d '{"names":["python","python3","console-application","cli","tui","automation","scripts","pillow","google-apis","homebrew","docker","vagrant","azure-pipelines","utilities","devtools"]}'
```

#### Using Python with requests library

```python
import requests
import os

token = os.getenv('GITHUB_TOKEN')
headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': f'Bearer {token}'
}

topics = [
    'python', 'python3', 'console-application', 'cli', 'tui',
    'automation', 'scripts', 'pillow', 'google-apis', 'homebrew',
    'docker', 'vagrant', 'azure-pipelines', 'utilities', 'devtools'
]

response = requests.put(
    'https://api.github.com/repos/Baneeishaque/Python-TUI-Scripts/topics',
    headers=headers,
    json={'names': topics}
)

print(response.json())
```

### Method 4: GitHub GraphQL API

```bash
# Using curl with GraphQL
curl -X POST \
  -H "Authorization: Bearer $GITHUB_TOKEN" \
  -H "Content-Type: application/json" \
  https://api.github.com/graphql \
  -d '{
    "query": "mutation { updateTopics(input: {repositoryId: \"REPO_ID\", topicNames: [\"python\", \"python3\", \"cli\"]}) { repository { topics { nodes { name } } } } }"
  }'
```

Note: You need to replace `REPO_ID` with the actual repository node ID, which can be obtained via:

```bash
gh api graphql -f query='{ repository(owner: "Baneeishaque", name: "Python-TUI-Scripts") { id } }'
```

## Quick Start Command

Run this single command to add all recommended topics:

```bash
gh repo edit Baneeishaque/Python-TUI-Scripts --add-topic python --add-topic python3 --add-topic console-application --add-topic cli --add-topic tui --add-topic automation --add-topic scripts --add-topic pillow --add-topic google-apis --add-topic homebrew --add-topic docker --add-topic vagrant --add-topic azure-pipelines --add-topic utilities --add-topic devtools
```

## Topic Guidelines

- Topics should be lowercase
- Use hyphens instead of spaces
- Topics should be concise and descriptive
- Avoid overly generic topics unless they're accurate
- Maximum 20 topics per repository

## Verification

After adding topics, verify them using:

```bash
# Using GitHub CLI
gh repo view Baneeishaque/Python-TUI-Scripts --json topics

# Using curl
curl -H "Accept: application/vnd.github+json" \
  https://api.github.com/repos/Baneeishaque/Python-TUI-Scripts/topics
```

## References

- [GitHub CLI Documentation](https://cli.github.com/manual/)
- [GitHub REST API - Topics](https://docs.github.com/en/rest/repos/repos#replace-all-repository-topics)
- [About Topics](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics)
