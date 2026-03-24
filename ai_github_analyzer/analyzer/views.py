from django.shortcuts import render
from .services.github_service import get_repo_data
from .services.ai_service import analyze_repository


def index(request):

    result = None
    ai_output = None

    if request.method == "POST":

        repo_url = request.POST.get("repo_url")

        # Fetch repository data from GitHub
        repo_data = get_repo_data(repo_url)

        result = repo_data

        # Try AI analysis
        try:
            ai_output = analyze_repository(repo_data)

        except Exception:

            # Fallback if AI API fails
            ai_output = f"""
Project Summary
The repository '{repo_data['name']}' appears to be a project written in {repo_data['language']}.

Description
{repo_data['description']}

Possible Improvements
• Improve documentation
• Add modular project structure
• Implement REST APIs

LinkedIn Post
🚀 I built an AI GitHub Repository Analyzer using Django and the GitHub API that can analyze repositories and generate project insights automatically.
"""

    return render(
        request,
        "index.html",
        {
            "result": result,
            "ai_output": ai_output
        }
    )