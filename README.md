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

The core logic of the application resides within the `src` directory. Here's a breakdown of the key files and folders:

src/
├── llmUtils/
│   ├── init.py
│   └── llm.py            # Contains LLM initialization and related utilities (e.g., Groq client)
├── init.py
├── agent.py              # Defines the main agent logic
├── flow.py               # Defines the LangGraph flow and its nodes/edges
├── generate.py           # Handles response generation based on retrieved context
├── grade.py              # (Optional) For grading or evaluating retrieved documents/responses
├── graphstate.py         # Defines the state object passed through the LangGraph
├── retriever.py          # Handles document retrieval logic (e.g., from VectorDB)
├── rewrite.py            # Handles query rewriting logic based on agent's decision
├── .gitignore            # Specifies intentionally untracked files to ignore
├── app.py                # Main FastAPI application entry point
└── requirements.txt      # Lists project dependencies


## LangGraph Flow

The Agentic RAG system follows a specific flow orchestrated by LangGraph. Below is a diagram illustrating the interaction between different components, showcasing the decision-making process of the agent:

![LangGraph Flow Diagram](image_20d1aa.png)

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

```bash
uvicorn src.app:app --reload
The application will typically be accessible at http://127.0.0.1:8000. You can interact with the API endpoints via a tool like Postman or through the automatically generated Swagger UI available at http://127.0.0.1:8000/docs.

Endpoints
/upload:

Method: POST
Description: Allows uploading a PDF file for processing and indexing into the VectorDB.
Example (Swagger UI):
Navigate to http://127.0.0.1:8000/docs.
Find the /upload endpoint and click "Try it out".
Choose your PDF file and click "Execute".
Sample Response:
/ask:

Method: POST
Description: Submits a question to the system. The agent processes the query using the RAG flow, potentially involving retrieval and generation.
Parameters: question (string)
Example (Swagger UI):
Navigate to http://127.0.0.1:8000/docs.
Find the /ask endpoint and click "Try it out".
Enter your question (e.g., "How did he greet the audience at the Parliament?").
Click "Execute".
Sample Response:
