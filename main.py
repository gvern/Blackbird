from core.local_model import OllamaLocalModel
from core.agent_manager import BlackbirdAgent
from rich.console import Console
from rich.markdown import Markdown

console = Console()
agent = BlackbirdAgent(model="llama2")

console.print(Markdown("# 🦅 Bienvenue dans Blackbird (Ollama)"))

while True:
    try:
        user_input = console.input("[bold blue]Vous[/bold blue]: ")
        if user_input.lower() in ("exit", "quit"):
            console.print("[italic]À bientôt ![/italic]")
            break

        response = agent.run(user_input)
        console.print(f"[bold green]🧠 Blackbird[/bold green]: {response}")

    except KeyboardInterrupt:
        console.print("\n[italic red]Interruption par l'utilisateur.[/italic red]")
        break
