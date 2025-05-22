def plan_action(instruction):
    # Exemples simples, améliorable avec un modèle de planification
    if "heure" in instruction.lower():
        return "tool:get_time"
    elif "capital" in instruction.lower():
        return "model:ask"
    else:
        return "model:ask"
