import disnake, os, random, aiohttp, json
from disnake.ext import commands
from config.cfg import general, messages, ppsize
from server import runserver

runserver()
discord = disnake
scp079=commands.Bot(command_prefix=commands.when_mentioned_or(general.prefix), descripion = "SCP-079 0.1.4", test_guilds=['INSERT_SERVER_ID_HERE'], help_command=None, intents=discord.Intents.all(), case_insensitive=True)
client = scp079

@scp079.event
async def on_ready():
    print(client.user.name,"is online")
    await scp079.change_presence(status=discord.Status.idle, activity = discord.Game(name = general.MOTD))
    f = open("cmdlogs.txt", "w+")
    f.write('\tBOT ONLINE\n')
    f.close()

@client.slash_command()
async def pp_width(ctx):
    '''Your pp width....'''
    if ctx.author.id == 756147569880727627:
        embed = discord.Embed(title = f"{ctx.author} your pp width is...", description = (f"1 inch u noob"), color = 0x5867f2)
    else:    
        embed = discord.Embed(title = f"{ctx.author} your pp width is...", description = (f"{random.randint(1, 10)} inches"), color = 0x5867f2)
    await ctx.response.send_message(embed = embed)
    print(f'command pp_width run in {ctx.guild}')
    f = open("cmdlogs.txt", "w+")
    f.write(f'{ctx.author}')
    f.write('\tpp width\n')
    f.close()

@client.slash_command()
async def rps(ctx, a):
        '''rock, paper, scissors'''
        a=a.lower()
        RPC=['rock','paper','scissors']
        b= RPC[random.randrange(0,2)]
        if a in RPC:
            if a==b:
                embed = discord.Embed(title = 'RPS results', description = f'{ctx.author.mention}: {a}\nMe: {b}', color = 0x808080)
                embed.set_footer (text = f'Loss!')
                await ctx.send (embed = embed)
            elif a=='rock' and b=='scissors':
                embed = discord.Embed(title = 'RPS results', description = f'{ctx.author.mention}: {a}\nMe: {b}', color = 0xFFDF00)
                await ctx.send (embed = embed)
            elif a=='scissors' and b=='rock':
                embed = discord.Embed(title = 'RPS results', description = f'{ctx.author.mention}: {a}\nMe: {b}')
                embed.set_footer (text = f'Loss!')
                await ctx.send (embed = embed)
            elif a=='paper' and b=='rock':
                embed = discord.Embed(title = 'RPS results', description = f'{ctx.author.mention}: {a}\nMe: {b}', color = 0xFFDF00)
                await ctx.send (embed = embed)
            elif a=='rock' and b=="paper":
                embed = discord.Embed(title = 'RPS results', description = f'{ctx.author.mention}: {a}\nMe: {b}')
                embed.set_footer (text = f'Loss!')
                await ctx.send (embed = embed)
            elif a=='scissors' and b=="paper":
                embed = discord.Embed(title = 'RPS results', description = f'{ctx.author.mention}: {a}\nMe: {b}', color = 0xFFDF00)
                await ctx.send (embed = embed)
            elif a=="paper" and b=="scissors":
                embed = discord.Embed(title = 'RPS results', description = f'{ctx.author.mention}: {a}\nMe: {b}')
                embed.set_footer (text = f'Loss!')
                await ctx.send (embed = embed)
            else:
                await ctx.send ("That's not a choice")
        f = open("cmdlogs.txt", "w+")
        f.write(f'{ctx.author}')
        f.write('\trps\n')
        f.close()

@client.command()
async def comedy(ctx):
    '''Some comedy pic'''
    author = ctx.author
    await author.send("https://cdn.discordapp.com/attachments/903454233037254666/904242252434505748/comedy.png")
    f = open("cmdlogs.txt", "w+")
    f.write(f'{ctx.author}')
    f.write('\tcomedy\n')
    f.close()

@client.slash_command()
async def ping(ctx):
    '''ping ...'''
    ping = int(round(client.latency, 3) * 1000)
    e=discord.Embed(title="ping", description=(f"Pong\n\nPing={ping}ms."))
    await ctx.response.send_message(embed=e)
    print(f'command ping run in {ctx.guild}')
    f = open("cmdlogs.txt", "w+")
    f.write(f'{ctx.author}')
    f.write('\tping\n')
    f.close()


@client.slash_command()
async def pp_size(ctx):
        '''Mesures ya dick and tells you the size'''
        msmt = ppsize.unit
        channel = client.get_channel(899378836968439878)
        size = random.randint(ppsize.mn, ppsize.mx)
        print(f'{ctx.author} got {size} in {ctx.guild} server')
        if size == 152:
            yes=random.randint(ppsize.mx, ppsize.rare)
            if yes == ppsize.rare:
                embed = discord.Embed(title = f"{ctx.author} your pp size is...", description = (f"{ppsize.rare} {msmt}, wait something ain't right here"), color = 0x5867f2)
                print(ctx.author, "GOT", ppsize.rare, msmt)
                await channel.send(f'ATTENTION @everyone, user <@{ctx.author.id}> got the RAREST dick size, {ppsize.rare}, {ppsize.rare} {msmt} is impossible but they still got it, congrats! ')
            else:
                embed = discord.Embed(title = f"{ctx.author} your pp size is...", description = (f"{ppsize.mx} inches"), color = 0x5867f2)
                
            
        else:
            embed = discord.Embed(title = f"{ctx.author} your pp size is...", description = (f"{size} {msmt}"), color = 0x5867f2)
        await ctx.response.send_message(embed = embed)
        f = open("ppsize.txt", "a")
        f.write(f'{ctx.author} =>\t\t')
        f.write(f'{size}\n')
        f.close()
        f = open("cmdlogs.txt", "w+")
        f.write(f'{ctx.author}')
        f.write('\tppsize\n')
        f.close()

