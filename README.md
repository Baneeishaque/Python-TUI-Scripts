<div align="center">

# 🐍 Python TUI Scripts

<img src="logo.png" alt="Python TUI Scripts Logo" width="150" height="150">

**A collection of utility Python scripts for terminal/console operations**

[![Python 3.10](https://img.shields.io/badge/Python-3.10-blue.svg?logo=python&logoColor=white)](https://www.python.org/downloads/)
[![License](https://img.shields.io/github/license/Baneeishaque/Python-TUI-Scripts)](LICENSE)
[![Azure Pipelines](https://img.shields.io/azure-devops/build/baneeishaque/Python-TUI-Scripts/Python-TUI-Scripts)](https://dev.azure.com/baneeishaque/Python-TUI-Scripts/_build)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)](Dockerfile)
[![Vagrant](https://img.shields.io/badge/Vagrant-Ready-1563FF?logo=vagrant&logoColor=white)](Vagrantfile)

<a href="https://gitpod.io/#https://github.com/Baneeishaque/Python-TUI-Scripts"><img src="https://img.shields.io/badge/Gitpod-Open%20in%20IDE-FFAE33?logo=gitpod&logoColor=white" alt="Open in Gitpod"></a>
<a href="https://github1s.com/Baneeishaque/Python-TUI-Scripts"><img src="https://img.shields.io/badge/Github1s-Browse%20Code-0078D7?logo=github&logoColor=white" alt="Open in Github1s"></a>

[![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.svg)](https://ssh.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https://github.com/Baneeishaque/Python-TUI-Scripts)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Scripts Documentation](#-scripts-documentation)
- [Technical Stack](#-technical-stack)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Development Environment](#-development-environment)
- [Project Structure](#-project-structure)
- [Configuration Files](#-configuration-files)
- [Contributing](#-contributing)
- [Troubleshooting](#-troubleshooting)
- [Security](#-security)
- [Changelog](#-changelog)

---

## 🎯 Overview

**Python TUI Scripts** is a curated collection of Python utility scripts designed for terminal and console operations. These scripts provide various functionalities ranging from system utilities, authentication helpers, to image processing tools. The project is containerized for easy deployment and includes multiple development environment options.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🍺 **Homebrew Tap Auditor** | Audit and validate Homebrew taps with reachability checks |
| 🖼️ **Logo Generator** | Create custom letter-based logos using PIL |
| 🔐 **Google Authentication** | Scripts for Google OAuth and Keep API authentication |
| 📁 **Pip Cache Inspector** | Display pip and wheel cache directories |
| ⏱️ **Infinite Runner** | Simple infinite loop script for testing and monitoring |
| 🐳 **Docker Support** | Containerized deployment ready |
| 📦 **Vagrant Support** | Local development VM configuration |
| ☁️ **Cloud Ready** | Google Cloud Shell integration |

---

## 📜 Scripts Documentation

### 1. `brew_tap_audit.py`

**Purpose:** Audits Homebrew taps for accessibility and lists installed formulae/casks from each tap.

**Features:**
- Retrieves all configured Homebrew taps
- Checks URL reachability for each tap's GitHub repository
- Groups installed formulae and casks by their source tap
- Provides detailed output with status indicators

**Usage:**
```bash
python brew_tap_audit.py
```

**Sample Output:**
```
Found 5 taps. Checking accessibility and usage...

[OK] homebrew/core (https://github.com/Homebrew/homebrew-core) is reachable
 ↳ Formulae: git, python, node
[OK] homebrew/cask (https://github.com/Homebrew/homebrew-cask) is reachable
 ↳ Casks: visual-studio-code, docker
```

**Requirements:** macOS with Homebrew installed

---

### 2. `create_letter_logo.py`

**Purpose:** Generates a custom logo image with specified letters using the Python Imaging Library (PIL).

**Features:**
- Creates transparent PNG logos
- Customizable letter content
- Auto-scaling based on existing logo dimensions
- White background with centered black text

**Usage:**
```bash
python create_letter_logo.py
```

**Configuration:**
- Modify the `text` variable (default: "DL") to change the letters
- Adjust `font_size` calculation for different text sizes
- Change `font` path for different fonts

**Output:** Creates `logo_new.png` in the project directory

**Requirements:** PIL/Pillow, Arial font (or modify font path)

---

### 3. `gkeepapi_script.py`

**Purpose:** Demonstrates Google Keep API integration for creating and managing notes.

**Status:** ⚠️ Requires valid authentication (BadAuthentication error with placeholder credentials)

**Features:**
- Create new notes with title and content
- Pin notes to the top
- Set note colors
- Sync changes with Google Keep

**Usage:**
```bash
# Replace credentials first
python gkeepapi_script.py
```

**Setup Required:**
1. Obtain a master token for your Google account
2. Replace `'user@gmail.com'` with your email
3. Replace `master_token` with your actual token

---

### 4. `gpsoauth_script.py`

**Purpose:** Demonstrates Google Play Services OAuth authentication flow.

**Status:** ⚠️ May not work with 2FA-enabled accounts

**Features:**
- Performs master login with email/password
- Retrieves master token
- Executes OAuth token exchange

**Usage:**
```bash
# Configure credentials first
python gpsoauth_script.py
```

---

### 5. `gpsoauth_script_alternative.py`

**Purpose:** Alternative OAuth flow using pre-existing OAuth token exchange.

**Features:**
- Token exchange without password
- Useful when you already have an OAuth token
- Service-specific authentication (e.g., Google Play Music)

**Usage:**
```bash
# Insert oauth_token first
python gpsoauth_script_alternative.py
```

---

### 6. `infinteRun.py`

**Purpose:** Simple infinite loop script that prints a message every minute.

**Use Cases:**
- Keep-alive scripts
- Connection testing
- Process monitoring placeholder
- CI/CD timeout testing

**Usage:**
```bash
python infinteRun.py
```

**Behavior:** Prints "This prints once a minute." every 60 seconds indefinitely.

---

### 7. `pip_cache_directories.py`

**Purpose:** Displays the cache directory locations for pip and wheel.

**Features:**
- Uses pip's internal API to retrieve accurate paths
- Cross-platform compatible
- Useful for cache management and debugging

**Usage:**
```bash
python pip_cache_directories.py
```

**Sample Output:**
```
/Users/username/Library/Caches/pip
/Users/username/Library/Caches/wheel
```

---

## 🛠️ Technical Stack

| Component | Technology | Version |
|-----------|------------|---------|
| **Language** | Python | 3.10.16 |
| **Image Processing** | Pillow | 11.1.0 |
| **Google Auth** | gpsoauth | 2.0.0 |
| **Google Keep API** | gkeepapi | 0.17.0 |
| **Package Manager** | pip | 24.3.1 |
| **Container Runtime** | Docker | Alpine 3.8 |
| **VM Provider** | Vagrant | Generic Alpine 38 |
| **CI/CD** | Azure Pipelines | Latest |
| **Version Manager** | mise | - |

---

## 📋 Prerequisites

### System Requirements

- **Python:** 3.10+ (managed via [mise](https://mise.jdx.dev/))
- **pip:** Latest version recommended
- **Git:** For cloning the repository

### Optional Requirements

| Tool | Purpose | Installation |
|------|---------|--------------|
| Docker | Containerized execution | [Install Docker](https://docs.docker.com/get-docker/) |
| Vagrant | Local VM development | [Install Vagrant](https://www.vagrantup.com/downloads) |
| VirtualBox | Vagrant provider | [Install VirtualBox](https://www.virtualbox.org/wiki/Downloads) |
| Homebrew | For `brew_tap_audit.py` | [Install Homebrew](https://brew.sh/) |
| mise | Python version management | [Install mise](https://mise.jdx.dev/getting-started.html) |

---

## 📥 Installation

### Method 1: Local Installation

```bash
# Clone the repository
git clone https://github.com/Baneeishaque/Python-TUI-Scripts.git
cd Python-TUI-Scripts

# (Optional) Setup Python version with mise
mise install

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/macOS:
source venv/bin/activate
# On Windows:
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Method 2: Docker

```bash
# Clone the repository
git clone https://github.com/Baneeishaque/Python-TUI-Scripts.git
cd Python-TUI-Scripts

# Build the Docker image
docker build -t python-tui-scripts .

# Run a script (default: pip_cache_directories.py)
docker run python-tui-scripts

# Run a specific script
docker run python-tui-scripts python ./brew_tap_audit.py
```

### Method 3: Vagrant

```bash
# Clone the repository
git clone https://github.com/Baneeishaque/Python-TUI-Scripts.git
cd Python-TUI-Scripts

# Start the Vagrant VM
vagrant up

# SSH into the VM
vagrant ssh

# Navigate to the project
cd /vagrant

# Run scripts
python pip_cache_directories.py
```

### Method 4: Cloud IDEs

#### Gitpod
Click the badge below to open in Gitpod:

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/Baneeishaque/Python-TUI-Scripts)

#### Google Cloud Shell
Click the button below to open in Cloud Shell:

[![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.svg)](https://ssh.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https://github.com/Baneeishaque/Python-TUI-Scripts)

#### GitHub1s (Browser-based code browsing)

[![Open in Github1s](https://img.shields.io/badge/Github1s-Browse%20Code-0078D7?logo=github&logoColor=white)](https://github1s.com/Baneeishaque/Python-TUI-Scripts)

---

## 🚀 Quick Start

After installation, run any script directly:

```bash
# Display pip cache directories
python pip_cache_directories.py

# Create a logo
python create_letter_logo.py

# Audit Homebrew taps (macOS only)
python brew_tap_audit.py

# Run infinite loop (Ctrl+C to stop)
python infinteRun.py
```

---

## 💻 Development Environment

### IDE Recommendations

| IDE | Configuration |
|-----|---------------|
| **VS Code** | `.vscode/` settings supported |
| **PyCharm/IntelliJ** | `.idea/` configurations included |

### Version Management with mise

The project uses [mise](https://mise.jdx.dev/) for Python version management:

```bash
# Install mise
curl https://mise.run | sh

# Install the required Python version
mise install

# Verify Python version
python --version  # Should output: Python 3.10.16
```

### Environment Setup Script

```bash
#!/bin/bash
# Quick setup script

# Clone repository
git clone https://github.com/Baneeishaque/Python-TUI-Scripts.git
cd Python-TUI-Scripts

# Setup Python with mise (optional)
mise install 2>/dev/null || echo "mise not installed, using system Python"

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

echo "Setup complete! Run scripts with: python <script_name>.py"
```

---

## 📁 Project Structure

```
Python-TUI-Scripts/
├── 📄 README.md                    # This file
├── 📄 requirements.txt             # Python dependencies
├── 📄 mise.toml                    # mise Python version config
│
├── 🐍 Scripts
│   ├── brew_tap_audit.py           # Homebrew tap auditor
│   ├── create_letter_logo.py       # Logo generator
│   ├── gkeepapi_script.py          # Google Keep API demo
│   ├── gpsoauth_script.py          # Google OAuth script
│   ├── gpsoauth_script_alternative.py # Alternative OAuth flow
│   ├── infinteRun.py               # Infinite loop script
│   └── pip_cache_directories.py    # Pip cache path finder
│
├── 🐳 Containerization
│   ├── Dockerfile                  # Docker image definition
│   ├── .dockerignore               # Docker build exclusions
│   └── Vagrantfile                 # Vagrant VM configuration
│
├── 🔧 CI/CD
│   └── azure-pipelines.yml         # Azure DevOps pipeline
│
├── 🔒 Security & Dependencies
│   ├── .pyup.yml                   # PyUp.io configuration
│   ├── .whitesource                # WhiteSource security config
│   └── renovate.json               # Renovate dependency updates
│
├── 🎨 Assets
│   └── logo.png                    # Project logo
│
└── 📝 IDE Configurations
    ├── .gitignore                  # Git exclusions
    └── .idea/                      # JetBrains IDE settings
```

---

## ⚙️ Configuration Files

### `requirements.txt`
Python package dependencies:
```
pip==24.3.1          # Package installer
pillow==11.1.0       # Image processing library
gpsoauth==2.0.0      # Google Play Services OAuth
gkeepapi==0.17.0     # Google Keep API client
```

### `mise.toml`
Python version specification:
```toml
[tools]
python = "3.10.16"
```

### `Dockerfile`
Containerized environment based on Alpine Linux:
```dockerfile
FROM python:3.7.3-alpine3.8
WORKDIR /usr/src/app
COPY . .
CMD [ "python", "./pip_cache_directories.py" ]
```

### `Vagrantfile`
Local development VM with Alpine Linux:
- Base box: `generic/alpine38`
- Network: Public network enabled
- Provisioning: Python and pip pre-installed

### `azure-pipelines.yml`
CI/CD configuration for Azure DevOps:
- Trigger: master branch
- Action: Docker image build
- Platform: Ubuntu latest

### `.pyup.yml`
Dependency monitoring configuration:
- Pin mode: Disabled (allows minor updates)
- Schedule: Daily checks

### `.whitesource`
Security scanning configuration:
- Vulnerable checks: Failure on detection
- Minimum severity: HIGH

### `renovate.json`
Automated dependency updates via Renovate Bot

---

## 🤝 Contributing

We welcome contributions! Please follow these guidelines:

### Getting Started

1. **Fork the repository**
   ```bash
   # Click "Fork" on GitHub, then:
   git clone https://github.com/YOUR_USERNAME/Python-TUI-Scripts.git
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Set up the development environment**
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

### Code Guidelines

| Aspect | Guideline |
|--------|-----------|
| **Python Version** | 3.10+ |
| **Style Guide** | [PEP 8](https://pep8.org/) |
| **Docstrings** | [PEP 257](https://peps.python.org/pep-0257/) |
| **Type Hints** | Encouraged for new code |
| **Imports** | Use standard library first, then third-party |

### Adding a New Script

1. Create your Python script in the root directory
2. Add any new dependencies to `requirements.txt`
3. Update this README with documentation
4. Test locally and with Docker

### Commit Message Format

```
<type>: <short summary>

<optional body>

<optional footer>
```

**Types:** `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

**Examples:**
```
feat: add new script for git repository analysis
fix: correct import path in brew_tap_audit.py
docs: update README with installation instructions
```

### Pull Request Process

1. **Ensure tests pass** (if applicable)
2. **Update documentation** for new features
3. **Test with Docker** to ensure containerization works
4. **Create a descriptive PR** with:
   - Summary of changes
   - Related issue numbers
   - Screenshots (if UI-related)

### Reporting Issues

- Use GitHub Issues
- Include Python version, OS, and error messages
- Provide steps to reproduce the issue

---

## 🔧 Troubleshooting

### Common Issues

#### 1. `ModuleNotFoundError: No module named 'PIL'`
```bash
pip install pillow
```

#### 2. `brew: command not found`
The `brew_tap_audit.py` script requires macOS with Homebrew:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

#### 3. Font not found error in `create_letter_logo.py`
Modify the font path in the script:
```python
# Change from:
font = ImageFont.truetype("/Library/Fonts/Arial.ttf", font_size)
# To a font available on your system:
font = ImageFont.truetype("/path/to/your/font.ttf", font_size)
```

#### 4. Google Authentication Errors
- Ensure 2FA is not interfering with OAuth
- Generate an app-specific password if needed
- Obtain a valid master token for gkeepapi

#### 5. Docker build fails
```bash
# Ensure Docker is running
docker info

# Clean and rebuild
docker system prune -f
docker build --no-cache -t python-tui-scripts .
```

---

## 🔒 Security

This project uses multiple security tools:

| Tool | Purpose |
|------|---------|
| **WhiteSource** | Vulnerability scanning |
| **PyUp.io** | Python dependency monitoring |
| **Renovate** | Automated dependency updates |

### Security Best Practices

- ⚠️ Never commit credentials or tokens
- 🔐 Use environment variables for sensitive data
- 📝 Review dependency updates before merging
- 🔍 Run security scans regularly

---

## 📝 Changelog

See [GitHub Releases](https://github.com/Baneeishaque/Python-TUI-Scripts/releases) for version history.

---

## 📄 License

This project is open source. See the repository for license details.

---

## 👤 Author

**Baneeishaque**
- GitHub: [@Baneeishaque](https://github.com/Baneeishaque)

---

<div align="center">

**⭐ If you find this project useful, please consider giving it a star! ⭐**

Made with ❤️ and Python 🐍

</div>
