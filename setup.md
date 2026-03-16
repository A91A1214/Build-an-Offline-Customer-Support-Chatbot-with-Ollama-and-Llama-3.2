# Project Setup Guide

Follow these steps to configure your local environment and run the offline customer support chatbot.

## 1. Install Ollama

Ollama is a lightweight framework for running large language models locally.

1. Visiti the [Ollama website](https://ollama.com/) and download the installer for your operating system (macOS, Windows, or Linux).
2. Follow the installation instructions provided on the site.
3. Verify the installation by opening your terminal or command prompt and running:
   ```bash
   ollama --version
   ```

## 2. Pull the Llama 3.2 Model

Once Ollama is installed, you need to download the specific model used for this project: Meta's Llama 3.2 (3B).

Open your terminal and run:
```bash
ollama pull llama3.2:3b
```
*Note: This will download approximately 2GB of data. The time required depends on your internet connection.*

*(Optional Step)*: To confirm the model works, you can chat with it interactively via the terminal:
```bash
ollama run llama3.2:3b
```
*Type `/bye` to exit the chat.*

## 3. Set Up the Python Environment

The Python script (`chatbot.py`) interacts with Ollama's local REST API. It is recommended to use a virtual environment.

1. **Navigate** to your project directory.
2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   ```
3. **Activate the virtual environment**:
   - On macOS/Linux: `source venv/bin/activate`
   - On Windows: `venv\Scripts\activate`
4. **Install necessary dependencies**:
   ```bash
   pip install requests datasets
   ```

## 4. Run the Chatbot

Make sure the Ollama application is running in the background. Then, execute the python script to run the 20 test queries:

```bash
python chatbot.py
```

The script will query the local LLM sequentially and generate a log file at `eval/results.md`. You can then review the model's outputs and adjust the scores based on the evaluation rubric.
