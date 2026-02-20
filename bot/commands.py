import os
import asyncio
import discord
from dotenv import set_key
from PyCharacterAI import get_client
from PyCharacterAI.exceptions import SessionClosedError

from bot.instance import bot
from bot import events  
from services.save_credentials import save_credentials, load_character_user, load_token_user, load_status_user
from services.save_session import save_chat_id, load_chat_id
from services.save_messages import save_message
from services.clear_global import clear
from services.save_primary_message import save_primary_message, load_primary_message
from services.permit_user import add_user, remove_user, load_ids

chat = None
iniciado = False


'''


░█████╗░░█████╗░███╗░░░███╗░█████╗░███╗░░██╗██████╗░░█████╗░░██████╗
██╔══██╗██╔══██╗████╗░████║██╔══██╗████╗░██║██╔══██╗██╔══██╗██╔════╝
██║░░╚═╝██║░░██║██╔████╔██║███████║██╔██╗██║██║░░██║██║░░██║╚█████╗░
██║░░██╗██║░░██║██║╚██╔╝██║██╔══██║██║╚████║██║░░██║██║░░██║░╚═══██╗
╚█████╔╝╚█████╔╝██║░╚═╝░██║██║░░██║██║░╚███║██████╔╝╚█████╔╝██████╔╝
░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░░╚════╝░╚═════╝░

░██████╗░██╗░░░░░░█████╗░██████╗░░█████╗░██╗░██████╗
██╔════╝░██║░░░░░██╔══██╗██╔══██╗██╔══██╗██║██╔════╝
██║░░██╗░██║░░░░░██║░░██║██████╦╝███████║██║╚█████╗░
██║░░╚██╗██║░░░░░██║░░██║██╔══██╗██╔══██║██║░╚═══██╗
╚██████╔╝███████╗╚█████╔╝██████╦╝██║░░██║██║██████╔╝
░╚═════╝░╚══════╝░╚════╝░╚═════╝░╚═╝░░╚═╝╚═╝╚═════╝░

'''

# mandar mensagem para o bot
@bot.command()
async def falar(ctx, *, mensagem):
    global chat, iniciado

    CHARACTERAI_TOKEN = os.getenv("CHARACTERAI_TOKEN")
    CHARACTER_ID = os.getenv("CHARACTER_ID")
    full_folder = r'save\global\session.json'
    full_folder_messages = r'save\global\history.json'

    if not CHARACTERAI_TOKEN:
        await ctx.send('O usuario não informou o token. Utilize !enviar_token')
        return

    if not CHARACTER_ID:
        await ctx.send('O usuario não informou o id do personagem. Utilize !enviar_character')
        return

    try:
        if not getattr(events, "cai_client", None):
            events.cai_client = await get_client(token=CHARACTERAI_TOKEN)

        saved_chat_id = load_chat_id(full_folder)

        if saved_chat_id:
            chat = type("Chat", (), {"chat_id": saved_chat_id})()
        else:
            chat, _ = await events.cai_client.chat.create_chat(CHARACTER_ID)
            save_chat_id(chat.chat_id, full_folder)

        iniciado = True

        async with ctx.typing():
            resposta = await events.cai_client.chat.send_message(
                CHARACTER_ID,
                chat.chat_id,
                mensagem
            )

        texto_resposta = resposta.get_primary_candidate().text

        def dividir_texto(texto, limite=2000):
            partes = []
            while len(texto) > limite:
                corte = texto.rfind("\n", 0, limite)
                if corte == -1:
                    corte = limite
                partes.append(texto[:corte])
                texto = texto[corte:]
            partes.append(texto)
            return partes

        partes = dividir_texto(texto_resposta)

        for parte in partes:
            await ctx.send(parte)

        save_message(ctx.author.id, mensagem, full_folder_messages)
        save_message(resposta.author_name, texto_resposta, full_folder_messages)

    except SessionClosedError:
        await ctx.send("Sessão com CharacterAI foi fechada.")

    except Exception as e:
        await ctx.send(f"Erro ao falar com o personagem: {e}")



