from tools import TOOLS
from core.local_model import query_model

def execute_plan(plan, instruction):
    if plan.startswith("tool:"):
        tool_name = plan.split(":")[1]
        tool = TOOLS.get(tool_name)
        return tool() if tool else "❌ Outil inconnu."
    elif plan.startswith("model:"):
        return query_model(instruction)
    else:
        return "❌ Plan invalide."
