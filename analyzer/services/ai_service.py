import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


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

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content