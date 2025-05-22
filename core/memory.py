import json
from pathlib import Path

class ChatMemory:
    def __init__(self, max_turns: int = 4, save_path: str = None):
        self.messages = []
        self.max_turns = max_turns
        self.save_path = Path(save_path) if save_path else None

        if self.save_path and self.save_path.exists():
            self._load()

    def add_user_message(self, msg: str):
        self.messages.append(("user", msg))
        self._save()

    def add_assistant_message(self, msg: str):
        self.messages.append(("assistant", msg))
        self._save()

    def get_context(self) -> str:
        """Retourne les N derniers échanges formatés pour le prompt."""
        relevant = self.messages[-self.max_turns * 2:]
        context = ""
        for role, msg in relevant:
            prefix = "User" if role == "user" else "Assistant"
            context += f"{prefix}: {msg.strip()}\n"
        return context.strip()

    def _save(self):
        if not self.save_path:
            return
        try:
            data = [{"role": role, "message": msg} for role, msg in self.messages]
            with open(self.save_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"[Mémoire] ❌ Erreur sauvegarde : {e}")

    def _load(self):
        try:
            with open(self.save_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.messages = [(entry["role"], entry["message"]) for entry in data]
        except Exception as e:
            print(f"[Mémoire] ❌ Erreur chargement : {e}")
