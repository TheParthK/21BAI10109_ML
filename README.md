# 21BAI10109
# Document Retrieval System (Parth Kalia)

## Overview

This project creates a Document Retrieval System specifically for chat applications. It allows for efficient document fetching and ranking based on user queries. The backend is built using FastAPI, and the system is containerized with Docker for easy and scalable deployment.

## Key Features

- Rapid document retrieval using text similarity search.
- Redis caching to enhance response times.
- Rate limiting to prevent API overuse (API responds with HTTP 429 after 5 requests).
- Background news article scraping.
- Fully containerized with Docker for efficient and scalable deployment.

## Setup Guide

### 1. Local Setup

1. **Install the required packages:**

```bash
pip install -r requirements.txt
```


2. *Initialize the database:*


python -c "from app.models import init_db; init_db()"


3. *Run the FastAPI server:*


uvicorn app.api:app --reload


Access the API:

- Health check: http://localhost:8000/health
- API docs: http://localhost:8000/docs

## 2. Docker Setup

1. Build the Docker image:


docker build -t document-retrieval


2. Run the Docker container:


docker run -p 8000:8000 document-retrieval


## 3. Design Choices

- FastAPI: For high performance and auto-generated documentation
- SQLite: For simplicity; can be switched to PostgreSQL for production
- Redis: For caching and optimization
### Collaborator
- recruitments@trademarkia.com
