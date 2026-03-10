# Test Plan: ide-personalization

## Scenario 1: Apply default colors to a new workspace
1. Create a dummy directory `test_workspace`.
2. Run the skill to apply default colors.
3. Verify `.vscode/settings.json` is created with the correct colors.

## Scenario 2: Merge colors into existing settings
1. Create a `.vscode/settings.json` with some existing settings.
2. Run the skill to apply new colors.
3. Verify that existing settings are preserved and new colors are added/updated.

## Verification Commands
```bash
# Check if settings.json exists and has content
cat .vscode/settings.json | python3 -c "import sys, json; data = json.load(sys.stdin); print(data['workbench.colorCustomizations']['statusBar.background'] == '#FC3')"
```
