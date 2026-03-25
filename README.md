# 🚀 AI GitHub Repository Analyzer

A Django-based web application that analyzes GitHub repositories and generates **AI-powered insights** such as project summaries, technology stack explanations, improvement suggestions, and LinkedIn-ready posts.

---

# 📌 Project Overview

AI GitHub Repository Analyzer allows users to enter a **GitHub repository URL** and instantly receive insights about the project.

The system fetches repository metadata and README content using the GitHub API and then uses an **LLM (Large Language Model)** to generate intelligent insights about the project.

This project demonstrates **modern backend architecture, API integration, and AI-powered analysis** in a clean web dashboard.

---

# ✨ Features

🔍 Analyze any public GitHub repository
📄 Fetch repository metadata using the GitHub API
📘 Automatically read and analyze README.md
🤖 Generate AI-powered project insights
💡 Suggest improvements for the project
📢 Generate LinkedIn-ready post summaries
📋 Copy AI-generated content with a single click
🎨 Modern responsive UI built with TailwindCSS

---

# 🛠 Tech Stack

### Backend

* Python
* Django

### APIs

* GitHub REST API
* Groq API

### AI Model

* Llama 3

### Frontend

* HTML
* Tailwind CSS

---

# ⚙️ How It Works

1. User enters a GitHub repository URL.
2. Django backend processes the request.
3. GitHub API fetches repository details and README content.
4. The AI service sends the repository data to the LLM.
5. The LLM generates intelligent insights about the repository.
6. Results are displayed in the web dashboard.

---

# 🧠 System Architecture

User Input
⬇
Django Views
⬇
GitHub API Service
⬇
AI Analysis Service
⬇
Groq LLM (Llama3)
⬇
Dashboard Output

---

# 🚀 Installation

Clone the repository:

```
git clone https://github.com/Manojvp22/ai-github-analyzer.git
```

Navigate into the project folder:

```
cd ai-github-analyzer
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the development server:

```
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root and add your Groq API key.

Example:

```
GROQ_API_KEY=your_groq_api_key_here
```

Make sure `.env` is added to `.gitignore` so your API key is not exposed.

---


# 🎯 Learning Outcomes

This project demonstrates:

* Django backend development
* API integration
* LLM integration
* Prompt engineering
* Environment variable management
* Modern UI design
* Service-layer architecture

---

# 📌 Future Improvements

* Detect technologies from `requirements.txt` automatically
* Analyze repository folder structure
* Show contributor statistics
* Add repository code explanation
* Deploy the application online

---

# 👨‍💻 Author

**Manoj V Poojar**
Electronics and Communication Engineering Graduate
Aspiring AI & Software Developer

---

# ⭐ If you like this project

Give it a ⭐ on GitHub!
