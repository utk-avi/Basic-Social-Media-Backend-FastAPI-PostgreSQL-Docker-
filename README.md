# 📝 Social Media Backend (FastAPI + PostgreSQL + Docker)

This project is a backend service for a simple social media style application where users can create, view, update, and delete posts. The application is built using **FastAPI** and **SQLAlchemy**, with **PostgreSQL** as the database, and is fully containerized using **Docker and Docker Compose**.

The goal of this project is to demonstrate how to build and deploy a production-style REST API with persistent storage and proper service separation.

---

## 🚀 Features

The backend provides the following RESTful APIs:

* **Create a post**
* **Get all posts**
* **Get a post by ID**
* **Update a post**
* **Delete a post**

All data is stored in PostgreSQL and persists across container restarts using Docker volumes.

---

## 🛠 Tech Stack

* **FastAPI** – REST API framework
* **SQLAlchemy** – ORM for database modeling and queries
* **PostgreSQL** – Relational database
* **Docker** – Containerization
* **Docker Compose** – Multi-container orchestration
* **Uvicorn** – ASGI server

---

## 🏗 Project Architecture

The application runs as two services:

* **API service** – FastAPI application running inside a Docker container
* **Database service** – PostgreSQL running in a separate Docker container

Docker Compose connects both services on a private network and exposes the API on port **8000**.

---

## ▶️ How to Run

Make sure Docker and Docker Compose are installed.

From the project root, run:

```
docker compose up --build
```

Once the containers start, open:

```
http://localhost:8000/docs
```

This opens the Swagger UI where you can test all API endpoints.

---

## 🧪 Using the API

Example request to create a post:

```
POST /post
{
  "title": "My first post",
  "content": "This is stored in PostgreSQL",
  "published": true
}
```

Example request to fetch all posts:

```
GET /post
```

---

## 💾 Data Persistence

The PostgreSQL data is stored in a Docker volume, so posts remain even after stopping and restarting the containers.

---

## 🎯 Purpose

This project demonstrates how to build a real-world backend using FastAPI and PostgreSQL and how to deploy it in a reproducible and production-like environment using Docker.

It serves as a foundation for more advanced systems such as recommendation engines, authentication systems, or machine learning–powered services.
