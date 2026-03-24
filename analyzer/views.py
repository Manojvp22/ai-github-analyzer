from django.shortcuts import render
from .services.github_service import get_repo_data
from .services.ai_service import analyze_repository


def index(request):

    result = None
    ai_output = None

    if request.method == "POST":

        repo_url = request.POST.get("repo_url")

        repo_data = get_repo_data(repo_url)

        ai_output = analyze_repository(repo_data)

        result = repo_data

    return render(
        request,
        "index.html",
        {
            "result": result,
            "ai_output": ai_output
        }
    )