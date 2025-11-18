# MoodDetector API — GitHub Actions CI/CD Lab

This project is my redesigned and significantly expanded version of the GitHub Actions Labs (Lab 1 + Lab 2).  
Instead of repeating the original lab, I built a complete CI workflow around a small FastAPI sentiment analysis API.  
The focus of this project is not the API itself, but the **automation, testing, documentation, and CI pipeline** that surrounds it.

This demonstrates practical CI/CD skills using GitHub Actions — exactly what real engineering teams expect.

---

## 🚀 What This Project Is About

The goal was to take the concepts taught in the GitHub Actions labs and turn them into a real, professional workflow.  
To do this, I created a small API (“MoodDetector”) and integrated it with a full CI pipeline:

- Automated linting  
- Automated testing  
- Multi-version Python test matrix  
- Coverage generation  
- Artifact uploads  
- Documentation build  
- Pre-commit code checks  

Together, this shows a complete CI foundation for an ML or backend project.

---

## 🧠 About the MoodDetector API

The API is intentionally simple — a lightweight FastAPI service with:

- **GET `/health`**  
  Returns a basic health response.

- **POST `/predict`**  
  Accepts text and returns a rule-based sentiment:  
  `positive`, `negative`, or `neutral`.

The simplicity of the API makes it perfect for demonstrating CI/CD concepts without unnecessary complexity.

---

## 🤖 What I Implemented (The Important Part)

### ✔ Fully Automated CI Pipeline (GitHub Actions)
Every push and pull request triggers:

- Setup of Python 3.10 and 3.11  
- Dependency installation  
- Linting using **flake8**  
- Unit tests using **pytest**  
- Coverage report generation  
- Coverage artifacts uploaded per Python version  

This means the entire project is verified automatically on every update — no manual steps.

---
