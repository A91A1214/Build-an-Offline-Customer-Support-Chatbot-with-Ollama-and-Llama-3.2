# Build an Offline Customer Support Chatbot with Ollama & Llama 3.2

## Overview

In the modern e-commerce landscape, privacy and security are paramount when handling sensitive customer data. Cloud-based LLMs pose a risk of data breaches under strict regulations (e.g., GDPR, CCPA). This project demonstrates a powerful alternative: an entirely offline, local customer support chatbot.

By leveraging **Ollama** and Meta's open-source **Llama 3.2 (3B)** model, this chatbot allows companies to provide high-quality AI assistance without ever transmitting customer data across the internet.

### Project Goals

1. **Deploy a local LLM:** Use Ollama to serve Llama 3.2 on consumer hardware.
2. **Explore Prompt Engineering:** Compare Zero-Shot and One-Shot prompting techniques.
3. **Handle Realistic Queries:** Adapt the Ubuntu Dialogue Corpus to a fictional e-commerce scenario.
4. **Evaluate Performance:** Systematically assess the chatbot's Relevance, Coherence, and Helpfulness.

## Project Structure

```text
your-project-name/
├── prompts/
│   ├── zero_shot_template.txt
│   └── one_shot_template.txt
├── eval/
│   └── results.md
├── chatbot.py
├── setup.md
├── report.md
└── README.md
```

## Methodology

1. **Query Adaptation**: 20 technical support queries from the Ubuntu Dialogue Corpus were manually rewritten to represent common e-commerce questions (e.g., shipping, returns, discounts).
2. **Prompt Templates**:
   - `zero_shot_template.txt`: Instructions to act as a "Chic Boutique" agent, without examples.
   - `one_shot_template.txt`: Includes a single, high-quality demonstration of the desired tone and format.
3. **Inference**: A Python script (`chatbot.py`) sends HTTP POST requests to the local Ollama API (`http://localhost:11434/api/generate`), capturing the AI's response for both prompting methods.
4. **Evaluation**: Responses are logged and manually scored on a 1-5 scale for Relevance, Coherence, and Helpfulness.

## Setup Instructions

Please see [`setup.md`](setup.md) for detailed instructions on installing Ollama, downloading the Llama 3.2 model, and configuring the Python environment.

## Running the Chatbot

After installing the requirements, run the main script to process the queries and generate the evaluation log:

```bash
python chatbot.py
```

Results are appended to `eval/results.md`.

## Key Findings

The comprehensive evaluation (detailed in `report.md`) reveals that **One-Shot prompting significantly outperforms Zero-Shot prompting**, particularly in ensuring the model maintains the professional, concise tone expected of an e-commerce agent. The Llama 3.2 (3B) model is highly capable of running locally and resolving standard support inquiries while preserving 100% data privacy.
