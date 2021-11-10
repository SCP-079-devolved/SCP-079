import disnake, os, random, aiohttp, json
from disnake.ext import commands
from config.cfg import general, messages
from server import runserver

runserver()
discord = disnake

scp079=commands.Bot(command_prefix=commands.when_mentioned_or(general.prefix), descripion = "Luke did the dumb and yeeted the bot, now I'm here!", test_guilds=[899374265512624138, 905153470993158174], help_command=None, intents=discord.Intents.all(), case_insensitive=True)
client = scp079

@scp079.event
async def on_ready():
    print(client.user.name,"is online")
    await scp079.change_presence(status=discord.Status.idle, activity = discord.Game(name = general.MOTD))

@client.slash_command()
async def pp_width(ctx):
    '''Your pp width....'''
    if ctx.author.id == 756147569880727627:
        embed = discord.Embed(title = f"{ctx.author} your pp width is...", description = (f"1 inch u noob"), color = 0x5867f2)
    else:    
        embed = discord.Embed(title = f"{ctx.author} your pp width is...", description = (f"{random.randint(1, 10)} inches"), color = 0x5867f2)
    await ctx.response.send_message(embed = embed)
    print(f'command pp_width run in {ctx.guild}')

@client.command()
async def comedy(ctx):
    '''Some comedy pic'''
    author = ctx.author
    await author.send("https://cdn.discordapp.com/attachments/903454233037254666/904242252434505748/comedy.png")
    print(f'command comedy run in {ctx.guild}')

@client.slash_command()
async def ping(ctx):
    '''ping ...'''
    ping = int(round(client.latency, 3) * 1000)
    e=discord.Embed(title="ping", description=(f"Pong\n\nPing={ping}ms."))
    await ctx.response.send_message(embed=e)

@client.slash_command()
async def pp_size(ctx):
    '''Your pp size...'''
    channel = client.get_channel(899378836968439878)
    if ctx.author.id == 756147569880727627:
        embed = discord.Embed(title = f"{ctx.author} your pp size is...", description = (f"{random.randint(1,2)} inch u noob"), color = 0x5867f2)

    else:
        size = random.randint(1, 500)
        print(size)
        if size == 152:
            yes=random.randint(500, 501)
            if yes == 501:
                embed = discord.Embed(title = f"{ctx.author} your pp size is...", description = ("501 inches, wait something ain't right here"), color = 0x5867f2)
                print(ctx.author, "GOT 501 INCHES")
                channel.send(f'ATTENTION @everyone, user <@{ctx.author.id}> got the RAREST dick size, 501, 501 inches is impossible but they still got it, congrats! ')
            else:
                embed = discord.Embed(title = f"{ctx.author} your pp size is...", description = ("500 inches"), color = 0x5867f2)
                
            
        else:
            embed = discord.Embed(title = f"{ctx.author} your pp size is...", description = (f"{size} inches"), color = 0x5867f2)
    await ctx.response.send_message(embed = embed)
    print(f'command pp_size run in {ctx.guild}')

@client.slash_command()
@commands.has_any_role('Dev', 'Head Mod', 'Mod')
async def ban(ctx, member: discord.Member,* ,reason = None):
    '''To Ban anyone you want in the server! (MOD command)'''
    if member == ctx.author:
        ctx.respoonse.send_message('no banning yourself')    
    else:
        if reason == None:
           reason = messages.ban_message
        author = ctx.author
        authorid = ctx.author.id
        await member.send(f'You have been banned from {ctx.guild.name} for {reason} by {author}')
        await ctx.guild.ban(member, reason = reason)
        await ctx.channel.send(f'{member} has been banned for {reason} by <@{authorid}> ')
    print(f'ban command run in {ctx.guild}')

@client.slash_command()
@commands.has_any_role('Dev', 'Head Mod', 'Mod')
async def kick(ctx, member: discord.Member,* ,reason = None):
    '''To Kick anyone you want in the server! (MOD command)'''
    if member == ctx.author:
        await ctx.response.send_message('no kicking yourself noob')
        pass
    else:
        if reason == None:
            reason = messages.kick_message
        author = ctx.author
        authorid = ctx.author.id
        invitelink = await ctx.channel.create_invite(max_uses=1,unique=True)
        server = ctx.guild
        await member.send(f'{author} has kicked you from {server} for {reason}. rejoin with this link {invitelink}')
        await ctx.response.send_message(f'Kicked {member} for you <@{authorid}>, they have recived another invite link but they have hopefully learned')
        await ctx.guild.kick(member, reason = reason)
    print(f'kick command run in {ctx.guild}')

@client.command()
async def redacted(ctx):
    await ctx.author.send('https://cdn.discordapp.com/attachments/903454233037254666/906806501061046302/unknown.png')

@client.command()
async def aaron(ctx):
    author = ctx.author
    await author.send('you owe me ∞ money UwU')
    await author.send('https://cdn.discordapp.com/attachments/903454233037254666/906049968312311848/Screenshot_20210928-230318_Discord.png')

@client.command()
async def luke(ctx):
    author = ctx.author
    await author.send('UwU you t-touchy my tail')
    await author.send('https://cdn.discordapp.com/attachments/903454233037254666/904242228803829770/luke.png')

@client.command()
async def sniper(ctx):
    author = ctx.author
    await author.send('https://cdn.discordapp.com/attachments/903454233037254666/904242035110846504/sniper.jpg')

@client.command()
async def sneaky(ctx):
    author = ctx.author
    await author.send('https://cdn.discordapp.com/attachments/903454233037254666/904241982870810635/sneaky1.png')
    await author.send('https://cdn.discordapp.com/attachments/903454233037254666/904241944014753792/sneaky2.png')

@client.command()
async def december(ctx):
    author = ctx.author
    await author.send('https://cdn.discordapp.com/attachments/903454233037254666/903454303887433808/MirMfPscvzz9Gp1v9Ht2AsHvjZrPx903zOXAXltYiXlTGg4sq5k8KXsmqpyjPX34tbUOG5PT6GisBCtDRrU19YiNSUVAceCFK8hEAgEgneXNyJWAoFAIBC8CkKsBAKBQLDmEWIlEAgEgjWPECuBQCAQrHmEWAkEAoFgzSPESiAQCARrHiFWAoFAIFjzCLESCAQCwZpHiJVAIBAI1jxCrAQCgUCw5hFiJRAIBII1jxArgUAgEKx5hFgJBAKBYM0jxEogEAgEax4hVgKBQCBY8wixEggEAsEa5yjP4liNfAZxcP4AAAAAElFTkSuQmCC.png')
    await author.send('https://cdn.discordapp.com/attachments/903454233037254666/903454373043109928/IWSvBzO7ZAAAAABJRU5ErkJggg.png')
    await author.send('https://cdn.discordapp.com/attachments/903454233037254666/903454391498076170/BzGf2butOoxyAAAAAElFTkSuQmCC.png')
    await author.send('https://cdn.discordapp.com/attachments/903454233037254666/903454410900930570/x8XIKFENCaRlwAAAABJRU5ErkJggg.png')

@client.slash_command()
async def bug_report(ctx, title, *, description):
    '''Use this to report a bug! '''
    print(f'A bug report from {ctx.author}:\n Title:\n {title} \n Description: \n {description}\n ')
    await ctx.response.send_message(f'Bug has been reported! Thanks 😉')
    print(f'bug report from {ctx.guild}')

token = general.token
client.run(token)
