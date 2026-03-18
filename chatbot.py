import requests
import json
import os

OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:3b"

# 20 realistically adapted e-commerce queries
QUERIES = [
    "How do I track my order?",
    "My discount code isn't working.",
    "Can I return an item without the original packaging?",
    "Do you ship internationally?",
    "I received the wrong size for my shirt.",
    "Where is the nearest physical store?",
    "How long does standard shipping take?",
    "My package says delivered but I haven't received it.",
    "Can I change my shipping address after placing the order?",
    "How do I apply a gift card to my purchase?",
    "What payment methods do you accept?",
    "I want to cancel my recent order.",
    "The item I want is out of stock. When will it be back?",
    "Do you offer student discounts?",
    "My item arrived damaged.",
    "How do I create an account?",
    "I forgot my password.",
    "Can I exchange an item for a different color?",
    "Are there any upcoming sales or promotions?",
    "How can I contact customer support directly?"
]

def load_template(filepath):
    """Loads a prompt template from a given file."""
    try:
        with open(filepath, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"Error loading template {filepath}: {e}")
        return ""

def query_ollama(prompt):
    """Sends a synchronous request to the Ollama local inference server."""
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }
    
    try:
        response = requests.post(OLLAMA_ENDPOINT, json=payload, timeout=180)
        response.raise_for_status()
        return json.loads(response.text).get("response", "").strip()
    except requests.exceptions.RequestException as e:
        print(f"Error querying Ollama API: {e}")
        return "Error: Could not get a response from the model. Please ensure Ollama is running locally."

def main():
    print(f"Loaded {len(QUERIES)} queries. Preparing templates...")
    
    zero_shot_path = os.path.join("prompts", "zero_shot_template.txt")
    one_shot_path = os.path.join("prompts", "one_shot_template.txt")
    
    zero_shot_template = load_template(zero_shot_path)
    one_shot_template = load_template(one_shot_path)
    
    if not zero_shot_template or not one_shot_template:
        print("Failed to load prompt templates. Exiting.")
        return
        
    results_file = os.path.join("eval", "results.md")
    
    # Initialize the Markdown log file
    with open(results_file, 'w') as f:
        f.write("# Interaction Log & Evaluation\n\n")
        f.write("Scoring Rubric:\n\n")
        f.write("- **Relevance (1-5):** How well does the response address the customer's query? (1 = Irrelevant, 5 = Perfectly relevant)\n")
        f.write("- **Coherence (1-5):** Is the response grammatically correct and easy to understand? (1 = Incoherent, 5 = Flawless)\n")
        f.write("- **Helpfulness (1-5):** Does the response provide a useful, actionable answer? (1 = Not helpful, 5 = Very helpful)\n\n")
        
        f.write("| Query # | Customer Query | Prompting Method | Response | Relevance (1-5) | Coherence (1-5) | Helpfulness (1-5) |\n")
        f.write("| :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n")
        
    for i, query in enumerate(QUERIES, start=1):
        print(f"Processing Query {i}: {query}")
        
        # Zero-Shot Processing
        prompt_zero = zero_shot_template.replace("{query}", query)
        response_zero = query_ollama(prompt_zero)
        
        # One-Shot Processing
        prompt_one = one_shot_template.replace("{query}", query)
        response_one = query_ollama(prompt_one)
        
        # We append to the file iteratively to prevent data loss if the script crashes
        with open(results_file, 'a') as f:
            # Format responses to be on one single line in the markdown table by replacing newlines
            clean_zero = response_zero.replace('\n', ' ').replace('|', '\\|')
            clean_one = response_one.replace('\n', ' ').replace('|', '\\|')
            
            f.write(f"| {i} | \"{query}\" | Zero-Shot | {clean_zero} |  |  |  |\n")
            f.write(f"| {i} | \"{query}\" | One-Shot | {clean_one} |  |  |  |\n")
            
    print(f"Completed processing 20 queries. Results written to {results_file}")

if __name__ == "__main__":
    main()
