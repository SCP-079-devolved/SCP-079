import disnake, os, random
from disnake.ext import commands

discord = disnake

scp079=commands.Bot(command_prefix='/', descripion = "Luke did the dumb and yeeted the bot, now I'm here!", test_guilds=[816430534757580830])
client = scp079

@client.slash_command()
async def ping(ctx):
    e=discord.Embed(title="ping", description=(f"Pong\n\n\n\nPing={round(client.latency)* 1000}ms."))
    await ctx.response.send_message(embed=e)

token = os.getenv('Token')