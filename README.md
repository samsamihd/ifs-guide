# IFS Guide

IFS Guide is a mock AI-powered chat application with a RESTful API built on top of FastAPI and using SQLAlchemy with PostgreSQL for data storage.

## Getting Started

### Prerequisites

- Docker

### Run Docker Container

Run a Docker container from the built image:

```bash
docker-compose up --build
```

### Access the FastAPI Application

Visit [http://localhost:8000](http://localhost:8000/docs) in your web browser or use tools like `curl` or `Postman` to interact with the API.

### Endpoints
#### Interactions
- POST /interactions - Create a new interaction
- GET /interactions - Get all interactions
#### Messages
- POST /interactions/{id}/messages - Create a message in an interaction
- GET /interactions/{id}/messages - Get all messages in an interaction