# mensagem inicial do bot que aparece no site.
@bot.command()
async def mensagem(ctx):
    global iniciado
    try:
     if iniciado:
      await ctx.send(f'{greeting.get_primary_candidate().text}')
      return
     else:
      await ctx.send('Você não iniciou uma conversa com o bot utilizando !falar.')
      return
    except Exception as e:
        await ctx.send(f'Ocorreu o seguinte erro: {e}. Talvez você não iniciou o bot.')
        return




# comando de ajuda
@bot.hybrid_command(name="ajuda", description="Exibe o painel de comandos do bot.")
async def ajuda(ctx):
    embed = discord.Embed(
        title="🤖 • Painel de Comandos",
        description=(
            "Seja bem-vindo ao menu de ajuda!\n"
            "Abaixo estão todos os comandos organizados por categoria.\n\n"
            "Use os comandos conforme sua necessidade."
        ),
        color=discord.Color.blue()
    )

    embed.add_field(
        name="🌍 • Comandos Globais",
        value=(
            "`!!ajuda` → Exibe este painel de ajuda.\n"
            "`!!falar` → Conversa global com o bot (todos veem).\n"
            "`!!sobre` → Informações sobre o bot e criador.\n"
            "`!!mensagem` → Mostra a mensagem inicial padrão."
        ),
        inline=False
    )

    embed.add_field(
        name="👤 • Comandos Individuais",
        value=(
            "`!!privado` → Inicia conversa privada.\n"
            "`!!falarprivado` → Interage com seu personagem privado.\n"
            "`!!mensagemprivado` → Mostra a mensagem inicial privada.\n"
            "`!!clear_s_p` → Limpa a sessão privada atual.\n"
            "`!!clear_h_p` → Apaga todo histórico privado salvo.\n"
            "`!!historico_privado` → Envia seu histórico no privado."
        ),
        inline=False
    )

    embed.add_field(
        name="🔐 • Administrativos (Somente Dono)",
        value=(
            "`!!historico_global` → Envia o histórico global.\n"
            "`!!clear_h_g` → Limpa o histórico global.\n"
            "`!!clear_s_g` → Reseta a sessão global do bot.\n"
            "`!!adicionar_usuario` → Adiciona administrador (via ID).\n"
            "`!!remover_usuario` → Remove administrador.\n"
            "`!!listar_usuarios` → Lista administradores.\n"
            "`!!enviar_token` → Define novo token (somente dono).\n"
            "`!!enviar_character` → Define novo personagem."
        ),
        inline=False
    )

    embed.set_footer(
        text=f"Solicitado por {ctx.author.name}",
        icon_url=ctx.author.display_avatar.url
    )

    if bot.user.avatar:
        embed.set_thumbnail(url=bot.user.avatar.url)

    await ctx.send(embed=embed)




# sobre o bot
@bot.hybrid_command(name="sobre", description="Mostra informações sobre o bot.")
async def sobre(ctx):

    embed = discord.Embed(
        title="✨ Sobre o Bot",
        description=(
            "Este bot foi criado com dedicação, estudo e muita vontade de evoluir.\n\n"
            "Ele nasceu como um projeto de aprendizado, focado em integração com IA "
            "e sistemas de conversa inteligentes dentro do Discord."
        ),
        color=discord.Color.blurple()
    )

    embed.add_field(
        name="🛠 Desenvolvimento",
        value=(
            "Desenvolvido utilizando:\n"
            "• `Python`\n"
            "• `discord.py`\n"
            "• Integração com IA externa PyCharacterAI\n\n"
            "Cada sistema foi estruturado para permitir sessões globais "
            "e privadas, com controle de histórico e administração."
        ),
        inline=False
    )

    embed.add_field(
        name="🎯 Objetivo do Projeto",
        value=(
            "Criar uma experiência interativa, imersiva e organizada.\n"
            "Permitir que usuários conversem com personagens "
            "de forma global ou privada, mantendo histórico e controle."
        ),
        inline=False
    )

    embed.add_field(
        name="👑 Criador",
        value=(
            f"Desenvolvido por **IstoryKeeper**\n"
            "Projeto em constante evolução 🚀"
        ),
        inline=False
    )

    if bot.user.avatar:
        embed.set_thumbnail(url=bot.user.avatar.url)

    embed.set_image(
        url="https://i.pinimg.com/736x/77/1d/d6/771dd6b41626f2b4cae6daab06648cbb.jpg" 
    )

    embed.set_footer(
        text=f"Solicitado por {ctx.author.name}",
        icon_url=ctx.author.display_avatar.url
    )

    await ctx.send(embed=embed)



