import os
import discord
import logging
from discord.ext import commands
from dotenv import load_dotenv
from cogs.swearsitter import SwearSitter



def main():
    # get env data for server / bot
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    GUILD = os.getenv('DISCORD_SERVER')

    logging.basicConfig(level=logging.INFO)

    # configure bot
    intents = discord.Intents.default()
    client = commands.Bot(command_prefix="?", intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user.name} has connected to Discord")

    # load in Cogs
    client.load_extension("cogs.swearsitter")
    
    # start bot
    client.run(TOKEN)

if __name__ == "__main__":
    main()