@client.slash_command()
@commands.has_any_role('Lead dev')
async def pp_reset(ctx):
  '''Resets the pp_size command logs'''
  f = open("ppsize.txt", "w+")
  f.truncate()
  f.write('pp-size command logs:\n')
  f.close()
  await ctx.response.send_message('Logs Reset')
  f = open("cmdlogs.txt", "w+")
  f.write(f'{ctx.author} reset ppsize logs\n')
  f.close()

@client.slash_command()
@commands.has_any_role('Dev', 'Head Mod', 'Mod', 'pointsr3')
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
    f = open("cmdlogs.txt", "w+")
    f.write(f'{ctx.author}')
    f.write('\tbanned someone\n')
    f.close()

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
    f = open("cmdlogs.txt", "w+")
    f.write(f'{ctx.author}')
    f.write('\tkicked someone\n')
    f.close()

@client.command()
async def redacted(ctx):
    await ctx.author.send('https://cdn.discordapp.com/attachments/903454233037254666/906806501061046302/unknown.png')
    print(f'command [REDACTED] run in {ctx.guild}')
    f = open("cmdlogs.txt", "w+")
    f.write(f'{ctx.author}')
    f.write('\t[REDACTED]\n')
    f.close()

@client.command()
async def aaron(ctx):
    author = ctx.author
    await author.send('you owe me ∞ money UwU')
    await author.send('https://cdn.discordapp.com/attachments/903454233037254666/906049968312311848/Screenshot_20210928-230318_Discord.png')
    print(f'command aaron run in {ctx.guild}')
    f = open("cmdlogs.txt", "w+")
    f.write(f'{ctx.author}')
    f.write('\taaron\n')
    f.close()

@client.command()
async def luke(ctx):
    author = ctx.author
    await author.send('UwU you t-touchy my tail')
    await author.send('https://cdn.discordapp.com/attachments/903454233037254666/904242228803829770/luke.png')
    print(f'command luke run in {ctx.guild}')
    f = open("cmdlogs.txt", "w+")
    f.write(f'{ctx.author}')
    f.write('\tluwuke\n')
    f.close()

@client.command()
async def sniper(ctx):
    author = ctx.author
    await author.send('https://cdn.discordapp.com/attachments/903454233037254666/904242035110846504/sniper.jpg')
    print(f'command sniper run in {ctx.guild}')
    f = open("cmdlogs.txt", "w+")
    f.write(f'{ctx.author}')
    f.write('\tsnipy wipy uwu\n')
    f.close()

@client.command()
async def sneaky(ctx):
    author = ctx.author
    await author.send('https://cdn.discordapp.com/attachments/903454233037254666/904241982870810635/sneaky1.png')
    await author.send('https://cdn.discordapp.com/attachments/903454233037254666/904241944014753792/sneaky2.png')
    print(f'command sneaky run in {ctx.guild}')
    f = open("cmdlogs.txt", "w+")
    f.write(f'{ctx.author}')
    f.write('\tWALL\n')
    f.close()

@client.command()
async def december(ctx):
    author = ctx.author
    await author.send('https://cdn.discordapp.com/attachments/903454233037254666/903454303887433808/MirMfPscvzz9Gp1v9Ht2AsHvjZrPx903zOXAXltYiXlTGg4sq5k8KXsmqpyjPX34tbUOG5PT6GisBCtDRrU19YiNSUVAceCFK8hEAgEgneXNyJWAoFAIBC8CkKsBAKBQLDmEWIlEAgEgjWPECuBQCAQrHmEWAkEAoFgzSPESiAQCARrHiFWAoFAIFjzCLESCAQCwZpHiJVAIBAI1jxCrAQCgUCw5hFiJRAIBII1jxArgUAgEKx5hFgJBAKBYM0jxEogEAgEax4hVgKBQCBY8wixEggEAsEa5yjP4liNfAZxcP4AAAAAElFTkSuQmCC.png')
    await author.send('https://cdn.discordapp.com/attachments/903454233037254666/903454373043109928/IWSvBzO7ZAAAAABJRU5ErkJggg.png')
    await author.send('https://cdn.discordapp.com/attachments/903454233037254666/903454391498076170/BzGf2butOoxyAAAAAElFTkSuQmCC.png')
    await author.send('https://cdn.discordapp.com/attachments/903454233037254666/903454410900930570/x8XIKFENCaRlwAAAABJRU5ErkJggg.png')
    print(f'command dc run in {ctx.guild}')
    f = open("cmdlogs.txt", "w+")
    f.write(f'{ctx.author}')
    f.write('\tdecember will agressively pursuade your mother\n')
    f.close()

@client.slash_command()
async def bug_report(ctx):
    '''Depreciated, join our discord server'''
    await ctx.response.send_message('Depreciated, report bugs in our discord server, check my About Me to join it')

token = general.token
client.run(token)
