from rich.console import Console
from rich.panel import Panel

console = Console()

def display_message(role, content):
    label = "🧠 Ollama" if role == "ai" else "👤 Vous"
    console.print(Panel.fit(content, title=label, title_align="left", padding=(1, 2)))
