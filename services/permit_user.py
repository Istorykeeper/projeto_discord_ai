import os

def add_user(user_id, arquivo):
    user_id = str(user_id)

    if not os.path.exists(arquivo):
        with open(arquivo, "w", encoding="utf-8") as f:
            f.write(user_id + "\n")
        return

    with open(arquivo, "r", encoding="utf-8") as f:
        users = [linha.strip() for linha in f]

    if user_id not in users:
        with open(arquivo, "a", encoding="utf-8") as f:
            f.write(user_id + "\n")




def remove_user(user_id, arquivo):
    user_id = str(user_id)

    if not os.path.exists(arquivo):
        return False 

    with open(arquivo, "r", encoding="utf-8") as f:
        users = [linha.strip() for linha in f]

    if user_id not in users:
        return False 

    users.remove(user_id)

    with open(arquivo, "w", encoding="utf-8") as f:
        for user in users:
            f.write(user + "\n")

    return True



def load_ids(arquivo):
    if not os.path.exists(arquivo):
        return []

    with open(arquivo, "r", encoding="utf-8") as f:
        return [linha.strip() for linha in f]