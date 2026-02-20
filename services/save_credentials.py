import json
import os

def save_credentials(id_user, token, character_id, arquivo):
    credentials = []

    credentials.append({
        "id_user": id_user,
        "token": token,
        "character": character_id,
        "isPrivate": True
    })


    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(credentials, f, ensure_ascii=False, indent=3)




def load_token_user(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            data_list = json.load(f)
            for item in data_list:
                token = item.get("token")
                return token
    return None



def load_character_user(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            data_list = json.load(f)
            for item in data_list:
                character = item.get("character")
                return character
    return None


def load_status_user(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            data_list = json.load(f)
            for item in data_list:
                status = item.get("isPrivate")
                return status
    return None