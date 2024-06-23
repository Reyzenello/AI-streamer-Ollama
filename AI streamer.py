import random
import time
import requests
import json

# Function to generate a response using Ollama API
def generate_response(prompt, model, role):
    url = f"http://localhost:11434/api/generate"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "prompt": f"Imagine you are a famous streamer responding to a viewer's question while live streaming. Here is the {role}: {prompt}",
        "max_tokens": 100
    }
    response = requests.post(url, headers=headers, json=data, stream=True)
    
    try:
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        
        complete_response = ""
        for line in response.iter_lines():
            if line:
                decoded_line = line.decode('utf-8')
                response_json = json.loads(decoded_line)  # Use the json module from the standard library
                complete_response += response_json["response"]
                if response_json.get("done"):
                    break
        
        return complete_response.strip()
    
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except requests.exceptions.RequestException as err:
        return f"Other error occurred: {err}"
    except ValueError as json_err:
        return f"JSON decode error: {json_err}"
    return "Error generating comment"

# Function to simulate chat with random comments
def simulate_chat(model):
    initial_prompts = [
        "What do you think of this game?",
        "Tell us about your favorite streamer!",
        "What is your favorite streamer moment?",
        "Do you have any advice for new streamers?",
        "Tell us a funny story about your streaming experience."
    ]

    question_number = 1
    while True:
        if question_number == 1:
            prompt = random.choice(initial_prompts)
        else:
            prompt = generate_response("Generate a new viewer question!", model, "question")

        comment = generate_response(prompt, model, "response")
        
        print(f"question {question_number} commenter: {prompt}\nAI streamer: {comment}\n")
        
        question_number += 1
        
        # Wait a random interval before generating the next comment
        time.sleep(random.uniform(1, 5))

if __name__ == "__main__":
    # Define the model to use
    model = "llama3"  # Adjust if needed to match your Ollama model identifier
    
    # Start the chat simulation
    simulate_chat(model)
