from bot.instance import bot
from services.env_watcher import start_env_watcher
from discord.ext import commands

cai_client = None 
@bot.event
async def on_ready():
    print(f"Logado com {bot.user}")
    start_env_watcher()


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"⚠️ Faltando argumento: `{error.param.name}` é obrigatório.")
    else:
        raise error


@bot.event
async def on_disconnect():
    global cai_client
    if cai_client:
        await cai_client.close_session()