'''


░█████╗░░█████╗░███╗░░░███╗░█████╗░███╗░░██╗██████╗░░█████╗░░██████╗
██╔══██╗██╔══██╗████╗░████║██╔══██╗████╗░██║██╔══██╗██╔══██╗██╔════╝
██║░░╚═╝██║░░██║██╔████╔██║███████║██╔██╗██║██║░░██║██║░░██║╚█████╗░
██║░░██╗██║░░██║██║╚██╔╝██║██╔══██║██║╚████║██║░░██║██║░░██║░╚═══██╗
╚█████╔╝╚█████╔╝██║░╚═╝░██║██║░░██║██║░╚███║██████╔╝╚█████╔╝██████╔╝
░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░░╚════╝░╚═════╝░

░█████╗░██████╗░███╗░░░███╗██╗███╗░░██╗██╗░██████╗████████╗██████╗░░█████╗░████████╗██╗██╗░░░██╗░█████╗░
██╔══██╗██╔══██╗████╗░████║██║████╗░██║██║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝██║██║░░░██║██╔══██╗
███████║██║░░██║██╔████╔██║██║██╔██╗██║██║╚█████╗░░░░██║░░░██████╔╝███████║░░░██║░░░██║╚██╗░██╔╝██║░░██║
██╔══██║██║░░██║██║╚██╔╝██║██║██║╚████║██║░╚═══██╗░░░██║░░░██╔══██╗██╔══██║░░░██║░░░██║░╚████╔╝░██║░░██║
██║░░██║██████╔╝██║░╚═╝░██║██║██║░╚███║██║██████╔╝░░░██║░░░██║░░██║██║░░██║░░░██║░░░██║░░╚██╔╝░░╚█████╔╝
╚═╝░░╚═╝╚═════╝░╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░╚═╝░░░░╚════╝░

'''


# mandar o historico global
@bot.command()
async def historico_global(ctx):
    folder_history = f'save/global/history.json'
    usuarios_permitidos = f"save/global/permited_users.txt"
    ids = load_ids(usuarios_permitidos)
    if ctx.author.id != int(os.getenv('DONO_ID')) and str(ctx.author.id) not in ids:
        await ctx.send('Acesso Bloqueado, comando apenas do dono.')
        return
    try:
        if not os.path.exists(folder_history) or os.path.getsize(folder_history) == 0:
                await ctx.send("Você não conversou com o bot ou limpou o histórico.")
        else:
            await ctx.author.send("Aqui seu histórico:")
            await ctx.author.send(file=discord.File(folder_history))
            await ctx.send("Histórico enviado na sua DM.")

    except discord.Forbidden:
        await ctx.send(f"{ctx.author.mention}, não consegui te enviar DM. Verifique suas configurações de privacidade.")
        return



# adicionar um usuario administrador
@bot.command()
async def adicionar_usuario(ctx, *, usuario_id):
    global_users = f'save/global/permited_users.txt'
    if ctx.author.id != int(os.getenv('DONO_ID')):
        await ctx.send('Acesso Bloqueado, comando apenas do dono.')
        return
    try:
        add_user(usuario_id, global_users)
        await ctx.send(f"O usuário <@{usuario_id}> foi adicionado aos administradores.")
    
    except Exception as e:
        await ctx.send(f"Ocorreu o seguinte erro: {e}")



