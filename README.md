# projeto_discord_ai
Um bot de Discord avançado para integração com CharacterAI. Possui sistema de persistência de sessões, gerenciamento de permissões por usuário, salvamento automático de histórico de conversas e suporte a múltiplas instâncias de chat.


# 🤖 Discord CharacterAI Integration Framework

Este projeto é uma ponte avançada entre o ecossistema do Discord e a API do **CharacterAI**. Diferente de integrações simples, este bot foi construído com uma arquitetura modular focada em **estabilidade** e **persistência**, permitindo que personagens de IA mantenham conversas longas e coerentes dentro do servidor.

## 🧐 Como o Bot Funciona?

O bot opera através de um ciclo de vida inteligente que garante que nenhuma informação seja perdida entre as sessões de uso:

1. **Autenticação e Sessão**: Ao ser iniciado, o bot carrega credenciais seguras e restabelece a conexão com a API do CharacterAI. Ele utiliza um gestor de sessões para verificar se existe um chat anterior ativo.
2. **Processamento de Mensagens**: Quando um utilizador interage, o bot consulta o módulo de permissões para verificar se o utilizador está autorizado. Se sim, a mensagem é enviada para a IA.
3. **Memória e Persistência**: Cada resposta da IA e cada pergunta do utilizador são filtradas e salvas localmente. Isso permite que, mesmo que o bot seja desligado, ao voltar, ele saiba exatamente onde a conversa parou.
4. **Monitorização**: O sistema inclui um "Watcher" que observa ficheiros de configuração e estados globais, permitindo ajustes em tempo real sem interrupção do serviço.

## ✨ Funcionalidades Detalhadas

### 🧠 Integração com IA
* **Chat Fluido**: Respostas em tempo real integradas nativamente nos canais do Discord.
* **Manutenção de Contexto**: Sistema que evita que a IA "perca a memória" durante conversas extensas.

### 🛡️ Segurança e Controle
* **Módulo de Permissões (`permit_user.py`)**: Sistema de lista branca que permite aos administradores controlar exatamente quem pode consumir os recursos do bot.
* **Gestão de Credenciais**: Armazenamento isolado de tokens para evitar exposição de chaves sensíveis.

### 💾 Gestão de Dados (Persistence Layer)
* **Save System**: Localizado na pasta `/save`, o bot utiliza serialização de dados para guardar:
    * Histórico completo de diálogos.
    * Mensagens primárias (âncoras de contexto).
    * Tokens de sessão e estados de utilizadores específicos.

### 🛠️ Estabilidade Técnica
* **Limpeza Global**: Rotinas que limpam ficheiros temporários e resets de memória para evitar sobrecarga do servidor.
* **Watcher de Ambiente**: Carregamento dinâmico do ficheiro `.env` para atualizações de tokens sem necessidade de reiniciar todo o código.

## 📂 Estrutura de Pastas

* **`/bot`**: Contém a interface do utilizador (comandos) e os gatilhos de eventos.
* **`/services`**: Contém a inteligência de backend (salvamento, validação e lógica de negócio).
* **`/save`**: Onde a "memória" do bot reside (ficheiros JSON/binários).
* **`main.py`**: Orquestrador principal do sistema.

## 🚀 Guia de Instalação

1. **Clonar o Repositório**:
   ```bash
   git clone [https://github.com/Istorykeeper/projeto_discord_ai.git](https://github.com/Istorykeeper/projeto_discord_ai.git)
   cd projeto_discord_ai
