import disnake, os, random, aiohttp, json
from disnake.ext import commands
from config.cfg import general, messages, publiccommands


discord = disnake

scp079=commands.Bot(command_prefix=general.prefix, descripion = "Luke did the dumb and yeeted the bot, now I'm here!", test_guilds=[816430534757580830], help_command=None)
client = scp079

@scp079.event
async def on_ready():
    print(client.user.name,"is online")

@client.slash_command()
async def comedy(ctx):
    await ctx.send(file=discord.File("images/comedy.png"))

@client.slash_command()
async def ping(ctx):
    e=discord.Embed(title="ping", description=(f"Pong\n\n\n\nPing={round(client.latency)* 1000}ms."))
    await ctx.response.send_message(embed=e)

@client.slash_command()
async def pp_size(ctx):
    embed = discord.Embed(title = f"{ctx.author} your pp size is...", description = (f"{random.randint(1, 500)} inches"), color = 0x5867fe)
    await ctx.send(embed = embed)

@client.slash_command()
@commands.has_permission(ban_members=True)
async def ban(ctx, member: discord.Member, reason = None):
      if reason == None:
           reason = messages.ban_message
      author = ctx.author
      authorid = ctx.author.id
      await member.send(f'You have been banned from {ctx.guild.name} for {reason} by {author}')
      await ctx.guild.ban(member, reason = reason)
      await ctx.channel.send(f'{member} has been banned for {reason} by <@{authorid}> ')

@client.slash_command()
@commands.has_permission(kick_members=True)
async def kick(ctx, member: discord.Member, reason = None):
    if reason == None:
      reason = messages.kick_message
    author = ctx.author
    authorid = ctx.author.id
    invitelink = await ctx.channel.create_invite(max_uses=1,unique=True)
    server = ctx.guild
    await member.send(f'{author} has kicked you from {server} for {reason}. rejoin with this link {invitelink}')
    await ctx.send(f'Kicked {member} for you <@{authorid}>, they have recived another invite link but they have hopefully learned')
    await ctx.guild.kick(member, reason = reason)

@client.slash_command()
async def meme(ctx):
    embed = discord.Embed(title="Welcome to r/dankmemes (or r/memes)", description=f"<@{ctx.author.id}>", color = 0x5867fe)
    rng = random.randit(1, 2)
    async with aiohttp.ClientSession() as cs:
      if rng == 1:
        async with cs.get(f'https://www.reddit.com/r/Memes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)
      if rng == 2:
        async with cs.get(f'https://www.reddit.com/r/DankMemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)

token = (os.getenv('Token'))