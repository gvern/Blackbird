from core.local_model import OllamaLocalModel

class BlackbirdAgent:
    def __init__(self, model="llama2"):
        self.llm = OllamaLocalModel(model=model)
        self.system_prompt = {
            "role": "system",
            "content": (
                "Tu es Blackbird, un agent autonome intelligent. Tu planifies les tâches "
                "avant de répondre et tu expliques ton raisonnement si besoin."
            )
        }

    def run(self, user_input):
        messages = [
            self.system_prompt,
            {"role": "user", "content": f"Planifie et réponds à cette requête : {user_input}"}
        ]
        return self.llm.generate(messages)
