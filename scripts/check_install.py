"""
Simple installation check for ScenarioNet / Traffic_automation.

Run from the repo root as:
    python scripts/check_install.py
"""

def main():
    try:
        import scenarionet  # type: ignore
        print("✅ scenarionet import successful.")
        print(f"   scenarionet version: {getattr(scenarionet, '__version__', 'unknown')}")
    except Exception as e:
        print("❌ scenarionet import failed.")
        print("Error details:")
        print(e)


if __name__ == "__main__":
    main()



