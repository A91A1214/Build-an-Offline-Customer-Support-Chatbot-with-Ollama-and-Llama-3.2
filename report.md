# Evaluation Report: Llama 3.2 3B for Offline Customer Support

## Introduction
The objective of this project was to establish a fully offline, privacy-centric customer support chatbot utilizing Meta's **Llama 3.2 3B** LLM served via **Ollama**. Sending sensitive customer records to cloud providers presents significant compliance risks (GDPR, CCPA). By routing queries to a local, on-premise model, data privacy is inherently guaranteed.

This report evaluates the model's performance on 20 realistic consumer inquiries. Specifically, it contrasts **Zero-Shot** prompting (providing only system instructions) against **One-Shot** prompting (providing one high-quality example) to determine the most effective approach for standardizing AI support agents.

## Methodology

**Query Sourcing and Adaptation:**
We sourced technical multi-turn dialogues from the Ubuntu Dialogue Corpus. These technical queries were manually adapted into 20 common e-commerce questions, representing themes like tracking, returns, store policies, and account management.

**Prompting Strategy:**
Two prompting templates were tested:
1. `zero_shot_template.txt`: Instructs the agent on its role ("Chic Boutique support agent") and constraints ("Do not make up information").
2. `one_shot_template.txt`: Uses the identical system instruction but includes one single input-output example outlining the company's return policy.

**Evaluation Rubric:**
Responses were logged to `eval/results.md` and manually scored on a 1-5 scale across three dimensions:
- **Relevance:** Does it directly answer the user's specific query?
- **Coherence:** Is the grammatical structure sound and logical?
- **Helpfulness:** Does it provide an actionable resolution or next step?

## Results & Analysis

### Quantitative Summary

| Metric | Zero-Shot Average | One-Shot Average | Improvement |
| :--- | :--- | :--- | :--- |
| **Relevance** | 3.50 | 5.00 | +42.8% |
| **Coherence** | 4.80 | 5.00 | +4.1% |
| **Helpfulness** | 2.85 | 4.90 | +71.9% |

### Qualitative Analysis

The quantitative data clearly illustrates that **One-Shot prompting significantly outperformed Zero-Shot prompting**, particularly in the "Helpfulness" and "Relevance" categories.

**1. Maintaining the Persona and Tone:**
Zero-shot responses often skewed towards being overly terse or slightly defensive. For example, in response to *"I received the wrong size for my shirt"*, the zero-shot model replied: *"That shouldn't happen. If you got the wrong size, please send it back"* (Helpfulness Score: 2). The one-shot model, guided by the tone established in the prompt's return policy example, outputted a highly professional response: *"I am so sorry about that! Please initiate a return through your order history..."* (Helpfulness Score: 5).

**2. Providing Actionable Next Steps:**
Zero-shot generations frequently summarized *what* to do without explaining *how*, rendering them unhelpful for a customer. When asked *"I forgot my password,"* the zero-shot model hallucinated a useless response: *"If you forgot your password, you should try to remember it or reset it"* (Helpfulness Score 1). The one-shot model reliably mapped the request to a standard e-commerce workflow: *"Just click the 'Forgot Password' link on the login page..."* (Helpfulness Score 5).

**3. Mitigating Hallucinations on Policies:**
While the zero-shot model was explicitly instructed not to hallucinate policies, it still occasionally produced non-committal or generic answers (e.g., claiming "We have local stores in major cities" when asked about store locations, relevance score: 2). The one-shot example grounded the model contextually, encouraging it to provide structured, standard business responses that mimic typical FAQs (e.g., explicitly stating it is an "online-only boutique").

## Conclusion & Limitations

**Suitability:** Llama 3.2 3B is highly suitable for this task when paired with **One-Shot (or Few-Shot) prompting**. The model operates quickly on standard hardware and successfully handles routing, tone-matching, and basic e-commerce inquiry resolution without compromising security.

**Limitations:**
1. **Lack of Real-Time Context:** The model operates entirely statelessly. It has no API access to an actual database to check if a specific user's package is delivered or what their order number is.
2. **Context Window Limitations:** By passing all history directly in prompt strings, large multi-turn conversations could theoretically overflow the context limit and degrade performance.
3. **Hardware Latency:** While relatively small (3B parameters), running inference on older laptops without unified memory or a dedicated GPU can still produce notable token-generation latency compared to high-end cloud providers.

**Next Steps to Improve:**
The logical next stage in evolving this chatbot is the integration of **Retrieval-Augmented Generation (RAG)** or **Tool Calling / Function Calling**. Instead of static text responses, the model could securely call an internal `/api/check_order_status` function using the local network, inject the actual customer database state into the local context window, and generate a dynamically accurate response without data ever leaving the private intranet.
