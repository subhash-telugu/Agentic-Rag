# Agentic RAG System with LangGraph

## Overview

This project implements an advanced Retrieval-Augmented Generation (RAG) system that leverages PDFs to answer user queries. It integrates an intelligent agent, powered by LangGraph, that can dynamically decide the best course of action based on the user's query, including when to interact with the knowledge base. The system also utilizes Groq for fast inference.

This project is part of an assignment to build a robust RAG system and extend it with agentic capabilities.

### Assignment Requirements

**Part 1: Building a RAG System**
* Use PDF text as the data source for domain knowledge.
* Chunk and index the PDF content in a VectorDB.
* Serve the RAG system and process user queries via a FastAPI endpoint.

**Part 2: Building an Agent with LangGraph**
* The agent decides when to call the VectorDB based on the user's query.
* The agent can decide the tool to use based on user query and execute it.
* Leverages LangGraph for defining and managing complex conversational flows.

**Part 3: Fast Inference with Groq**
* Integrates Groq for high-speed LLM inference, enhancing response times.

## Features

* **PDF Processing:** Upload PDFs, extract text, and chunk it for indexing into a VectorDB.
* **Agentic RAG:** An intelligent agent orchestrated by LangGraph dynamically decides the best action, such as performing retrieval, rewriting queries, or directly generating responses.
* **LangGraph Integration:** Defines and manages the complex conversational flow, allowing for sophisticated decision-making within the RAG process.
* **Groq Integration:** Utilizes Groq for rapid LLM inference, leading to quicker response times.
* **Dynamic Query Rewriting:** The agent can intelligently rewrite user queries to improve retrieval effectiveness.
* **Contextual Generation:** Generates precise answers based on the retrieved context.
* **API Endpoints:** Provides a set of FastAPI endpoints for seamless interaction.

## Project Structure

```bash
src/
│
├── agent.py              # Agent logic (core decision-making node)
├── flow.py               # Constructs and compiles the LangGraph workflow
├── generate.py           # Final generation node logic
├── grade.py              # Grader logic to choose between rewrite/generate
├── graphstate.py         # Defines the LangGraph state class
├── retriever.py          # Retrieves external content using a tool node
├── rewrite.py            # Rewrites the retrieved content for clarity or improvement
│
├── llmUtils/             # Utilities for LLM operations
│   ├── __init__.py
│   └── llm.py            # Helper methods for LLM calls or prompts
│
app.py                    # Entry script to initialize and run the LangGraph
requirements.txt          # Python package dependencies
.env                      # Environment variables (e.g., GROQ_API_KEY)
.gitignore                # Git ignored files (should include __pycache__, .env, etc.)

```

## LangGraph Flow

The Agentic RAG system follows a specific flow orchestrated by LangGraph. Below is a diagram illustrating the interaction between different components, showcasing the decision-making process of the agent:

![LangGraph Flow Diagram]![image](https://github.com/user-attachments/assets/c92a5af1-378a-44d4-8ec6-b1820a87b74c)


**_Explanation of the Flow:_**
* **Start:** The process initiates with a user query.
* **Agent:** The central orchestrator decides the next action based on the query.
* **Retriever_tool:** If the agent determines that information retrieval is necessary, this component fetches relevant documents from the knowledge base.
* **Rewrite:** The agent might decide to rewrite the user's query for better retrieval results before or after an initial retrieval attempt.
* **Generate:** Once sufficient context is available, this component synthesizes the final answer.
* **End:** The process concludes, delivering the generated response to the user.

## Setup Instructions

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/subhash-telugu/Agentic-Rag.git](https://github.com/subhash-telugu/Agentic-Rag.git)
    cd Agentic-Rag
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    Create a `.env` file in the root of your project directory and add your Groq API key:
    ```
    GROQ_API_KEY="your_groq_api_key_here"
    ```
    You can obtain a Groq API key by signing up and creating a project at [Groq Console](https://console.groq.com/).

## Usage

### Running the Application

To start the FastAPI server:



uvicorn src.app:app --reload
The application will typically be accessible at http://127.0.0.1:8000. You can interact with the API endpoints via a tool like Postman or through the automatically generated Swagger UI available at http://127.0.0.1:8000/docs.

Endpoints
/upload:
![image](https://github.com/user-attachments/assets/528c1983-a040-4198-bd63-672b96486b05)
```bash
Method: POST
Description: Allows uploading a PDF file for processing and indexing into the VectorDB.
Example (Swagger UI):
Navigate to http://127.0.0.1:8000/docs.
Find the /upload endpoint and click "Try it out".
Choose your PDF file and click "Execute".
Sample Response:
```

Endpoints
/ask:
![image](https://github.com/user-attachments/assets/ce7e3eef-1520-4869-bd43-6da65b0b02fe)
```bash
Method: POST
Description: Submits a question to the system. The agent processes the query using the RAG flow, potentially involving retrieval and generation.
Parameters: question (string)
Example (Swagger UI):
Navigate to http://127.0.0.1:8000/docs.
Find the /ask endpoint and click "Try it out".
Enter your question (e.g., "How did he greet the audience at the Parliament?").
Click "Execute".
Sample Response:
```
