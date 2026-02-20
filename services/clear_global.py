import os

def clear(arquivo):
    if os.path.exists(arquivo):
        try:
            os.remove(arquivo)
        except OSError as e:
            return e
    else:
        return f'o arquivo {arquivo} não encontrado.'