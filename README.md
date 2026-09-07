# LLM Learning

This repository contains my hands-on learning and practice with Large Language Models (LLMs), APIs, local models, embeddings, and Retrieval-Augmented Generation (RAG).

The goal is to understand LLM concepts step by step by implementing them in Python.

## Topics Covered

* Working with local LLMs
* Gemini API
* Prompting
* Text chunking
* Text embeddings
* Vector representations
* Cosine similarity
* Semantic retrieval
* Retrieval-Augmented Generation (RAG)
* Context-based generation

## Repository Structure

```text
LLM-Learning/
│
├── local_model.py
├── gemini_test.py
│
└── RAG/
    ├── chunking.py
    ├── embedding.py
    ├── emb_.py
    ├── emb_with_num.py
    └── retr.py
```

## Files

### `local_model.py`

Practice with running and interacting with local language models using Ollama.

### `gemini_test.py`

Basic practice with the Gemini API using Google's Python SDK.

## RAG

The `RAG` folder contains my implementation and practice of the core concepts behind Retrieval-Augmented Generation.

### `chunking.py`

Practice with splitting text into multiple chunks and joining chunks back together.

### `embedding.py`

Basic practice with generating text embeddings using the Gemini API.

### `emb_.py`

Practice with generating embeddings for multiple documents and a question.

### `emb_with_num.py`

Practice with understanding the numerical/vector representation produced from text embeddings.

### `retr.py`

A basic end-to-end RAG implementation.

It:

1. Creates embeddings for documents.
2. Creates an embedding for the user question.
3. Calculates cosine similarity.
4. Finds the most relevant document.
5. Uses the retrieved document as context.
6. Generates an answer using Gemini based on the retrieved context.

## RAG Flow

```text
Documents
    ↓
Chunking
    ↓
Embeddings
    ↓
Vector Representations
    ↓
User Question
    ↓
Question Embedding
    ↓
Cosine Similarity
    ↓
Relevant Document Retrieval
    ↓
Retrieved Context
    ↓
Gemini
    ↓
Final Answer
```

## Example

Documents:

```text
Refund requests are allowed within 7 days
Python classes happen Monday to Friday
Students get 4 interview opportunities
Course access is available for 6 months
```

Question:

```text
How many interview opportunities can I get?
```

Retrieved context:

```text
Students get 4 interview opportunities
```

The retrieved context is then provided to the LLM to generate the final answer.

## Technologies

* Python
* Ollama
* Google Gemini API
* NumPy
* Gemini Embeddings
* Cosine Similarity
* Retrieval-Augmented Generation (RAG)

## Purpose

This repository is part of my LLM learning journey.

I am building the concepts step by step, starting from basic LLM/API usage and progressing toward embeddings, retrieval, RAG, and more advanced LLM applications.
