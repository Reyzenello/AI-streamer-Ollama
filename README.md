# AI-streamer-Ollama

This code simulates a chat between a "famous streamer" (powered by an Ollama language model) and viewers, with questions and responses generated dynamically.  

**1. Importing Libraries:** Standard libraries for randomization, time delays, HTTP requests, and JSON handling.

**2. `generate_response` Function:**

```python
def generate_response(prompt, model, role):
    # ...
```

* Takes the `prompt`, `model` name, and the `role` (either "question" or "response") as input.
* Constructs the URL for the Ollama API endpoint.  It assumes the API is running locally on port 11434.
* Sets the request headers for JSON content.
* Constructs the request data:
    * `model`: The name of the Ollama model to use.
    * `prompt`: The prompt for the model, including context about being a streamer and the role.
    * `max_tokens`: Limits the length of the generated response.
* `response = requests.post(...)`: Makes a POST request to the Ollama API, using streaming to receive the response incrementally.
* **Improved Error Handling:** Includes `try-except` blocks to handle potential errors during the request and JSON decoding:
    * `response.raise_for_status()`: Raises an exception for HTTP errors (4xx or 5xx).
* Iterates through the response lines:
    * Decodes each line from UTF-8.
    * Parses the JSON response.
    * Appends the `response` part to `complete_response`.
    * Checks for the `done` flag to see if the generation is complete.
* Returns the complete response, handling potential errors.

**3. `simulate_chat` Function:**

```python
def simulate_chat(model):
    # ...
```

* `initial_prompts`: A list of initial questions to start the conversation.
* Enters a `while True` loop to simulate an ongoing chat.
* `question_number`: Keeps track of the question number.
* For the first question, chooses a random prompt from `initial_prompts`.
* For subsequent questions, uses `generate_response` to generate a new viewer question.  This makes the chat dynamic!
* Calls `generate_response` again to get the AI streamer's response to the question.
* Prints the question and the AI's response.
* Increments the `question_number`.
* `time.sleep(random.uniform(1, 5))`: Pauses for a random interval between 1 and 5 seconds to simulate real-time chat.

**4. Main Execution Block:**

```python
if __name__ == "__main__":
    model = "llama2"  # Replace with your Ollama model name
    simulate_chat(model)
```

* Sets the `model` name. **Adjust this to match the identifier of your Ollama model.**
* Calls `simulate_chat` to start the simulation.
