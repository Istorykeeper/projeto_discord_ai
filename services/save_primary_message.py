import json
import os

# função para salvar mensagem primaria do bot
def save_primary_message(mensagem, arquivo):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump({"primary_message": mensagem}, f)



# função para carregar a mensagem primaria do bot
def load_primary_message(arquivo):
    if not os.path.exists(arquivo):
        return None

    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f).get("primary_message")

    except (json.JSONDecodeError, AttributeError):
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump({}, f)
        return None