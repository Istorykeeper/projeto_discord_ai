# projeto_discord_ai
Um bot de Discord avançado para integração com CharacterAI. Possui sistema de persistência de sessões, gerenciamento de permissões por usuário, salvamento automático de histórico de conversas e suporte a múltiplas instâncias de chat.

# 🤖 Discord CharacterAI Bot

[cite_start]Este projeto é uma integração entre o Discord e a plataforma CharacterAI, permitindo que os usuários conversem com personagens de inteligência artificial diretamente pelos canais do servidor. [cite: 1, 8] [cite_start]O sistema foi desenvolvido com foco em estabilidade, persistência de dados e controle de acesso. [cite: 12, 13, 15]

## ✨ Funcionalidades

* [cite_start]**💬 Chat em Tempo Real**: Comandos e eventos otimizados para interação contínua com IAs. [cite: 1, 8]
* [cite_start]**🔐 Controle de Acesso**: Sistema de permissão para gerenciar quais usuários podem interagir com o bot. [cite: 12]
* [cite_start]**💾 Persistência de Sessão**: Salva automaticamente o estado da conversa para que o contexto não seja perdido entre reinicializações. [cite: 15]
* [cite_start]**📜 Histórico de Mensagens**: Armazenamento de mensagens primárias e logs de conversas para auditoria e continuidade. [cite: 14]
* [cite_start]**🔑 Gestão de Credenciais**: Serviço dedicado para o armazenamento seguro de tokens e credenciais necessárias. [cite: 13]
* [cite_start]**⚙️ Monitoramento de Ambiente**: Possui um "watcher" para variáveis de ambiente e limpeza de estados globais. [cite: 11, 12]

## 📂 Estrutura do Projeto

* [cite_start]**`bot/`**: Contém a lógica de comandos, eventos e a instância principal do bot Discord. [cite: 1, 8, 10]
* [cite_start]**`services/`**: Scripts responsáveis pelo backend, incluindo salvamento de sessões, mensagens e validação de usuários. [cite: 12, 13, 14, 15]
* [cite_start]**`save/`**: Diretório para armazenamento local de dados de usuários e configurações globais. [cite: 16]
* [cite_start]**`config.py`**: Centraliza as definições e variáveis globais do sistema. [cite: 10]
* [cite_start]**`main.py`**: Ponto de entrada para execução da aplicação. [cite: 10, 11]

## 🚀 Como Instalar

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/projeto_discord_CharacterAi.git](https://github.com/seu-usuario/projeto_discord_CharacterAi.git)
    cd projeto_discord_CharacterAi
    ```

2.  [cite_start]**Instale as dependências necessárias:** [cite: 11]
    ```bash
    pip install -r requirements.txt.txt
    ```

3.  [cite_start]**Configure suas credenciais:** [cite: 1]
    * [cite_start]Crie ou edite o arquivo `.env` na raiz do projeto. [cite: 1]
    * Adicione seu `DISCORD_TOKEN` e as chaves da `CHARACTER_AI`.

4.  [cite_start]**Inicie o bot:** [cite: 10, 11]
    ```bash
    python main.py
    ```

## 🛠️ Tecnologias Utilizadas

* [cite_start]**Linguagem**: Python [cite: 11]
* [cite_start]**Bibliotecas**: Discord.py, CharacterAI API, Python-dotenv [cite: 1, 11]

---
**Desenvolvido por [Seu Nome/User]**