# remover um usuario administrador
@bot.command()
async def remover_usuario(ctx, *, usuario_id):
    global_users = f'save/global/permited_users.txt'
    if ctx.author.id != int(os.getenv('DONO_ID')):
        await ctx.send('Acesso Bloqueado, comando apenas do dono.')
        return
    try:
        remove_user(usuario_id, global_users)
        await ctx.send(f"O usuário <@{usuario_id}> foi removido.")
    
    except Exception as e:
        await ctx.send(f"Ocorreu o seguinte erro: {e}")



# listar os administradores
@bot.command()
async def listar_usuarios(ctx):
    global_users = f'save/global/permited_users.txt'
    if ctx.author.id != int(os.getenv('DONO_ID')):
        await ctx.send('Acesso Bloqueado, comando apenas do dono.')
        return
    try:
        lista = load_ids(global_users)
        await ctx.send(f"Lista de ids dos usuaríos: {lista}")
    
    except Exception as e:
        await ctx.send(f"Ocorreu o seguinte erro: {e}")




# limpar o historico global
@bot.command()
async def clear_h_g(ctx):
    usuarios_permitidos = f"save/global/permited_users.txt"
    ids = load_ids(usuarios_permitidos)
    if ctx.author.id != int(os.getenv('DONO_ID')) and str(ctx.author.id) not in ids:
        await ctx.send('Acesso Bloqueado, comando apenas do dono.')
        return
    try:
        file_path = r'save\global\history.json'
        clear(file_path)
        await ctx.send(f"Arquivo de sessão globalmente limpado.")
    except Exception as e:
         await ctx.send(f"Ocorreu o seguinte erro: {e}")



# limpar a sessão global
@bot.command()
async def clear_s_g(ctx):
    usuarios_permitidos = f"save/global/permited_users.txt"
    ids = load_ids(usuarios_permitidos)
    if ctx.author.id != int(os.getenv('DONO_ID')) and str(ctx.author.id) not in ids:
        await ctx.send('Acesso Bloqueado, comando apenas do dono.')
        return
    try:
        file_path = r'save\global\session.json'
        clear(file_path)
        await ctx.send(f"Arquivo de sessão globalmente limpado.")
    except Exception as e:
         await ctx.send(f"Ocorreu o seguinte erro: {e}")



# trocar o token da conta do character.ai
@bot.command()
async def enviar_token(ctx):
    if ctx.author.id != int(os.getenv('DONO_ID')):
        await ctx.send('Acesso Bloqueado, comando apenas do dono.')
        return
    try:
        await ctx.author.send("Digite seu token do Character.Ai: ")
    except discord.Forbidden:
        await ctx.send(f"{ctx.author.mention}, não consegui te enviar DM. Verifique suas configurações de privacidade.")
        return

    def check(m):
        return m.author == ctx.author and isinstance(m.channel, discord.DMChannel)

    try:
        token = await bot.wait_for('message', timeout=60.0, check=check)
    except asyncio.TimeoutError:
        await ctx.author.send("Você demorou muito para responder. Por favor reenvie o comando.")
        return

    await ctx.author.send(f"Token digitado: {token.content}")
    dotenv_file = '.env'
    set_key(dotenv_file, 'CHARACTERAI_TOKEN', token.content)



# enviar/trocar um personagem do c.ai(globalmente)
@bot.command()
async def enviar_character(ctx):
    if ctx.author.id != int(os.getenv('DONO_ID')):
        await ctx.send('Acesso Bloqueado, comando apenas do dono.')
        return
    try:
        await ctx.author.send("Digite o id do personagem: ")
    except discord.Forbidden:
        await ctx.send(f"{ctx.author.mention}, não consegui te enviar DM. Verifique suas configurações de privacidade.")
        return

    def check(m):
        return m.author == ctx.author and isinstance(m.channel, discord.DMChannel)

    try:
        id = await bot.wait_for('message', timeout=60.0, check=check)
    except asyncio.TimeoutError:
        await ctx.author.send("Você demorou muito para responder. Por favor reenvie o comando.")
        return

    await ctx.author.send(f"ID Digitado: {id.content}")
    dotenv_file = '.env'
    set_key(dotenv_file, 'CHARACTER_ID', id.content)

