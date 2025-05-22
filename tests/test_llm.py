import requests

def query_ollama(prompt, model="llama2", max_tokens=50):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {
            "num_predict": max_tokens
        }
    }
    response = requests.post(url, json=payload)
    response.raise_for_status()
    return response.json()["response"]

# Exemple d’usage
if __name__ == "__main__":
    print("⏳ Début du chargement...")
    prompt = "Question: Quelle est la capitale de la France ? Réponse:"
    output = query_ollama(prompt)
    print("🧠 Réponse:", output)
