import json
import os

# função para salvar o chat_id
def save_chat_id(chat_id, arquivo):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump({"chat_id": chat_id}, f)



# função para carregar o chat_id
def load_chat_id(arquivo):
    if not os.path.exists(arquivo):
        return None

    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f).get("chat_id")

    except (json.JSONDecodeError, AttributeError):
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump({}, f)
        return None