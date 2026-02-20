# projeto_discord_ai
Um bot de Discord avançado para integração com CharacterAI. Possui sistema de persistência de sessões, gerenciamento de permissões por usuário, salvamento automático de histórico de conversas e suporte a múltiplas instâncias de chat.


# 🤖 Discord CharacterAI Bot

Este projeto é uma integração poderosa entre o Discord e a plataforma **CharacterAI**, permitindo que usuários interajam com personagens de IA diretamente em servidores do Discord. O sistema foi desenvolvido com foco em persistência de dados, garantindo que o contexto das conversas e as configurações de sessão não sejam perdidas.

## ✨ Funcionalidades

* **💬 Integração Real-time**: Converse com personagens do CharacterAI via chat do Discord.
* **🔐 Gerenciamento de Permissões**: Controle de acesso através de um serviço dedicado para permitir ou restringir usuários.
* **💾 Persistência de Sessão**: Salvamento automático das credenciais e estados de chat.
* **📜 Histórico de Conversas**: Armazenamento detalhado de mensagens primárias e logs de interação.
* **🛠️ Serviços de Suporte**: Inclui utilitários para limpeza de estados globais e monitoramento de variáveis de ambiente.

## 📂 Estrutura do Projeto

* **/bot**: Contém a lógica de comandos e eventos do Discord.
* **/services**: Scripts especializados em tarefas de back-end (salvamento de dados, sessões e permissões).
* **/save**: Diretório destinado ao armazenamento local de arquivos JSON e binários de usuários.
* **main.py**: O ponto de entrada principal da aplicação.
* **config.py**: Arquivo central de configurações do sistema.

## 🚀 Como Instalar e Rodar

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/projeto_discord_CharacterAi.git](https://github.com/seu-usuario/projeto_discord_CharacterAi.git)
   cd projeto_discord_CharacterAi
