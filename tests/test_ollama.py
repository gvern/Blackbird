import requests

prompt = "Quelle est la capitale de la France ?"

response = requests.post("http://localhost:11434/api/generate", json={
    "model": "tinyllama",
    "prompt": prompt,
    "stream": False
})

print("🧠 Réponse :", response.json()["response"])
