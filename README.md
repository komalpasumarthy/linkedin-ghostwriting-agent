Sure! Here's the **cleaned-up `README.md`** without any setup or installation instructions — just the high-level overview and project details:

---

# 🤖 LinkedIn Ghostwriter using Vertex AI ADK

This repository showcases a **multi-agent system** built with **Vertex AI’s Agent Development Kit (ADK)**. The system functions as a personalized **LinkedIn Ghostwriter**, helping users craft professional and engaging posts in their unique writing style.

---

## 🚀 Features

* 🔍 **Profile Style Analysis**
  Analyzes a user's LinkedIn profile content (or manually submitted posts) to detect tone, structure, and preferred topics.

* ✍️ **Personalized Post Generation**
  Creates LinkedIn posts from topic ideas or bullet points, mimicking the user's tone and content patterns.

* 🏷️ *Optional Enhancements*

  * Hashtag recommendations
  * Writing style rewrites (formal, casual, concise, etc.)
  * Virality score estimation *(optional)*

---

## 🧱 Tech Stack

* **Vertex AI Agent Development Kit (ADK)**
* **Python** (for tool functions and logic)
* **Large Language Models (LLMs)** with function-calling
* **Google Cloud Platform (GCP)**

---

## 🧠 Architecture Overview

![Architecture Diagram](./assets/architecture.png)

---

## 📝 Workflow

1. User submits a LinkedIn profile or writing samples
2. The **Style Analyzer Agent** identifies tone, structure, and key themes
3. User provides a topic idea or bullet points
4. The **Post Generator Agent** creates a personalized, post-ready output
5. (Optional) Suggestions for hashtags or rewrites are provided

---

## 🔐 Data Privacy

This project is built with user privacy in mind. All writing samples are processed securely, with no external sharing or persistent storage.

---

## 🙌 Acknowledgements

* [Google Cloud Vertex AI](https://cloud.google.com/vertex-ai)
* [Airtribe AI Agent Challenge](https://airtribe.notion.site/)

---

Let me know if you want a matching `LICENSE`, or documentation for how each agent/tool works!
