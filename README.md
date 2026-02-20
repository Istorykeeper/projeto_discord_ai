# projeto_discord_ai
Um bot de Discord avançado para integração com CharacterAI. Possui sistema de persistência de sessões, gerenciamento de permissões por usuário, salvamento automático de histórico de conversas e suporte a múltiplas instâncias de chat.

# 🤖 Discord CharacterAI Bot

Este projeto é uma integração entre o Discord e a plataforma CharacterAI, permitindo que os usuários conversem com personagens de inteligência artificial diretamente pelos canais do servidor.O sistema foi desenvolvido com foco em estabilidade, persistência de dados e controle de acesso. 

## ✨ Funcionalidades

💬 **Chat em Tempo Real**: Comandos e eventos otimizados para interação contínua com IAs. 

🔐 **Controle de Acesso**: Sistema de permissão para gerenciar quais usuários podem interagir com o bot.

💾 **Persistência de Sessão**: Salva automaticamente o estado da conversa para que o contexto não seja perdido entre reinicializações. 

📜 **Histórico de Mensagens**: Armazenamento de mensagens primárias e logs de conversas para auditoria e continuidade.

🔑 **Gestão de Credenciais**: Serviço dedicado para o armazenamento seguro de tokens e credenciais necessárias.

⚙️ **Monitoramento de Ambiente**: Possui um "watcher" para variáveis de ambiente e limpeza de estados globais.

## 📂 Estrutura do Projeto

**`bot/`**: Contém a lógica de comandos, eventos e a instância principal do bot Discord.
**`services/`**: Scripts responsáveis pelo backend, incluindo salvamento de sessões, mensagens e validação de usuários. 
**`save/`**: Diretório para armazenamento local de dados de usuários e configurações globais.
**`config.py`**: Centraliza as definições e variáveis globais do sistema. 
**`main.py`**: Ponto de entrada para execução da aplicação. 

## 🚀 Como Instalar

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/Istorykeeper/projeto_discord_ai.git](https://github.com/Istorykeeper/projeto_discord_ai.git)
    cd projeto_discord_ai
    ```

2.  **Instale as dependências necessárias:**
    ```bash
    pip install -r requirements.txt.txt
    ```

3.  **Configure suas credenciais:**
    * Crie ou edite o arquivo `.env` na raiz do projeto. 
    * Adicione seu `DISCORD_TOKEN` e as chaves da `CHARACTER_AI`.

4.  **Inicie o bot:**
    ```bash
    python main.py
    ```

## 🛠️ Tecnologias Utilizadas

**Linguagem**: Python
**Bibliotecas**: Discord.py, CharacterAI API, Python-dotenv ]

---
**Desenvolvido por Istorykeeper**
