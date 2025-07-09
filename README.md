# 🧠 Sentiment Analysis Microservice (DevOps + AI)

This project is a lightweight sentiment analysis API that uses a pre-trained transformer model to classify text as **positive**, **negative**, or **neutral**. Built with **FastAPI**, containerized with **Docker**, and deployed using **GitHub Actions CI/CD**.

---

## 🚀 Features

- ✅ `/analyze` POST endpoint
- ✅ Uses Hugging Face Transformer model (no training required)
- ✅ Dockerized for easy deployment
- ✅ GitHub Actions CI/CD:
  - Installs dependencies
  - Runs inference test
  - Builds Docker image

---

## 📦 Tech Stack

| Area           | Tech                     |
|----------------|--------------------------|
| API            | FastAPI (Python)         |
| AI Model       | Hugging Face Transformers |
| DevOps         | Docker + GitHub Actions  |
| CI/CD          | GitHub Actions Workflow  |
| Docs           | Swagger (`/docs`)        |

---

## 📥 Install & Run Locally

### Clone & Setup:
```bash
git clone https://github.com/Abdun-Naffey/sentiment-microservice.git
cd sentiment-microservice
