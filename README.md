# 🦅 Blackbird

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> _Blackbird_ est une plateforme d'agents conversationnels locaux, propulsée par **Ollama** et conçue pour fonctionner en local ou en mode serveur HTTP.

---

## 🚀 Table des matières

- [Présentation](#-présentation)
- [Fonctionnalités](#fonctionnalités)
- [Structure du projet](#structure-du-projet)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
  - [Interface CLI](#interface-cli)
  - [Test unitaire](#test-unitaire)
- [Contribuer](#contribuer)
- [Licence](#licence)

---

## Présentation

Blackbird est une plateforme modulable d’agents IA locaux, idéale pour :

- Prototyper des assistants spécialisés (juridique, technique, etc.)
- Expérimenter des LLM locaux via **Ollama** (supporte `llama2`, `mistral-7b`, etc.)
- Tester, historiser et orchestrer plusieurs agents

L’architecture se veut simple, extensible et 100% open source.

---

## Fonctionnalités

- 🔌 **Agents plug-and-play** via des configurations YAML
- 🧠 **Chargement local de modèles** (GGUF, `ollama run`)
- 💾 **Memory** : historisation des conversations
- 🛠️ **Agent Manager** : création, chargement et exécution d’agents
- 🎨 **Frontend CLI** enrichi par **Rich** ou optionnellement un UI Streamlit
- 🧪 **Tests** prêts à l’emploi pour valider l’intégration LLM

---

## Structure du projet

```bash
Blackbird/
├── main.py                   # Entrypoint CLI
├── requirements.txt          # Dépendances Python
├── .gitignore
├── README.md
├── core/                     # Modules centraux
│   ├── local_model.py        # Wrapper OllamaLocalModel
│   ├── agent_manager.py      # Chargement / exécution d’agents
│   └── memory.py             # Historique des échanges
├── tests/                    # Scénarios de tests unitaires
│   └── test_llm.py
└── models/                   # (Gitignore) Modèles GGUF locaux
```

---

## Installation

1. **Pré-requis** :
   - Python 3.8+
   - [Ollama CLI](https://ollama.com/docs) (installer et init)  
     ```bash
     brew install ollama
     ollama pull llama2
     ```

2. **Cloner le projet**  
   ```bash
   git clone https://github.com/votre-org/Blackbird.git
   cd Blackbird
   ```

3. **Créer et activer un venv**  
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. **Installer les dépendances**  
   ```bash
   pip install -r requirements.txt
   ```

---

## Configuration

- `.gitignore` exclut `models/` et `data/` pour éviter les fichiers volumineux.
- Un exemple de config pour un agent se trouve dans `agents/<agent_name>/config.yaml`.

---

## Usage

### Interface CLI

```bash
python main.py
```

**Exemple** :
```bash
🦅 Bienvenue dans Blackbird (Ollama)
Vous: Quelle est la capitale de la France ?
🧠 Blackbird: La capitale de la France est Paris.
```  
Taper `exit` ou `quit` pour terminer.

### Test unitaire

```bash
pytest tests/test_llm.py
```  
Le test valide la classe `OllamaLocalModel` via la fonction `query_ollama`.

---

## Contribuer

1. Forkez ce dépôt
2. Créez une branche : `git checkout -b feature/mon-agent`
3. Codez et testez vos changements
4. Ouvrez une Pull Request

Merci à tous les contributeurs ! 🦅

---

## Licence

Ce projet est sous licence MIT. Consultez le fichier [LICENSE](LICENSE) pour plus de détails.
