import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def analyze_repository(repo):

    prompt = f"""
    Analyze this GitHub repository.

    Project Name: {repo['name']}
    Description: {repo['description']}
    Language: {repo['language']}

    README CONTENT:
    {repo['readme']}

    Provide:
    1. Project summary
    2. Technologies used
    3. Possible improvements
    4. LinkedIn post about this project
    """

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text