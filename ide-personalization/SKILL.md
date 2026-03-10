---
name: ide-personalization
description: >
  Personalizes the IDE (VS Code) interface by customizing status bar colors. 
  Use when starting isolated environments like git worktrees or when the user 
  wants to visually distinguish different project windows. Similar to "Peacock" extension.
  Don't use for general theme changes or editor font settings.
---

# IDE Personalization

This skill helps visually distinguish different IDE windows by applying unique colors to the status bar. This is particularly useful for git worktrees or multiple open projects.

## Quick Recipes

### Apply Status Bar Colors to Current Workspace

To apply the colors to the current workspace (using `.vscode/settings.json`):

1. **Colors**: Define the colors. Default example:
   - `statusBarItem.remoteBackground`: `#ff5722` (Orange)
   - `statusBarItem.remoteForeground`: `#ffffff` (White)
   - `statusBar.background`: `#FC3` (Yellow)

2. **Update Settings**: Use the bundled script to merge these into the workspace settings.

```bash
python3 scripts/update_settings.py --path .vscode/settings.json --colors '{"workbench.colorCustomizations": {"statusBarItem.remoteBackground": "#ff5722", "statusBarItem.remoteForeground": "#ffffff", "statusBar.background": "#FC3"}}'
```

## Gotchas and Pitfalls

- **Local vs Global**: Always prefer workspace-level settings (`.vscode/settings.json`) to avoid affecting all IDE windows.
- **Git Ignore**: Be aware that `.vscode/settings.json` might be ignored by git. If you want these settings to persist across worktrees but not be committed, ensure the user knows.
- **JSON Format**: Ensure the JSON is valid before writing. Use the provided script to avoid corrupting existing settings.

## Bundled Scripts

### scripts/update_settings.py

This script safely merges color customizations into a VS Code settings file.

```python
import json
import sys
import os
import argparse

def merge_settings(file_path, new_settings):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    data = {}
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
        except json.JSONDecodeError:
            print(f"Error decoding {file_path}. Starting with empty settings.")

    # Merge workbench.colorCustomizations
    if "workbench.colorCustomizations" in new_settings:
        if "workbench.colorCustomizations" not in data:
            data["workbench.colorCustomizations"] = {}
        data["workbench.colorCustomizations"].update(new_settings["workbench.colorCustomizations"])

    # Update other top-level settings if any
    for k, v in new_settings.items():
        if k != "workbench.colorCustomizations":
            data[k] = v

    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Successfully updated {file_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", required=True)
    parser.add_argument("--colors", required=True)
    args = parser.parse_args()
    
    merge_settings(args.path, json.loads(args.colors))
```

## Validation

After applying, verify that `.vscode/settings.json` contains the expected `workbench.colorCustomizations`.

```bash
cat .vscode/settings.json
```
