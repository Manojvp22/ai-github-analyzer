# 🚀 AI GitHub Repository Analyzer

A Django-based web application that analyzes GitHub repositories and generates AI-powered insights such as project summaries, technology stack explanations, improvement suggestions, and LinkedIn-ready posts.

---

## 📌 Project Overview

AI GitHub Repository Analyzer allows users to enter a GitHub repository URL and instantly receive insights about the project. The system fetches repository data and README content using the GitHub API and then generates analysis using AI.

This project demonstrates modern backend architecture, API integration, and AI-assisted analysis in a clean web dashboard.

---

## ✨ Features

* 🔍 Analyze any public GitHub repository
* 📄 Fetch repository metadata using the GitHub API
* 📘 Automatically read and analyze README.md
* 🤖 Generate AI-powered project insights
* 💡 Suggest improvements for the project
* 📢 Generate LinkedIn-ready post summaries
* 📋 Copy AI-generated content with a single click
* 🎨 Modern responsive UI built with TailwindCSS

---

## 🛠 Tech Stack

Backend

* Python
* Django

APIs

* GitHub REST API
* Gemini AI API

Frontend

* HTML
* Tailwind CSS

Tools

* Git
* VS Code

---

## ⚙️ How It Works

1. User enters a GitHub repository URL.
2. Django backend processes the request.
3. GitHub API fetches repository details and README content.
4. AI service analyzes the project data.
5. Insights and suggestions are displayed on the dashboard.

---

## 🧠 System Architecture

User Input
⬇
Django View
⬇
GitHub API Service
⬇
AI Analysis Service
⬇
Dashboard Output

---

## 🚀 Installation

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

Run the server:

```
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000
```

---

## 🔑 Environment Variables

Create an environment variable for your API key.

Example (Windows):

```
setx GEMINI_API_KEY "your_api_key_here"
```

---

## 📷 Screenshot

(Add a screenshot of the dashboard here once deployed.)

---

## 🎯 Learning Outcomes

This project demonstrates:

* Django backend development
* API integration
* AI service integration
* Modern UI design
* Service-layer architecture

---

## 📌 Future Improvements

* Detect technologies from requirements.txt automatically
* Analyze repository folder structure
* Show contributor statistics
* Deploy the application online

---

## 👨‍💻 Author

Manoj V Poojar
Electronics and Communication Engineering Graduate
Aspiring AI & Software Developer

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
