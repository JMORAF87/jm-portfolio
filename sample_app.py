import os
import requests
import json
import time

# Configuration
AI_API_BASE = os.getenv("AI_API_BASE", "http://localhost:8000/v1" )
AI_API_KEY = os.getenv("AI_API_KEY", "YOUR_API_KEY_HERE")

# API Endpoints
COMPLETIONS_URL = f"{AI_API_BASE}/chat/completions"
MODELS_URL = f"{AI_API_BASE}/models"

def _handle_api_response(response: requests.Response, endpoint: str):
    """Handles common HTTP error codes and returns JSON data."""
    if response.status_code == 200:
        return response.json()
    
    # Custom error handling based on OpenAPI spec
    if response.status_code == 401:
        print(f"Error 401 Unauthorized: Invalid API Key for {endpoint}")
    elif response.status_code == 400:
        print(f"Error 400 Bad Request: Check your input parameters for {endpoint}")
    elif response.status_code == 429:
        print(f"Error 429 Rate Limit Exceeded: Please try again later for {endpoint}")
    elif response.status_code == 500:
        print(f"Error 500 Internal Server Error: Something went wrong on the server for {endpoint}")
    else:
        print(f"Unexpected Error {response.status_code}: {response.text} for {endpoint}")
    
    return None

def get_models_list():
    """Fetches the list of available AI models."""
    headers = {
        "Authorization": f"Bearer {AI_API_KEY}"
    }
    print(f"\nFetching models from: {MODELS_URL}")
    try:
        response = requests.get(MODELS_URL, headers=headers, timeout=5)
        return _handle_api_response(response, "Models Endpoint")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during models request: {e}")
        return None

def get_chat_completion(prompt: str, model: str = "gpt-3.5-turbo", temperature: float = 0.7, max_tokens: int = 50):
    """Sends a chat completion request to the AI API."""
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {AI_API_KEY}"
    }
    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": temperature,
        "max_tokens": max_tokens
    }

    retries = 3
    for i in range(retries):
        start_time = time.time()
        try:
            response = requests.post(COMPLETIONS_URL, headers=headers, json=payload, timeout=10)
            end_time = time.time()
            latency = (end_time - start_time) * 1000 # in milliseconds
            print(f"API Call Latency: {latency:.2f} ms")
            
            result = _handle_api_response(response, "Completions Endpoint")
            if result:
                return result
            
        except requests.exceptions.Timeout:
            print(f"Attempt {i+1}/{retries}: Request timed out.")
        except requests.exceptions.RequestException as e:
            print(f"Attempt {i+1}/{retries}: An error occurred: {e}")
        time.sleep(2) # Wait before retrying
    return None

if __name__ == "__main__":
    # 1. Test Models Endpoint
    models_list = get_models_list()
    if models_list and models_list.get("data"):
        print("\nSuccessfully retrieved Models List:")
        print(f"Found {len(models_list['data'])} models. Example: {models_list['data'][0]['id']}")
    
    # 2. Test Chat Completions Endpoint
    user_prompt = "Explain the concept of large language models in simple terms."
    print(f"\nSending request for prompt: '{user_prompt}'")
    
    completion = get_chat_completion(user_prompt)

    if completion:
        print("\nAI Response:")
        # print(json.dumps(completion, indent=2)) # Commented out for cleaner output
        if completion.get("choices") and completion["choices"][0].get("message"):
            print("\nContent:")
            print(completion["choices"][0]["message"]["content"])
    else:
        print("Failed to get AI completion.")
