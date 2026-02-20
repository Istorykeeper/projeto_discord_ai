import json
import os

def save_message(author, text, arquivo):
    history = []

    if os.path.exists(arquivo):
        try:
            with open(arquivo, "r", encoding="utf-8") as f:
                history = json.load(f)
                if not isinstance(history, list):
                    history = []

        except json.JSONDecodeError:
            history = []

    history.append({
        "autor": author,
        "texto": text
    })

    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

