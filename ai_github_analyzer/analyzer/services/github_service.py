import requests


def get_repo_data(repo_url):

    parts = repo_url.strip("/").split("/")
    owner = parts[-2]
    repo = parts[-1]

    # repo information
    repo_api = f"https://api.github.com/repos/{owner}/{repo}"

    repo_response = requests.get(repo_api)
    repo_data = repo_response.json()

    # README file
    readme_api = f"https://api.github.com/repos/{owner}/{repo}/readme"

    readme_response = requests.get(
        readme_api,
        headers={"Accept": "application/vnd.github.raw"}
    )

    readme_content = ""

    if readme_response.status_code == 200:
        readme_content = readme_response.text

    return {
        "name": repo_data.get("name"),
        "description": repo_data.get("description"),
        "language": repo_data.get("language"),
        "stars": repo_data.get("stargazers_count"),
        "repo_url": repo_data.get("html_url"),
        "owner": repo_data.get("owner", {}).get("login"),
        "avatar": repo_data.get("owner", {}).get("avatar_url"),
        "readme": readme_content[:2000]  # limit text size
    }