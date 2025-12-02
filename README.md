# 🐍 Python TUI Scripts

<div align="center">

![Python Logo](https://raw.githubusercontent.com/Baneeishaque/Python-TUI-Scripts/master/logo.png)

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-PEP8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)
[![Build Status](https://dev.azure.com/baneeishaque/Python-TUI-Scripts/_apis/build/status/Python-TUI-Scripts?branchName=master)](https://dev.azure.com/baneeishaque/Python-TUI-Scripts/_build/latest?definitionId=1&branchName=master)
[![Renovate](https://img.shields.io/badge/renovate-enabled-brightgreen.svg)](https://renovatebot.com)

**A curated collection of powerful Python Terminal User Interface (TUI) scripts for everyday automation tasks**

[Features](#-features) •
[Installation](#-installation) •
[Usage](#-usage) •
[Scripts](#-available-scripts) •
[Development](#-development) •
[Contributing](#-contributing)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Technical Stack](#-technical-stack)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
  - [Quick Start](#quick-start)
  - [Docker Setup](#docker-setup)
  - [Vagrant Setup](#vagrant-setup)
  - [Development Environment](#development-environment)
- [Available Scripts](#-available-scripts)
- [Usage](#-usage)
- [Configuration](#-configuration)
- [Project Structure](#-project-structure)
- [Development](#-development)
- [CI/CD Pipeline](#-cicd-pipeline)
- [Contributing](#-contributing)
- [Troubleshooting](#-troubleshooting)
- [License](#-license)
- [Contact](#-contact)

---

## 🌟 Overview

**Python TUI Scripts** is a comprehensive collection of command-line utilities designed to simplify common automation tasks. From system administration to API interactions, this repository provides ready-to-use scripts that enhance productivity through terminal-based interfaces.

### Why This Repository?

- 🚀 **Production-Ready**: Battle-tested scripts for real-world scenarios
- 📦 **Modular Design**: Each script is self-contained and independent
- 🔧 **Easy Integration**: Simple to integrate into existing workflows
- 📚 **Well-Documented**: Extensive inline documentation and examples
- 🐳 **Container Support**: Docker and Vagrant configurations included
- 🔄 **Automated Updates**: Renovate and PyUp integration for dependency management

---

## ✨ Features

### Core Capabilities

- **📱 Google API Integration**: Scripts for Google Keep and authentication
- **🍺 Homebrew Management**: Audit and manage Homebrew taps
- **🎨 Image Processing**: Generate custom letter logos programmatically
- **⚙️ System Utilities**: Cache management and system diagnostics
- **♾️ Background Tasks**: Infinite loop scripts for monitoring
- **🔐 OAuth Authentication**: Google OAuth token management

### Development Features

- ✅ **Multi-platform Support**: Works on Linux, macOS, and Windows
- 🐳 **Containerized Deployment**: Docker and Vagrant configurations
- 🔄 **Automated Dependency Updates**: Renovate and PyUp integration
- 📊 **CI/CD Pipeline**: Azure Pipelines for continuous integration
- 🛠️ **Development Tools**: mise for version management

---

## 🔧 Technical Stack

### Languages & Frameworks

| Technology | Version | Purpose |
|------------|---------|---------|
| **Python** | 3.7+ | Primary language |
| **Pillow** | 11.1.0 | Image processing |
| **gpsoauth** | 2.0.0 | Google authentication |
| **gkeepapi** | 0.17.0 | Google Keep API |
| **pip** | 24.3.1 | Package management |

### Infrastructure & DevOps

- **Docker**: Alpine Linux-based containerization
- **Vagrant**: VirtualBox/generic Alpine 3.8 VM provisioning
- **Azure Pipelines**: Continuous integration and Docker image building
- **mise**: Development environment version management
- **Renovate**: Automated dependency updates
- **PyUp**: Python package security monitoring

### Development Environment

- **Supported IDEs**: 
  - Gitpod (cloud-based)
  - GitHub1s (web-based editor)
  - Google Cloud Shell
  - JetBrains (IntelliJ/PyCharm)
  - Visual Studio Code

---

## 📦 Prerequisites

### System Requirements

- **Operating System**: Linux, macOS, Windows (with WSL2), or Docker
- **Python**: Version 3.7 or higher
- **pip**: Latest version (included with Python 3.4+)
- **Git**: For cloning the repository

### Optional Requirements

- **Docker**: For containerized execution (recommended)
- **Vagrant**: For VM-based development
- **Homebrew**: For macOS users running brew_tap_audit.py
- **Font Files**: For create_letter_logo.py (Arial.ttf or similar)

### Python Version Compatibility

```bash
# Check your Python version
python3 --version

# Minimum supported: Python 3.7
# Recommended: Python 3.10+
# Tested on: Python 3.7, 3.8, 3.9, 3.10, 3.11, 3.12
```

---

## 🚀 Installation

### Quick Start

#### 1. Clone the Repository

```bash
git clone https://github.com/Baneeishaque/Python-TUI-Scripts.git
cd Python-TUI-Scripts
```

#### 2. Install Dependencies

```bash
# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

#### 3. Verify Installation

```bash
# Test a simple script
python3 pip_cache_directories.py
```

---

### Docker Setup

Docker provides an isolated, consistent environment for running scripts.

#### Build Docker Image

```bash
# Build the Docker image
docker build -t python-tui-scripts .

# Run a script in the container
docker run --rm python-tui-scripts

# Run with custom script
docker run --rm -v $(pwd):/usr/src/app python-tui-scripts python ./infinteRun.py
```

#### Docker Compose (Advanced)

```yaml
# Create docker-compose.yml
version: '3.8'
services:
  scripts:
    build: .
    volumes:
      - .:/usr/src/app
    command: python ./pip_cache_directories.py
```

```bash
# Run with Docker Compose
docker-compose up
```

---

### Vagrant Setup

Vagrant provides a reproducible development environment using virtual machines.

#### Start Vagrant VM

```bash
# Start and provision the VM
vagrant up

# SSH into the VM
vagrant ssh

# Navigate to synced folder
cd /vagrant

# Install dependencies (if not auto-provisioned)
pip install -r requirements.txt

# Run scripts
python pip_cache_directories.py
```

#### Vagrant Commands

```bash
# Suspend VM (save state)
vagrant suspend

# Resume VM
vagrant resume

# Destroy VM (cleanup)
vagrant destroy

# Reload VM (with provisioning)
vagrant reload --provision
```

---

### Development Environment

#### Using mise (Recommended)

mise is a polyglot version manager that ensures consistent Python versions.

```bash
# Install mise (if not already installed)
curl https://mise.run | sh

# Activate mise
mise install

# Verify Python version
python --version  # Should show Python 3.10.16
```

#### Using Cloud IDEs

##### Gitpod

<a href="https://gitpod.io/#https://github.com/Baneeishaque/Python-TUI-Scripts">
  <img src="https://gitpod.io/button/open-in-gitpod.svg" alt="Open in Gitpod">
</a>

```bash
# One-click setup with Gitpod
# https://gitpod.io/#https://github.com/Baneeishaque/Python-TUI-Scripts
```

##### GitHub1s

<a href="https://github1s.com/Baneeishaque/Python-TUI-Scripts">
  <img src="https://raw.githubusercontent.com/conwnet/github1s/master/resources/images/logo.svg" alt="Open in GitHub1s" width="100">
</a>

```bash
# Web-based VS Code editor
# https://github1s.com/Baneeishaque/Python-TUI-Scripts
```

##### Google Cloud Shell

[![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.svg)](https://ssh.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https://github.com/Baneeishaque/Python-TUI-Scripts)

---

## 📜 Available Scripts

### 1. **brew_tap_audit.py** 🍺

**Purpose**: Audit Homebrew taps for accessibility and installed packages.

**Features**:
- Lists all Homebrew taps (including core and cask repositories)
- Checks GitHub URL accessibility for each tap
- Groups installed formulae and casks by their source tap
- Provides detailed output of installed packages per tap

**Usage**:
```bash
python brew_tap_audit.py
```

**Output Example**:
```
Found 15 taps. Checking accessibility and usage...

[OK] homebrew/core (https://github.com/homebrew/homebrew-core) is reachable
 ↳ Formulae: git, node, python@3.10, wget
 ↳ Casks: 

[OK] homebrew/cask (https://github.com/homebrew/homebrew-cask) is reachable
 ↳ Formulae: 
 ↳ Casks: docker, visual-studio-code

[ERROR] Cannot reach custom/tap (https://github.com/custom/homebrew-tap): Error: HTTP Error 404
 ↳ No formulae or casks installed from custom/tap
```

**Technical Details**:
- Uses `subprocess` to execute brew commands
- Leverages `brew info --json=v2` for efficient batch queries
- Implements URL reachability checks via `urllib`
- Handles errors gracefully with fallback mechanisms

**Requirements**:
- macOS with Homebrew installed
- Network connectivity for GitHub URL checks

---

### 2. **create_letter_logo.py** 🎨

**Purpose**: Generate custom letter-based logos programmatically.

**Features**:
- Creates PNG logos with custom text
- Automatically centers text in the image
- Supports TTF/OTF font files
- Configurable font size based on image dimensions

**Usage**:
```bash
python create_letter_logo.py
```

**Configuration**:
```python
# Edit the script to customize:
text = "DL"  # Change the logo text
font_path = "/Library/Fonts/Arial.ttf"  # Font location
background_color = "white"
text_color = "black"
```

**Output**:
- Creates `logo_new.png` in the current directory
- Maintains aspect ratio of original logo
- RGBA color space support

**Technical Details**:
- Uses Pillow (PIL) for image manipulation
- Font rendering with TrueType support
- Bounding box calculations for precise centering
- Anti-aliased text rendering

**Use Cases**:
- Batch logo generation
- Placeholder image creation
- Brand asset automation
- Dynamic watermark generation

---

### 3. **gpsoauth_script.py** 🔐

**Purpose**: Perform Google OAuth authentication using master login (legacy).

**Status**: ⚠️ Not currently working due to 2FA requirements

**Features**:
- Master token generation via email/password
- OAuth token exchange for Google services
- Service-specific authentication (Google Play Music, etc.)

**Usage**:
```python
# Configure credentials
email = 'example@gmail.com'
password = 'your-app-password'
android_id = '0123456789abcdef'

# Run the script
python gpsoauth_script.py
```

**Security Notes**:
- ⚠️ Never commit credentials to version control
- Use app-specific passwords when possible
- Consider using environment variables for sensitive data
- This method is deprecated; use gpsoauth_script_alternative.py instead

---

### 4. **gpsoauth_script_alternative.py** 🔑

**Purpose**: Alternative Google OAuth authentication using token exchange.

**Features**:
- Token exchange mechanism (more secure)
- Bypasses direct password authentication
- Supports 2FA-enabled accounts

**Usage**:
```python
# Configure with existing OAuth token
email = 'example@gmail.com'
android_id = '0123456789abcdef'
oauth_token = 'your-oauth-token-here'

# Run the script
python gpsoauth_script_alternative.py
```

**How to Get OAuth Token**:
1. Use browser-based OAuth flow
2. Extract token from authorized session
3. Insert into script configuration

**Security Best Practices**:
```bash
# Use environment variables
export GOOGLE_EMAIL="your@email.com"
export GOOGLE_OAUTH_TOKEN="your-token"
export ANDROID_ID="your-device-id"

# Modify script to read from environment
import os
email = os.getenv('GOOGLE_EMAIL')
```

---

### 5. **gkeepapi_script.py** 📝

**Purpose**: Interact with Google Keep API programmatically.

**Status**: ⚠️ Currently experiencing BadAuthentication errors

**Features**:
- Create and manage Google Keep notes
- Set note properties (pinned, color, etc.)
- Sync notes with Google Keep cloud

**Usage**:
```python
# Configure master token
master_token = 'your-master-token'

# Run the script
python gkeepapi_script.py
```

**Functionality**:
```python
# Creates a note titled "Todo" with content "Eat breakfast"
# Sets note as pinned
# Sets note color to red
# Syncs with Google Keep
```

**Known Issues**:
- Authentication currently failing due to API changes
- May require updated gkeepapi library
- Alternative: Use official Google Keep API

**Roadmap**:
- Update to latest gkeepapi version
- Implement error handling and retry logic
- Add support for labels and reminders

---

### 6. **infinteRun.py** ♾️

**Purpose**: Continuous execution script for monitoring and periodic tasks.

**Features**:
- Infinite loop execution
- Configurable delay intervals
- Simple and lightweight

**Usage**:
```bash
# Run in foreground
python infinteRun.py

# Run in background (Linux/macOS)
nohup python infinteRun.py &

# Run with systemd (Linux)
# See systemd section below
```

**Configuration**:
```python
# Edit sleep duration (currently 60 seconds)
time.sleep(60)  # Change to desired interval

# Customize action
print("This prints once a minute.")  # Replace with your code
```

**Use Cases**:
- Health check monitoring
- Periodic API polling
- Log file monitoring
- Keep-alive scripts for servers
- Scheduled task execution

**Running as System Service (Linux)**:

```bash
# Create systemd service file
sudo nano /etc/systemd/system/infinite-run.service
```

```ini
[Unit]
Description=Python Infinite Run Script
After=network.target

[Service]
Type=simple
User=your-username
WorkingDirectory=/path/to/Python-TUI-Scripts
ExecStart=/usr/bin/python3 /path/to/Python-TUI-Scripts/infinteRun.py
Restart=always

[Install]
WantedBy=multi-user.target
```

```bash
# Enable and start service
sudo systemctl daemon-reload
sudo systemctl enable infinite-run.service
sudo systemctl start infinite-run.service

# Check status
sudo systemctl status infinite-run.service
```

---

### 7. **pip_cache_directories.py** 📦

**Purpose**: Display pip and wheel cache directory locations.

**Features**:
- Shows pip cache location
- Shows wheel cache location
- Platform-independent paths
- Useful for cache management and cleanup

**Usage**:
```bash
python pip_cache_directories.py
```

**Output Example**:
```
/home/username/.cache/pip
/home/username/.cache/pip/wheels
```

**Platform-Specific Paths**:

| Platform | Default Cache Location |
|----------|------------------------|
| **Linux** | `~/.cache/pip` |
| **macOS** | `~/Library/Caches/pip` |
| **Windows** | `%LocalAppData%\pip\Cache` |

**Cache Management**:
```bash
# View cache size
du -sh $(python pip_cache_directories.py | head -1)

# Clear pip cache
pip cache purge

# Remove specific package cache
pip cache remove package-name
```

**Integration Examples**:
```python
# Use in cleanup scripts
from pip._internal.utils.appdirs import user_cache_dir
import shutil

cache_dir = user_cache_dir('pip')
# shutil.rmtree(cache_dir)  # Careful! This deletes the cache
```

---

## 🎯 Usage

### Running Scripts

#### Direct Execution

```bash
# Make script executable (Linux/macOS)
chmod +x script_name.py

# Run directly
./script_name.py

# Or use Python interpreter
python3 script_name.py
```

#### With Virtual Environment

```bash
# Activate virtual environment
source venv/bin/activate  # Linux/macOS
# or
venv\Scripts\activate  # Windows

# Run script
python script_name.py

# Deactivate when done
deactivate
```

#### Batch Execution

```bash
# Run multiple scripts sequentially
python3 pip_cache_directories.py && python3 brew_tap_audit.py

# Run in parallel (background)
python3 infinteRun.py &
python3 other_script.py &
```

### Command-Line Arguments

While current scripts don't use CLI arguments, you can extend them:

```python
# Example: Adding argparse to infinteRun.py
import argparse
import time

parser = argparse.ArgumentParser(description='Infinite run script')
parser.add_argument('--interval', type=int, default=60, help='Sleep interval in seconds')
args = parser.parse_args()

while True:
    print(f"Running every {args.interval} seconds")
    time.sleep(args.interval)
```

```bash
# Usage
python infinteRun.py --interval 30
```

---

## ⚙️ Configuration

### Environment Variables

For scripts requiring credentials, use environment variables:

```bash
# Create .env file (add to .gitignore!)
touch .env

# Add credentials
echo "GOOGLE_EMAIL=your@email.com" >> .env
echo "GOOGLE_MASTER_TOKEN=your-token" >> .env
echo "ANDROID_ID=your-device-id" >> .env
```

Load environment variables:

```python
# Using python-dotenv
from dotenv import load_dotenv
import os

load_dotenv()

email = os.getenv('GOOGLE_EMAIL')
token = os.getenv('GOOGLE_MASTER_TOKEN')
```

### Script-Specific Configuration

#### create_letter_logo.py

```python
# Configuration options
INPUT_LOGO = "logo.png"
OUTPUT_LOGO = "logo_new.png"
TEXT = "DL"
FONT_PATH = "/Library/Fonts/Arial.ttf"  # macOS
# FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"  # Linux
# FONT_PATH = "C:\\Windows\\Fonts\\arial.ttf"  # Windows
BACKGROUND_COLOR = "white"
TEXT_COLOR = "black"
FONT_SIZE_RATIO = 0.8
```

#### infinteRun.py

```python
# Configuration
SLEEP_INTERVAL = 60  # seconds
MESSAGE = "This prints once a minute."
LOG_FILE = "/var/log/infinite_run.log"  # Optional logging
```

### Docker Configuration

Modify `Dockerfile` for different scripts:

```dockerfile
# Change default script
CMD [ "python", "./brew_tap_audit.py" ]

# Or use environment variable
ENV SCRIPT_NAME pip_cache_directories.py
CMD python ${SCRIPT_NAME}
```

### Vagrant Configuration

Customize `Vagrantfile`:

```ruby
# Change VM box
config.vm.box = "ubuntu/focal64"  # Ubuntu instead of Alpine

# Add more memory
config.vm.provider "virtualbox" do |vb|
  vb.memory = "2048"
  vb.cpus = 2
end

# Additional provisioning
config.vm.provision "shell", inline: <<-SHELL
  pip install -r /vagrant/requirements.txt
SHELL
```

---

## 📁 Project Structure

```
Python-TUI-Scripts/
│
├── 📄 README.md                          # This file
├── 📄 requirements.txt                   # Python dependencies
├── 📄 Dockerfile                         # Docker configuration
├── 📄 Vagrantfile                        # Vagrant VM configuration
├── 📄 mise.toml                          # Development tool version manager
├── 📄 azure-pipelines.yml                # Azure DevOps CI/CD pipeline
├── 📄 renovate.json                      # Renovate dependency config
├── 📄 .pyup.yml                          # PyUp security monitoring
├── 📄 .gitignore                         # Git ignore rules
├── 📄 .dockerignore                      # Docker ignore rules
├── 📄 .whitesource                       # WhiteSource security config
│
├── 🐍 Scripts/
│   ├── brew_tap_audit.py                # Homebrew tap auditing
│   ├── create_letter_logo.py            # Logo generation
│   ├── gpsoauth_script.py               # Google OAuth (legacy)
│   ├── gpsoauth_script_alternative.py   # Google OAuth (alternative)
│   ├── gkeepapi_script.py               # Google Keep integration
│   ├── infinteRun.py                    # Infinite loop utility
│   └── pip_cache_directories.py         # Pip cache location finder
│
├── 🖼️ Assets/
│   └── logo.png                         # Project logo
│
└── 📂 .idea/                            # JetBrains IDE configuration
    └── (IDE-specific files)
```

### File Descriptions

| File/Directory | Purpose |
|----------------|---------|
| **requirements.txt** | Python package dependencies |
| **Dockerfile** | Containerization configuration |
| **Vagrantfile** | VM provisioning and setup |
| **azure-pipelines.yml** | CI/CD pipeline definition |
| **mise.toml** | Development environment versions |
| **renovate.json** | Automated dependency updates |
| **.pyup.yml** | Python security monitoring |
| **.gitignore** | Git exclusion patterns |
| **.idea/** | JetBrains IDE settings |

---

## 🛠️ Development

### Setting Up Development Environment

#### 1. Fork and Clone

```bash
# Fork the repository on GitHub
# Then clone your fork
git clone https://github.com/YOUR_USERNAME/Python-TUI-Scripts.git
cd Python-TUI-Scripts

# Add upstream remote
git remote add upstream https://github.com/Baneeishaque/Python-TUI-Scripts.git
```

#### 2. Create Virtual Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate (Linux/macOS)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Install development dependencies (optional)
pip install black flake8 mypy pytest
```

#### 3. Install Pre-commit Hooks (Recommended)

```bash
# Install pre-commit
pip install pre-commit

# Set up git hooks
pre-commit install
```

### Code Style and Standards

#### Python Style Guide

We follow **PEP 8** style guidelines:

```bash
# Format code with black
black *.py

# Lint with flake8
flake8 *.py --max-line-length=100

# Type checking with mypy
mypy *.py
```

#### Code Style Rules

- **Indentation**: 4 spaces (no tabs)
- **Line Length**: Maximum 100 characters
- **Naming Conventions**:
  - `snake_case` for functions and variables
  - `PascalCase` for classes
  - `UPPER_CASE` for constants
- **Docstrings**: Google-style docstrings for functions
- **Imports**: Organized (standard library, third-party, local)

#### Example Code Template

```python
"""
Module description.

This module provides functionality for...
"""

import os
import sys
from typing import List, Dict, Optional

from third_party_library import something


# Constants
DEFAULT_TIMEOUT = 30
MAX_RETRIES = 3


def example_function(param1: str, param2: int = 10) -> Dict[str, any]:
    """
    Brief description of function.
    
    Args:
        param1: Description of param1
        param2: Description of param2 (default: 10)
    
    Returns:
        Dictionary containing results
    
    Raises:
        ValueError: If param2 is negative
    """
    if param2 < 0:
        raise ValueError("param2 must be non-negative")
    
    result = {"param1": param1, "param2": param2}
    return result


if __name__ == "__main__":
    # Script execution entry point
    pass
```

### Testing

#### Manual Testing

```bash
# Test individual scripts
python brew_tap_audit.py
python pip_cache_directories.py
python infinteRun.py  # Ctrl+C to stop
```

#### Automated Testing (Future Enhancement)

```python
# tests/test_brew_tap_audit.py
import unittest
from unittest.mock import patch, MagicMock
import brew_tap_audit


class TestBrewTapAudit(unittest.TestCase):
    
    @patch('brew_tap_audit.subprocess.run')
    def test_get_homebrew_taps(self, mock_run):
        mock_run.return_value = MagicMock(
            stdout="homebrew/core\nhomebrew/cask\n",
            returncode=0
        )
        taps = brew_tap_audit.get_homebrew_taps()
        self.assertEqual(len(taps), 2)
        self.assertIn('homebrew/core', taps)


if __name__ == '__main__':
    unittest.main()
```

```bash
# Run tests
python -m pytest tests/
```

### Adding New Scripts

1. **Create Script File**
   ```bash
   touch new_script.py
   chmod +x new_script.py
   ```

2. **Add Script Header**
   ```python
   #!/usr/bin/env python3
   """
   Script description.
   
   Author: Your Name
   Date: YYYY-MM-DD
   """
   ```

3. **Update Requirements**
   ```bash
   # If adding new dependencies
   pip install new-package
   pip freeze | grep new-package >> requirements.txt
   ```

4. **Document in README**
   - Add script description
   - Include usage examples
   - List any special requirements

5. **Test Thoroughly**
   ```bash
   # Test in multiple environments
   python3 new_script.py
   docker build -t test . && docker run test python new_script.py
   ```

### Debugging

#### Python Debugger (pdb)

```python
# Add breakpoint in code
import pdb; pdb.set_trace()

# Or use Python 3.7+ breakpoint
breakpoint()
```

```bash
# Run with debugger
python -m pdb script.py
```

#### Logging

```python
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

# Use in code
logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
```

---

## 🔄 CI/CD Pipeline

### Azure Pipelines

The repository uses **Azure Pipelines** for continuous integration.

#### Pipeline Configuration

```yaml
# azure-pipelines.yml
trigger:
- master

pool:
  vmImage: 'ubuntu-latest'

steps:
- task: Docker@2
  displayName: 'Build Docker Image'
  inputs:
    command: build
    dockerfile: '$(Build.SourcesDirectory)/Dockerfile'
    tags: |
      $(Build.BuildId)
      latest
```

#### Pipeline Stages

1. **Trigger**: Runs on push to `master` branch
2. **Build**: Creates Docker image
3. **Tag**: Tags image with build ID and `latest`
4. **Publish**: (Future) Push to container registry

### Automated Dependency Management

#### Renovate

Automatically updates dependencies via pull requests.

**Configuration** (`renovate.json`):
```json
{
  "extends": ["config:base"],
  "schedule": ["before 5am on Monday"],
  "labels": ["dependencies"],
  "assignees": ["Baneeishaque"]
}
```

**Features**:
- Weekly dependency checks
- Automated PR creation
- Changelog integration
- Security vulnerability alerts

#### PyUp

Monitors Python packages for security issues.

**Configuration** (`.pyup.yml`):
```yaml
pin: False
schedule: every day
```

**Features**:
- Daily security scans
- Automated security patches
- Dependency version suggestions

---

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### Ways to Contribute

- 🐛 **Report Bugs**: Submit detailed bug reports with reproduction steps
- 💡 **Suggest Features**: Propose new scripts or enhancements
- 📝 **Improve Documentation**: Fix typos, add examples, clarify instructions
- 🔧 **Submit Code**: Fix bugs, add features, optimize performance
- 🧪 **Add Tests**: Increase code coverage and reliability
- 🌍 **Localization**: Translate documentation or messages

### Contribution Workflow

#### 1. Check Existing Issues

```bash
# Search for existing issues or feature requests
# https://github.com/Baneeishaque/Python-TUI-Scripts/issues
```

#### 2. Fork and Create Branch

```bash
# Fork the repository on GitHub
git clone https://github.com/YOUR_USERNAME/Python-TUI-Scripts.git
cd Python-TUI-Scripts

# Create feature branch
git checkout -b feature/amazing-feature

# Or bug fix branch
git checkout -b fix/bug-description
```

#### 3. Make Changes

```bash
# Make your changes
# Test thoroughly
python your_script.py

# Ensure code follows style guide
black *.py
flake8 *.py
```

#### 4. Commit Changes

```bash
# Stage changes
git add .

# Commit with descriptive message
git commit -m "feat: Add amazing new feature

- Detailed description of changes
- Why the change was needed
- Any breaking changes or migrations"
```

**Commit Message Guidelines**:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types**:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting)
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance tasks

**Examples**:
```bash
git commit -m "feat(brew): Add tap URL validation"
git commit -m "fix(logo): Handle missing font file gracefully"
git commit -m "docs(readme): Update installation instructions"
```

#### 5. Push and Create Pull Request

```bash
# Push to your fork
git push origin feature/amazing-feature

# Create Pull Request on GitHub
# https://github.com/Baneeishaque/Python-TUI-Scripts/compare
```

#### 6. Pull Request Guidelines

**PR Title**: Clear and descriptive
```
feat: Add support for custom font paths in logo generator
fix: Handle Homebrew tap 404 errors gracefully
docs: Add troubleshooting section to README
```

**PR Description Template**:
```markdown
## Description
Brief description of changes

## Motivation
Why is this change needed?

## Changes Made
- Change 1
- Change 2
- Change 3

## Testing
How was this tested?

## Screenshots (if applicable)
[Add screenshots]

## Checklist
- [ ] Code follows project style guide
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No breaking changes (or documented)
- [ ] Tests added/updated (if applicable)
```

### Code Review Process

1. **Automated Checks**: CI pipeline runs automatically
2. **Maintainer Review**: Project maintainer reviews code
3. **Feedback**: Address any requested changes
4. **Approval**: PR approved and merged
5. **Recognition**: Contributor added to acknowledgments

### Development Guidelines

#### Adding Dependencies

```bash
# Only add necessary dependencies
# Check for existing alternatives first

# Add to requirements.txt with pinned version
echo "new-package==1.2.3" >> requirements.txt

# Document why dependency is needed in PR
```

#### Security Considerations

- Never commit credentials or API keys
- Use environment variables for sensitive data
- Validate user input
- Handle errors gracefully
- Follow OWASP security guidelines

#### Performance Considerations

- Avoid unnecessary loops or recursion
- Use generators for large datasets
- Profile code for bottlenecks
- Implement caching where appropriate

### Getting Help

- 💬 **Discussions**: [GitHub Discussions](https://github.com/Baneeishaque/Python-TUI-Scripts/discussions)
- 🐛 **Issues**: [GitHub Issues](https://github.com/Baneeishaque/Python-TUI-Scripts/issues)
- 📧 **Email**: Contact repository owner

---

## 🔍 Troubleshooting

### Common Issues

#### 1. Import Errors

**Problem**:
```
ModuleNotFoundError: No module named 'PIL'
```

**Solution**:
```bash
# Ensure virtual environment is activated
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt

# Or install specific package
pip install pillow
```

#### 2. Font Not Found (create_letter_logo.py)

**Problem**:
```
OSError: cannot open resource
```

**Solution**:
```bash
# Find available fonts
# macOS
ls /Library/Fonts/
ls ~/Library/Fonts/

# Linux
fc-list | grep -i arial

# Update font path in script
font = ImageFont.truetype("/path/to/font.ttf", font_size)
```

#### 3. Homebrew Not Found (brew_tap_audit.py)

**Problem**:
```
Error getting taps: [Errno 2] No such file or directory: 'brew'
```

**Solution**:
```bash
# Install Homebrew (macOS/Linux)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Or skip this script on non-brew systems
```

#### 4. Permission Denied

**Problem**:
```
PermissionError: [Errno 13] Permission denied
```

**Solution**:
```bash
# Make script executable
chmod +x script.py

# Or run with python
python script.py

# Check file permissions
ls -la script.py
```

#### 5. Docker Build Failures

**Problem**:
```
ERROR: failed to solve: process "/bin/sh -c pip install -r requirements.txt" did not complete successfully
```

**Solution**:
```bash
# Clear Docker cache
docker system prune -a

# Rebuild without cache
docker build --no-cache -t python-tui-scripts .

# Check Docker version
docker --version  # Ensure Docker is updated
```

#### 6. Vagrant Issues

**Problem**:
```
The box 'generic/alpine38' could not be found
```

**Solution**:
```bash
# Update Vagrant
vagrant version

# Download box manually
vagrant box add generic/alpine38

# Or change box in Vagrantfile
config.vm.box = "ubuntu/focal64"
```

### Debug Mode

Enable verbose output for troubleshooting:

```python
# Add to script
import logging
logging.basicConfig(level=logging.DEBUG)
```

```bash
# Run with Python debug mode
python -v script.py

# Or with trace
python -m trace --trace script.py
```

### Getting Support

1. **Check Documentation**: Review this README and inline code comments
2. **Search Issues**: Look for similar issues on GitHub
3. **Create Issue**: If problem persists, open a new issue with:
   - Operating system and version
   - Python version (`python --version`)
   - Full error message and stack trace
   - Steps to reproduce
   - Expected vs actual behavior

---

## 📄 License

This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2024 Baneeishaque

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 📞 Contact

### Repository Owner

- **GitHub**: [@Baneeishaque](https://github.com/Baneeishaque)
- **Repository**: [Python-TUI-Scripts](https://github.com/Baneeishaque/Python-TUI-Scripts)

### Quick Links

- 🐛 [Report a Bug](https://github.com/Baneeishaque/Python-TUI-Scripts/issues/new?template=bug_report.md)
- 💡 [Request a Feature](https://github.com/Baneeishaque/Python-TUI-Scripts/issues/new?template=feature_request.md)
- 🔒 [Security Policy](https://github.com/Baneeishaque/Python-TUI-Scripts/security/policy)
- 📊 [Project Board](https://github.com/Baneeishaque/Python-TUI-Scripts/projects)

---

## 🙏 Acknowledgments

### Technologies Used

- **Python**: The core language powering all scripts
- **Pillow**: Image processing library
- **gpsoauth**: Google authentication
- **gkeepapi**: Google Keep API client
- **Docker**: Containerization platform
- **Vagrant**: VM provisioning tool
- **Azure Pipelines**: CI/CD platform

### Contributors

Thank you to all contributors who have helped improve this project!

<!-- Add contributors list here -->

### Inspiration

This project was inspired by the need for simple, reusable Python scripts for common automation tasks.

---

## 📈 Roadmap

### Planned Features

- [ ] **Unit Tests**: Comprehensive test coverage
- [ ] **CLI Interface**: Unified command-line interface for all scripts
- [ ] **Configuration Files**: YAML/JSON config support
- [ ] **Logging Framework**: Structured logging across all scripts
- [ ] **Error Handling**: Improved error messages and recovery
- [ ] **Documentation**: API documentation with Sphinx
- [ ] **Package Distribution**: PyPI package for easy installation
- [ ] **More Scripts**: Additional utility scripts
  - [ ] File organization automation
  - [ ] Network diagnostics
  - [ ] System monitoring
  - [ ] Database utilities

### Version History

- **v1.0.0** (Current): Initial collection of scripts
- **v0.2.0**: Added gkeepapi integration
- **v0.1.0**: Initial repository setup

---

## 🌟 Star History

If you find this project useful, please consider giving it a star! ⭐

[![Star History Chart](https://api.star-history.com/svg?repos=Baneeishaque/Python-TUI-Scripts&type=Date)](https://star-history.com/#Baneeishaque/Python-TUI-Scripts&Date)

---

<div align="center">

**Made with ❤️ by [Baneeishaque](https://github.com/Baneeishaque)**

[⬆ Back to Top](#-python-tui-scripts)

</div>