'''


░█████╗░░█████╗░███╗░░░███╗░█████╗░███╗░░██╗██████╗░░█████╗░░██████╗
██╔══██╗██╔══██╗████╗░████║██╔══██╗████╗░██║██╔══██╗██╔══██╗██╔════╝
██║░░╚═╝██║░░██║██╔████╔██║███████║██╔██╗██║██║░░██║██║░░██║╚█████╗░
██║░░██╗██║░░██║██║╚██╔╝██║██╔══██║██║╚████║██║░░██║██║░░██║░╚═══██╗
╚█████╔╝╚█████╔╝██║░╚═╝░██║██║░░██║██║░╚███║██████╔╝╚█████╔╝██████╔╝
░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░░╚════╝░╚═════╝░

██████╗░██████╗░██╗██╗░░░██╗░█████╗░██████╗░░█████╗░░██████╗
██╔══██╗██╔══██╗██║██║░░░██║██╔══██╗██╔══██╗██╔══██╗██╔════╝
██████╔╝██████╔╝██║╚██╗░██╔╝███████║██║░░██║██║░░██║╚█████╗░
██╔═══╝░██╔══██╗██║░╚████╔╝░██╔══██║██║░░██║██║░░██║░╚═══██╗
██║░░░░░██║░░██║██║░░╚██╔╝░░██║░░██║██████╔╝╚█████╔╝██████╔╝
╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═════╝░

'''


# mostrar a mensagem privada da pessoa
@bot.command()
async def mensagemprivado(ctx):
    folder_primary = f'save/usuarios/{ctx.author.id}/primary_message.json'
    folder_status = f'save/usuarios/{ctx.author.id}/credentials.json'
    STATUS_PRIVATE = load_status_user(folder_status)
    try:
     if STATUS_PRIVATE:
      texto = load_primary_message(folder_primary)
      await ctx.send(texto)
      return
     else:
      await ctx.send('Você não iniciou uma conversa com o bot utilizando !privado.')
      return
    except Exception as e:
        await ctx.send(f'Ocorreu o seguinte erro: {e}. Talvez você não iniciou o bot.')
        return




# criar um chat privado
@bot.command()
async def privado(ctx):
    user_folder = f"save/usuarios/{ctx.author.id}"
    if not os.path.exists(user_folder):
                os.makedirs(user_folder)
    file_path = f"{user_folder}/credentials.json"
    try:
        await ctx.author.send("Digite o id do personagem: ")
    except discord.Forbidden:
        await ctx.send(f"{ctx.author.mention}, não consegui te enviar DM. Verifique suas configurações de privacidade.")
        return

    def check(m):
        return m.author == ctx.author and isinstance(m.channel, discord.DMChannel)

    try:
        id = await bot.wait_for('message', timeout=60.0, check=check)
    except asyncio.TimeoutError:
        await ctx.author.send("Você demorou muito para responder. Por favor reenvie o comando.")
        return
    
    try:
        await ctx.author.send("Digite o seu token: ")
    except discord.Forbidden:
        await ctx.send(f"{ctx.author.mention}, não consegui te enviar DM. Verifique suas configurações de privacidade.")
        return
    

    try:
        token = await bot.wait_for('message', timeout=60.0, check=check)
    except asyncio.TimeoutError:
        await ctx.author.send("Você demorou muito para responder. Por favor reenvie o comando.")
        return

    await ctx.author.send(f"ID Digitado: {id.content}\nToken Digitado: {token.content}\n Você agora pode utilizar !falarprivado")
    save_credentials(ctx.author.id, token.content, id.content, file_path)




