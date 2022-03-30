import os


def main():
    github_actions = os.getenv("GITHUB_ACTIONS")
    print(f"GITHUB_ACTIONS: {github_actions}")

if __name__ == "__main__":
    main()