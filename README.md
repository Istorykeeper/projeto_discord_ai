# projeto_discord_ai
Um bot de Discord avançado para integração com CharacterAI. Possui sistema de persistência de sessões, gerenciamento de permissões por usuário, salvamento automático de histórico de conversas e suporte a múltiplas instâncias de chat.


# 🤖 Discord CharacterAI Bot

[cite_start]Este projeto realiza a integração entre o Discord e a plataforma CharacterAI[cite: 1], permitindo que usuários interajam com personagens de inteligência artificial em servidores. [cite_start]O sistema foca em persistência de dados e gerenciamento modular de serviços[cite: 11, 16].

## ✨ Funcionalidades

* [cite_start]**💬 Chat e Comandos**: Implementação de comandos e eventos específicos para o bot do Discord[cite: 1, 8].
* [cite_start]**🔐 Controle de Permissões**: Serviço dedicado para permitir ou restringir o acesso de usuários ao bot (`permit_user.py`)[cite: 12].
* [cite_start]**💾 Persistência de Sessão**: Salvamento e carregamento automático de sessões para manter o contexto das conversas (`save_session.py`)[cite: 14, 15].
* [cite_start]**📜 Histórico de Mensagens**: Armazenamento de mensagens primárias e logs das interações (`save_messages.py`, `save_primary_message.py`)[cite: 13, 14].
* [cite_start]**🔑 Gestão de Credenciais**: Armazenamento seguro de tokens e credenciais necessárias para a API (`save_credentials.py`)[cite: 12, 13].
* [cite_start]**⚙️ Monitoramento de Ambiente**: Possui um sistema de "watcher" para variáveis de ambiente e limpeza de estados globais (`env_watcher.py`, `clear_global.py`)[cite: 11, 12].

## 📂 Estrutura do Projeto

* [cite_start]**`bot/`**: Contém a lógica de comandos (`commands.py`), eventos (`events.py`) e a instância principal do bot[cite: 1, 8, 10].
* [cite_start]**`services/`**: Scripts de backend para gerenciamento de dados, sessões e usuários[cite: 11, 12, 13].
* [cite_start]**`save/`**: Diretórios destinados ao armazenamento local de informações globais e de usuários[cite: 15, 16].
* [cite_start]**`config.py` e `main.py`**: Configurações centrais e ponto de entrada da aplicação[cite: 10].

## 🚀 Como Instalar

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/projeto_discord_CharacterAi.git](https://github.com/seu-usuario/projeto_discord_CharacterAi.git)
    cd projeto_discord_CharacterAi
    ```

2.  **Instale as dependências:**
    * [cite_start]O projeto utiliza as bibliotecas listadas em `requirements.txt.txt`[cite: 11].
    ```bash
    pip install -r requirements.txt.txt
    ```

3.  **Configuração:**
    * [cite_start]Configure o arquivo `.env` com seu `DISCORD_TOKEN` e chaves da `CharacterAI`[cite: 1].

4.  **Inicie o bot:**
    ```bash
    python main.py
    ```

---
**Desenvolvido com foco em integração e persistência.**
