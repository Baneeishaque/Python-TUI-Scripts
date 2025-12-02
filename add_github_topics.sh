#!/bin/bash

# Script to add GitHub topics using curl and GitHub CLI
# This script provides multiple methods to add topics to the repository

REPO_OWNER="Baneeishaque"
REPO_NAME="Python-TUI-Scripts"

# Array of recommended topics
TOPICS=(
    "python"
    "python-scripts"
    "automation"
    "cli-tools"
    "utilities"
    "pillow"
    "google-keep"
    "gkeepapi"
    "google-oauth"
    "homebrew"
    "docker"
    "vagrant"
    "azure-pipelines"
    "ci-cd"
    "developer-tools"
    "scripts"
    "python3"
    "image-processing"
    "google-api"
    "devops"
)

# Convert array to JSON format
TOPICS_JSON=$(printf '%s\n' "${TOPICS[@]}" | jq -R . | jq -s .)

echo "Repository: $REPO_OWNER/$REPO_NAME"
echo "Topics to add: ${#TOPICS[@]}"
echo ""

# Method 1: Using GitHub CLI (gh)
method_gh_cli() {
    echo "=== Method 1: Using GitHub CLI (gh) ==="
    
    if ! command -v gh &> /dev/null; then
        echo "Error: GitHub CLI (gh) is not installed"
        echo "Install it from: https://cli.github.com/"
        return 1
    fi
    
    if ! command -v jq &> /dev/null; then
        echo "Error: jq is not installed"
        echo "Install it: brew install jq (macOS) or apt-get install jq (Linux)"
        return 1
    fi
    
    echo "Using GitHub CLI to set topics..."
    gh api --method PUT "/repos/$REPO_OWNER/$REPO_NAME/topics" \
        -H "Accept: application/vnd.github+json" \
        -f names="$TOPICS_JSON"
    
    if [ $? -eq 0 ]; then
        echo "✓ Topics set successfully using gh CLI!"
        return 0
    else
        echo "✗ Failed to set topics using gh CLI"
        return 1
    fi
}

# Method 2: Using curl with GitHub API
method_curl() {
    echo "=== Method 2: Using curl with GitHub API ==="
    
    if [ -z "$GITHUB_TOKEN" ]; then
        echo "Error: GITHUB_TOKEN environment variable is not set"
        echo "Set it with: export GITHUB_TOKEN='your_token_here'"
        return 1
    fi
    
    if ! command -v curl &> /dev/null; then
        echo "Error: curl is not installed"
        return 1
    fi
    
    if ! command -v jq &> /dev/null; then
        echo "Error: jq is not installed"
        echo "Install it: brew install jq (macOS) or apt-get install jq (Linux)"
        return 1
    fi
    
    echo "Using curl to set topics..."
    
    RESPONSE=$(curl -s -X PUT \
        -H "Accept: application/vnd.github+json" \
        -H "Authorization: token $GITHUB_TOKEN" \
        -H "Content-Type: application/json" \
        -d "{\"names\": $TOPICS_JSON}" \
        "https://api.github.com/repos/$REPO_OWNER/$REPO_NAME/topics")
    
    if echo "$RESPONSE" | jq -e '.names' > /dev/null 2>&1; then
        echo "✓ Topics set successfully using curl!"
        echo "Topics:"
        echo "$RESPONSE" | jq -r '.names[]' | sed 's/^/  - /'
        return 0
    else
        echo "✗ Failed to set topics using curl"
        echo "Response: $RESPONSE"
        return 1
    fi
}

# Method 3: Display topics list
method_display() {
    echo "=== Recommended Topics ==="
    echo "Total: ${#TOPICS[@]} topics"
    echo ""
    for topic in "${TOPICS[@]}"; do
        echo "  - $topic"
    done
    echo ""
    echo "JSON format:"
    echo "$TOPICS_JSON" | jq .
}

# Main menu
show_menu() {
    echo ""
    echo "Choose a method to add GitHub topics:"
    echo "  1) GitHub CLI (gh) - Requires: gh, jq"
    echo "  2) curl + API - Requires: curl, jq, GITHUB_TOKEN"
    echo "  3) Display topics only"
    echo "  4) Exit"
    echo ""
}

# Main execution
main() {
    if [ "$1" == "--auto" ]; then
        # Try methods in order
        method_gh_cli || method_curl || method_display
    elif [ "$1" == "--gh" ]; then
        method_gh_cli
    elif [ "$1" == "--curl" ]; then
        method_curl
    elif [ "$1" == "--display" ]; then
        method_display
    else
        # Interactive mode
        while true; do
            show_menu
            read -p "Enter choice [1-4]: " choice
            case $choice in
                1) method_gh_cli; break ;;
                2) method_curl; break ;;
                3) method_display; break ;;
                4) echo "Exiting..."; exit 0 ;;
                *) echo "Invalid choice. Please try again." ;;
            esac
        done
    fi
}

# Show usage if --help
if [ "$1" == "--help" ] || [ "$1" == "-h" ]; then
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  --auto      Try methods automatically (gh -> curl -> display)"
    echo "  --gh        Use GitHub CLI method"
    echo "  --curl      Use curl + API method (requires GITHUB_TOKEN)"
    echo "  --display   Display topics only"
    echo "  --help, -h  Show this help message"
    echo ""
    echo "Interactive mode runs if no options provided."
    echo ""
    echo "Examples:"
    echo "  $0 --gh"
    echo "  GITHUB_TOKEN=ghp_xxx $0 --curl"
    echo "  $0 --auto"
    exit 0
fi

main "$@"
