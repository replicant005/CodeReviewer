# CodeGuard – AI Code Security Reviewer 

## Overview

**CodeGuard** is an AI-powered code security reviewer built using an MCP server and a locally hosted LLM via Ollama.
The system allows AI coding assistants (cursor) to send code snippets to a server that analyzes them for potential security vulnerabilities, bad practices, and risky patterns.


# How it works 

The system contains two main services.

The MCP Client access the MCP Server (CodeGuard), sends prompts to Local LLM (qwen2.5-coder) using the Ollama API and returns security analysis of the code sent by Client. 


### Key Files

**server.py**

Runs the MCP server and exposes tools for code review.

**ollama_client.py**

Handles communication with the Ollama API.

**Dockerfile**

Builds the MCP server container.

**docker-compose.yml**

Runs both services together.

**test_server.py**

Contains unit tests for the Ollama client logic.


# Running the Project

## Install the following:

* Docker
* Docker Compose
* Python 3.11+

From the project directory run:

```
docker compose up
```

Docker will:

1. Build the MCP server image
2. Pull the Ollama image
3. Start both containers
4. Connect them on a shared network

Go to cursor and press control shift p
then add this to the mcp and tools 

```
{
  "mcpServers": {
    "code-guardian": {
      "command": "path to python/python.exe",
      "args": ["path to server/server.py"]
    }
  }
}

```


# Running Tests

Install test dependencies:

```
pip install pytest
```

Run tests:

```
pytest
```

Tests include checks for:

* Successful LLM responses
* Network failures
* Invalid API responses
* Incorrect endpoint usage
* Model errors
* Prompt formatting

These tests ensure the client behaves correctly even when the API fails.


# Learning Goals of the Project

This project helps demonstrate:

* REST API integration
* AI service architecture
* Docker container orchestration
* MCP server development
* unit testing strategies
* mocking external services

# Possible Future Improvements

* Add a web dashboard
* Support multiple models
* Add caching for responses
