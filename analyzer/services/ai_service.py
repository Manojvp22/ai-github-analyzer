import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def analyze_repository(repo):

    prompt = f"""
    Analyze this GitHub repository.

    Project Name: {repo['name']}
    Description: {repo['description']}
    Language: {repo['language']}

    Provide:
    1. Short project summary
    2. Technologies used
    3. Possible improvements
    4. LinkedIn post about the project
    """

    response = client.responses.create(
        model="gpt-4.1",
        input=prompt
    )

    return response.output_text