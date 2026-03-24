import requests

def get_repo_data(repo_url):

    parts = repo_url.strip("/").split("/")
    owner = parts[-2]
    repo = parts[-1]

    api_url = f"https://api.github.com/repos/{owner}/{repo}"

    response = requests.get(api_url)
    data = response.json()

    return {
        "name": data.get("name"),
        "description": data.get("description"),
        "language": data.get("language"),
        "stars": data.get("stargazers_count"),
        "repo_url": data.get("html_url"),
        "owner": data.get("owner", {}).get("login"),
        "avatar": data.get("owner", {}).get("avatar_url"),
    }