# falar com o privado individual
@bot.command()
async def falarprivado(ctx, *, mensagem):
    global chat, greeting

    user_folder = f"save/usuarios/{ctx.author.id}/credentials.json"
    session_folder = f"save/usuarios/{ctx.author.id}/session.json"
    message_folder = f"save/usuarios/{ctx.author.id}/history.json"
    primary_message_folder = f'save/usuarios/{ctx.author.id}/primary_message.json'

    CHARACTERAI_TOKEN = load_token_user(user_folder)
    CHARACTER_ID = load_character_user(user_folder)
    STATUS_PRIVATE = load_status_user(user_folder)

    if not STATUS_PRIVATE:
        await ctx.send("Digite o comando !privado")
        return

    if not CHARACTERAI_TOKEN:
        await ctx.send("O usuario não informou o token. Utilize !enviar_token")
        return

    if not CHARACTER_ID:
        await ctx.send("O usuario não informou o id do personagem. Utilize !enviar_character")
        return

    try:
        events.cai_client = await get_client(token=CHARACTERAI_TOKEN)
        chat_id = load_chat_id(session_folder)

        if chat_id:
            try:
                chat = await events.cai_client.chat.get_chat(
                    CHARACTER_ID,
                    chat_id
                )
            except Exception:
                chat, greeting = await events.cai_client.chat.create_chat(
                    CHARACTER_ID
                )
                save_chat_id(chat.chat_id, session_folder)
        else:
            chat, greeting = await events.cai_client.chat.create_chat(
                CHARACTER_ID
            )
            save_chat_id(chat.chat_id, session_folder)

        async with ctx.typing():
            resposta = await events.cai_client.chat.send_message(
                CHARACTER_ID,
                chat.chat_id,
                mensagem
            )

        texto = resposta.get_primary_candidate().text

        def dividir_texto(texto, limite=2000):
            partes = []
            while len(texto) > limite:
                corte = texto.rfind("\n", 0, limite)
                if corte == -1:
                    corte = limite
                partes.append(texto[:corte])
                texto = texto[corte:]
            partes.append(texto)
            return partes

        partes = dividir_texto(texto)

        for parte in partes:
            await ctx.send(parte)

    
        save_message(ctx.author.id, mensagem, message_folder)
        save_message(resposta.author_name, texto, message_folder)
        save_primary_message(greeting.get_primary_candidate().text, primary_message_folder)

    except SessionClosedError:
        await ctx.send("Sessão com CharacterAI foi fechada.")

    except Exception as e:
        await ctx.send(
            f"Ocorreu um erro ao falar com o personagem. Erro: {e}"
        )






# limpar a sessão individualmente
@bot.command()
async def clear_s_p(ctx):
    folder_session = f'save/usuarios/{ctx.author.id}/session.json'
    try:
        if not os.path.exists(folder_session) or os.path.getsize(folder_session) == 0:
            await ctx.send("A sessão ja esta vazia ou limpa. ou você não cricou usando !privado")
            return
        else:
            clear(folder_session)
            await ctx.send("Sessão limpa com sucesso.")
    except Exception as e:
        await ctx.send(f"Ocorreu o seguinte erro: {e}")
       


# limpar o historico individual
@bot.command()
async def clear_h_p(ctx):
    folder_history = f'save/usuarios/{ctx.author.id}/history.json'
    try:
        if not os.path.exists(folder_history) or os.path.getsize(folder_history) == 0:
            await ctx.send("O histórico já esta limpo ou você não iniciou um chat com !privado")
            return
        else:
            clear(folder_history)
            await ctx.send("Histórico limpo com sucesso.")
    except Exception as e:
        await ctx.send(f"Ocorreu o seguinte erro: {e}")
    



# mostrar todo o historico da pessoa
@bot.command()
async def historico_privado(ctx):
    folder_history = f'save/usuarios/{ctx.author.id}/history.json'
    try:
        if not os.path.exists(folder_history) or os.path.getsize(folder_history) == 0:
                await ctx.send("Você não conversou com o bot ou limpou o histórico.")
        else:
            await ctx.author.send("Aqui seu histórico:")
            await ctx.author.send(file=discord.File(folder_history))
            await ctx.send("Histórico enviado na sua DM.")

    except discord.Forbidden:
        await ctx.send(f"{ctx.author.mention}, não consegui te enviar DM. Verifique suas configurações de privacidade.")

        return
