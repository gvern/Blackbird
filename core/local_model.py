import requests

class OllamaLocalModel:
    def __init__(self, model="llama2"):
        self.url = "http://localhost:11434/api/chat"
        self.model = model

    def generate(self, messages, temperature=0.7, max_tokens=200):
        payload = {
            "model": self.model,
            "messages": messages,
            "stream": False,
            "options": {
                "temperature": temperature,
                "num_predict": max_tokens,
            }
        }
        try:
            response = requests.post(self.url, json=payload)
            response.raise_for_status()
            return response.json()["message"]["content"]
        except requests.RequestException as e:
            return f"❌ Erreur: {str(e)}"
