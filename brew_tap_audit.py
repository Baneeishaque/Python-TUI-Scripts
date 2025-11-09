import subprocess
import urllib.request
import json
from collections import defaultdict

def get_homebrew_taps():
    """Return a list of tap names"""
    try:
        result = subprocess.run(['brew', 'tap'], capture_output=True, text=True, check=True)
        taps = result.stdout.strip().splitlines()
        taps.sort()  # Sort alphabetically for consistent output
        return taps
    except subprocess.CalledProcessError as e:
        print("Error getting taps:", e)
        return []

def get_installed_items(item_type):
    """Return a list of installed formulae or casks"""
    try:
        result = subprocess.run(['brew', 'list', f'--{item_type}'], capture_output=True, text=True, check=True)
        return result.stdout.strip().splitlines()
    except subprocess.CalledProcessError as e:
        print(f"Error getting installed {item_type}:", e)
        return []

def group_items_by_tap(items):
    """Group installed items by actual tap using brew info --json=v2"""
    tap_map = defaultdict(list)
    if not items:
        return tap_map
    
    # Run brew info --json=v2 for all items at once (efficient; v2 supports both formulae and casks)
    try:
        result = subprocess.run(
            ['brew', 'info', '--json=v2'] + items,
            capture_output=True, text=True, check=True
        )
        info_data = json.loads(result.stdout)
        
        # Extract relevant sections
        formulae_info = info_data.get('formulae', [])
        casks_info = info_data.get('casks', [])
        all_info = formulae_info + casks_info
        
        # Assume order matches input items
        for idx, info in enumerate(all_info):
            # Confirm it's installed
            installed = info.get('installed', [])
            if installed and idx < len(items):
                # Tap is top-level in the JSON
                tap = info.get('tap', 'homebrew/core')
                tap_map[tap].append(items[idx])
    except (subprocess.CalledProcessError, json.JSONDecodeError, KeyError) as e:
        print(f"Error grouping items: {e}")
        # Fallback: put all in core
        for item in items:
            tap_map["homebrew/core"].append(item)
    
    return tap_map

def merge_formulae_and_casks(formula_map, cask_map):
    """Combine formulae and casks under each tap"""
    all_taps = set(formula_map) | set(cask_map)
    merged = {}
    for tap in all_taps:
        formulas = formula_map.get(tap, [])
        casks = cask_map.get(tap, [])
        merged[tap] = {
            "formulae": formulas,
            "casks": casks
        }
    return merged

def check_url_reachable(url):
    """Check if a URL is reachable using urllib"""
    try:
        req = urllib.request.Request(url, method='HEAD')
        with urllib.request.urlopen(req, timeout=5) as response:
            return response.status == 200
    except Exception as e:
        # Clean up error message to first line/reason
        error_msg = str(e).splitlines()[0] if str(e) else "Unknown error"
        return f"Error: {error_msg}"

def infer_tap_url(tap_name):
    """Infer GitHub URL from tap name"""
    user, repo = tap_name.split("/")
    return f"https://github.com/{user}/homebrew-{repo}"

def check_tap(tap, installed):
    """Check tap URL and list installed formulae and casks"""
    url = infer_tap_url(tap)
    result = check_url_reachable(url)
    if result is True:
        print(f"[OK] {tap} ({url}) is reachable")
    else:
        print(f"[ERROR] Cannot reach {tap} ({url}): {result}")
    formulas = installed.get("formulae", [])
    casks = installed.get("casks", [])
    if formulas:
        print(f" ↳ Formulae: {', '.join(formulas)}")
    if casks:
        print(f" ↳ Casks: {', '.join(casks)}")
    if not formulas and not casks:
        print(f" ↳ No formulae or casks installed from {tap}")

def main():
    custom_taps = get_homebrew_taps()
    taps = ['homebrew/core', 'homebrew/cask'] + custom_taps
    taps = list(set(taps))  # Remove duplicates if any
    taps.sort()
    formulae = get_installed_items("formula")
    casks = get_installed_items("cask")
    formula_map = group_items_by_tap(formulae)
    cask_map = group_items_by_tap(casks)
    installed_map = merge_formulae_and_casks(formula_map, cask_map)
    if not taps:
        print("No taps found.")
        return
    print(f"Found {len(taps)} taps. Checking accessibility and usage...\n")
    for tap in taps:
        check_tap(tap, installed_map.get(tap, {}))

if __name__ == "__main__":
    main()
