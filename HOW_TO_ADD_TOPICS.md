# How to Add GitHub Topics

This guide provides step-by-step instructions for adding GitHub topics to your repository using various methods.

## Quick Start

### Option 1: Automated Python Script (Recommended)

```bash
# Set your GitHub token
export GITHUB_TOKEN="your_github_token_here"

# Run the script
python3 add_github_topics.py
```

### Option 2: Automated Shell Script

```bash
# Interactive mode
./add_github_topics.sh

# Or use GitHub CLI directly
./add_github_topics.sh --gh

# Or use curl with API
export GITHUB_TOKEN="your_token"
./add_github_topics.sh --curl
```

### Option 3: Manual Web Interface

1. Go to https://github.com/Baneeishaque/Python-TUI-Scripts
2. Click the ⚙️ gear icon next to "About" section
3. Add topics one by one in the "Topics" field
4. Click "Save changes"

---

## Detailed Instructions

### Method 1: Python Script

**Requirements:**
- Python 3.6+
- GitHub Personal Access Token

**Steps:**

1. **Create GitHub Token** (if you don't have one):
   - Go to https://github.com/settings/tokens
   - Click "Generate new token (classic)"
   - Give it a name: "Topic Management"
   - Select scope: `repo` (Full control of private repositories)
   - Click "Generate token"
   - Copy the token (starts with `ghp_`)

2. **Run the script:**
   ```bash
   # Dry run to see what will happen
   python3 add_github_topics.py --dry-run
   
   # Actually add topics
   python3 add_github_topics.py --token ghp_your_token_here
   
   # Or use environment variable
   export GITHUB_TOKEN="ghp_your_token_here"
   python3 add_github_topics.py
   ```

3. **Verify:**
   Visit https://github.com/Baneeishaque/Python-TUI-Scripts to see the topics

**Script Features:**
- Shows current topics
- Shows what will be added
- Validates token before making changes
- Provides detailed error messages
- Supports dry-run mode

---

### Method 2: Shell Script with GitHub CLI

**Requirements:**
- Bash shell
- GitHub CLI (`gh`)
- `jq` for JSON processing

**Installation:**

```bash
# macOS
brew install gh jq

# Ubuntu/Debian
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update
sudo apt install gh jq

# Windows (using Chocolatey)
choco install gh jq
```

**Steps:**

1. **Authenticate with GitHub CLI:**
   ```bash
   gh auth login
   ```
   Follow the prompts to authenticate.

2. **Run the script:**
   ```bash
   # Interactive mode
   ./add_github_topics.sh
   
   # Use GitHub CLI method directly
   ./add_github_topics.sh --gh
   
   # Display topics only
   ./add_github_topics.sh --display
   
   # Get help
   ./add_github_topics.sh --help
   ```

---

### Method 3: Direct GitHub CLI Command

**One-liner to add all topics:**

```bash
gh api --method PUT /repos/Baneeishaque/Python-TUI-Scripts/topics \
  -f names='["python","python-scripts","automation","cli-tools","utilities","pillow","google-keep","gkeepapi","google-oauth","homebrew","docker","vagrant","azure-pipelines","ci-cd","developer-tools","scripts","python3","image-processing","google-api","devops"]'
```

**View current topics:**

```bash
gh api /repos/Baneeishaque/Python-TUI-Scripts/topics
```

---

### Method 4: Using curl and GitHub API

**Requirements:**
- curl
- GitHub Personal Access Token
- jq (optional, for pretty output)

**Steps:**

1. **Set your token:**
   ```bash
   export GITHUB_TOKEN="ghp_your_token_here"
   ```

2. **Add topics:**
   ```bash
   curl -X PUT \
     -H "Accept: application/vnd.github+json" \
     -H "Authorization: token $GITHUB_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{
       "names": [
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
     }' \
     https://api.github.com/repos/Baneeishaque/Python-TUI-Scripts/topics
   ```

3. **View topics (with jq for formatting):**
   ```bash
   curl -H "Accept: application/vnd.github+json" \
     -H "Authorization: token $GITHUB_TOKEN" \
     https://api.github.com/repos/Baneeishaque/Python-TUI-Scripts/topics | jq
   ```

---

### Method 5: Using PyGithub Library

**Requirements:**
- Python 3.6+
- PyGithub library

**Installation:**
```bash
pip install PyGithub
```

**Script:**

```python
from github import Github

# Authenticate
token = "ghp_your_token_here"
g = Github(token)

# Get repository
repo = g.get_repo("Baneeishaque/Python-TUI-Scripts")

# Define topics
topics = [
    "python", "python-scripts", "automation", "cli-tools", "utilities",
    "pillow", "google-keep", "gkeepapi", "google-oauth", "homebrew",
    "docker", "vagrant", "azure-pipelines", "ci-cd", "developer-tools",
    "scripts", "python3", "image-processing", "google-api", "devops"
]

# Set topics
repo.replace_topics(topics)

print(f"✓ Topics updated!")
print(f"Current topics: {repo.get_topics()}")
```

---

## Recommended Topics for This Repository

The following 20 topics have been carefully selected based on the repository content:

1. **python** - Primary language
2. **python-scripts** - Collection of scripts
3. **automation** - Automation utilities
4. **cli-tools** - Command-line tools
5. **utilities** - General utilities
6. **pillow** - Image processing library
7. **google-keep** - Google Keep integration
8. **gkeepapi** - Google Keep API
9. **google-oauth** - Google OAuth
10. **homebrew** - Homebrew tools
11. **docker** - Docker support
12. **vagrant** - Vagrant configuration
13. **azure-pipelines** - Azure CI/CD
14. **ci-cd** - Continuous Integration
15. **developer-tools** - Dev tools
16. **scripts** - Generic scripts
17. **python3** - Python 3 compatibility
18. **image-processing** - Image manipulation
19. **google-api** - Google API integration
20. **devops** - DevOps tools

---

## Troubleshooting

### "Authentication failed"
- Verify your token is correct
- Ensure token has `repo` scope
- Check if token has expired

### "Resource not found"
- Verify repository name is correct
- Ensure you have access to the repository
- Check if repository is private and token has private repo access

### "Topics unchanged"
- Topics might already be set correctly
- Check current topics first before updating

### Script errors
- Ensure Python 3.6+ is installed
- Check internet connectivity
- Verify all dependencies are installed

---

## Best Practices

1. **Use automation**: Prefer scripts over manual methods for consistency
2. **Version control**: Keep topic lists in code for tracking changes
3. **Regular updates**: Review and update topics as repository evolves
4. **Follow conventions**: Use lowercase, hyphens for multi-word topics
5. **Be specific**: Choose accurate, relevant topics
6. **Limit to 20**: GitHub allows maximum 20 topics

---

## Security Notes

- **Never commit tokens**: Use environment variables or token managers
- **Rotate tokens regularly**: Generate new tokens periodically
- **Minimum permissions**: Use tokens with minimum required scopes
- **Secure storage**: Store tokens in secure password managers

---

## Additional Resources

- [GitHub Topics Documentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics)
- [GitHub REST API - Topics](https://docs.github.com/en/rest/repos/repos#replace-all-repository-topics)
- [GitHub CLI Documentation](https://cli.github.com/manual/)
- [PyGithub Documentation](https://pygithub.readthedocs.io/)

---

## Quick Reference Card

| Method | Difficulty | Requirements | Best For |
|--------|-----------|--------------|----------|
| Web Interface | Easy | Browser | One-time setup |
| Python Script | Easy | Python, Token | Automation |
| Shell Script | Medium | Bash, gh/curl | CI/CD |
| GitHub CLI | Medium | gh CLI | Command line users |
| curl | Medium | curl, Token | Scripting |
| PyGithub | Medium | Python, Library | Python projects |

---

For more details, see [GITHUB_TOPICS_ANALYSIS.md](GITHUB_TOPICS_ANALYSIS.md)
