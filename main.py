import disnake, os, random
from disnake.ext import commands
from config.cfg import general, messages

discord = disnake

scp079=commands.Bot(command_prefix=general.prefix, descripion = "Luke did the dumb and yeeted the bot, now I'm here!", test_guilds=[816430534757580830], help_command=None)
client = scp079

@client.slash_command()
async def ping(ctx):
    e=discord.Embed(title="ping", description=(f"Pong\n\n\n\nPing={round(client.latency)* 1000}ms."))
    await ctx.response.send_message(embed=e)

token = (os.getenv('Token'))