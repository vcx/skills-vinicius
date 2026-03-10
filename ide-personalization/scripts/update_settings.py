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
            # Handle comments in settings.json which is common in VS Code
            # Very basic comment removal
            try:
                with open(file_path, 'r') as f:
                    content = f.read()
                    # Remove // comments
                    lines = [line.split('//')[0] for line in content.splitlines()]
                    data = json.loads('\n'.join(lines))
            except Exception as e:
                print(f"Error decoding {file_path}: {e}. Starting with empty settings.")

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
