# MoodDetector API — GitHub Actions CI/CD Lab

This project is a refreshed and extended version of the GitHub Actions Labs (Lab 1 + Lab 2).  
It uses a small FastAPI sentiment analysis service to demonstrate how CI pipelines are built, tested, and automated using GitHub Actions.

The goal was to take the original lab and enhance it with cleaner structure, automated tests, linting, documentation, multi-version testing, and artifact publishing — making it production-style and portfolio-ready.

---

## 🚀 What This Project Includes

### ✔ FastAPI application
A lightweight API with two endpoints:

- **GET `/health`** — basic health check  
- **POST `/predict`** — returns simple sentiment: `positive`, `negative`, or `neutral`

### ✔ Automated CI Pipeline (GitHub Actions)
Every push and pull request triggers:

- **Linting** (flake8)  
- **Unit tests** (pytest)  
- **Coverage reports**  
- **Python 3.10 & 3.11 test matrix**  
- **Artifact uploads per Python version**  
- **Documentation build** (MkDocs)

### ✔ Documentation Build Pipeline
MkDocs automatically builds and uploads documentation artifacts.

---

## 📁 Project Structure

