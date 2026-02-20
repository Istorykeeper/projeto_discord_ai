from config import DISCORD_TOKEN
import bot.instance as bot_instance


# Importa para registrar eventos e comandos
import bot.events
import bot.commands


if __name__ == "__main__":
    bot_instance.bot.run(DISCORD_TOKEN)

