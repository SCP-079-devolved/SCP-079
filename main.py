# IMPORTS
import disnake, random
from disname.enums import ButtonStyle
from disnake.ext import commands
from config.cfg import general, messages, ppsize, website
import server
#       Nightly build 0.2.1

# starting server
server.start_server()
# making it so you can do `discord.` instead of `disnake.`
discord = disnake
# defining scp079
scp079=commands.Bot(command_prefix=commands.when_mentioned_or(general.prefix), descripion = "Luke did the dumb and yeeted the bot, now I'm here!", test_guilds=[899374265512624138], help_command=None, intents=discord.Intents.all(), case_insensitive=True)
# making @client. work alongside @scp079.
client = scp079
# multiplication (coming soon)
def multiply(x, y):
    return x * y

# on start event
@scp079.event
async def on_ready():
    print(client.user.name,"is online")
    await scp079.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=general.MOTD))
    f = open("cmdlogs.txt", "a")
    f.write('Bot started\n')
    f.close()

# 
  
#@client.slash_command()
#async def help(ctx):
#  e=disnake.Embed(title = f"{general.botname} Help")
#  e.set_footer(text = f'<:dani:930306330340753418> {general.botname}')

#class helpgui(disnake.ui.View):

#  def __init__(self):
#     super().__init__
#
#  @disnake.ui.button(label="Commands", style=ButtonStyle.blurple)
#  async def cmds(
#    self, button:disnake.ui.Button, ctx:disnake.MessageInteraction
#  ):
#    embed = disnake.Embed(title = f"{general.botname} Commands")
#    await ctx.response.send_message(embed=embed)

# Commands 
@client.slash_command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel : discord.TextChannel=None):
    '''Lock Command'''
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.response.send_message('Channel locked.')

@client.slash_command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel : discord.TextChannel=None):
    '''Unlock command'''
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.response.send_message('Channel unlocked.')

@client.slash_command()
async def pp_width(ctx):
    '''Your pp width....'''
    if ctx.author.id == 756147569880727627:
        embed = discord.Embed(title = f"{ctx.author} your pp width is...", description = (f"1 inch u noob"), color = 0x5867f2)
    else:    
        embed = discord.Embed(title = f"{ctx.author} your pp width is...", description = (f"{random.randint(1, 10)} inches"), color = 0x5867f2)
    await ctx.response.send_message(embed = embed)
    print(f'command pp_width run in {ctx.guild}')
    f = open("cmdlogs.txt", "a")
    f.write(f'{ctx.author}')
    f.write('\tMesured width of their dick\n')
    f.close()

#@client.command()
#async def slowmode(ctx, time: int, *, multiplier = None):
#    if not multiplier:
#        await ctx.channel.edit(slowmode_delay=time)
#    elif multiplier = m or M:
#        time=multiply(time, 60)
#        await ctx.channel.edit(slowmode_delay=time)
#    await ctx.channel.edit(slowmode_delay=time)
#    await ctx.send(f"Set the slowmode delay in this channel to {time} {multiplier}!")


@client.slash_command()
async def rps(ctx, option):
        '''rock, paper, scissors'''
        a=option.lower()
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
        f = open("cmdlogs.txt", "a")
        f.write(f'{ctx.author}')
        f.write('\trock paper scissors SHOOT\n')
        f.close()


@client.command()
async def comedy(ctx):
    '''Some comedy pic'''
    author = ctx.author
    await author.send("https://cdn.discordapp.com/attachments/903454233037254666/904242252434505748/comedy.png")
    f = open("cmdlogs.txt", "a")
    f.write(f'{ctx.author}')
    f.write('\tgot comedy gold\n')
    f.close()


@client.slash_command()
async def ping(ctx):
    '''ping ...'''
    ping = int(round(client.latency, 3) * 1000)
    e=discord.Embed(title="ping", description=(f"Pong\n\nPing={ping}ms."))
    await ctx.response.send_message(embed=e)
    print(f'command ping run in {ctx.guild}')
    f = open("cmdlogs.txt", "a")
    f.write(f'{ctx.author}')
    f.write('\tGot their ping\n')
    f.close()



@client.slash_command(aliases="pp-size")
async def pp_size(ctx):
        '''Mesures ya dick and tells you the size'''
        channel = client.get_channel(899378836968439878)
        size = random.randint(1, 500)
        print(f'{ctx.author} got {size} in {ctx.guild} server')
        if size == 152:
            yes=random.randint(ppsize.mx, ppsize.rare)
            if yes == ppsize.rare:
                embed = discord.Embed(title = f"{ctx.author} your pp size is...", description = ("501 inches, wait something ain't right here"), color = 0x5867f2)
                print(ctx.author, "GOT 501 inches!!")
                await ctx.response.send_message(embed = embed)
                await channel.send(f'ATTENTION @everyone, user <@{ctx.author.id}> got the RAREST dick size, 501 inches is impossible but they still got it, congrats! ')
                f = open("ppsize.scp079", "a")
                f.write(f'{ctx.author} =>\t\t')
                f.write('501!\n')
                f.close()
            else:
                embed = discord.Embed(title = f"{ctx.author} your pp size is...", description = ("500 inches"), color = 0x5867f2)
                await ctx.response.send_message(embed = embed)
                f = open("ppsize.scp079", "a")
                f.write(f'{ctx.author} =>\t\t')
                f.write(f'500\n')
                f.close()

        elif size == 335:
            rare=random.randint(1, 500)
            if rare == 470:
                embed = discord.Embed(title = f"{ctx.author} your pp size is...", description = ("hold up, wait a minute, we're having an error... your pp size is 502 somehow?"))
                await ctx.response.send_message(f"yo <@&910068859573256212> look at this...",embed = embed)
                print(ctx.author, "GOT 502 inches!!")
                f = open("ppsize.scp079", "a")
                f.write(f'{ctx.author} =>\t\t')
                f.write('502?\n')
                f.close()
            else:
                embed = discord.Embed(title = f"{ctx.author} your pp size is...", description = (f"{rare} inches"))
                await ctx.response.send_message(embed = embed)
                f = open("ppsize.scp079", "a")
                f.write(f'{ctx.author} =>\t\t')
                f.write(f'{size}\n')
                f.close()
        else:
            embed = discord.Embed(title = f"{ctx.author} your pp size is...", description = (f"{size} inches"), color = 0x5867f2)
            await ctx.response.send_message(embed = embed)
            f = open("ppsize.scp079", "a")
            f.write(f'{ctx.author} =>\t\t')
            f.write(f'{size}\n')
            f.close()

        f = open("cmdlogs.txt", "a")
        f.write(f'{ctx.author}')
        f.write('\tmesured their dick\n')
        f.close()


@client.slash_command()
@commands.has_any_role('Lead dev')
async def pp_reset(ctx):
    '''Resets the pp_size command logs'''
    f = open("ppsize.scp079", "w+")
    f.truncate()
    f.write('pp-size command logs:\n')
    f.close()
    await ctx.response.send_message('Logs Reset')
    f = open("cmdlogs.txt", "a")
    f.write(f'{ctx.author}')
    f.write('\treset ppsize logs\n')
    f.close()

@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clear(ctx, limit: int):
    await ctx.channel.purge(limit=limit)
    await ctx.send(f'last {limit} messages have been Cleared by{ctx.author.mention}')
    await ctx.message.delete()
    f = open("cmdlogs.txt", "a")
    f.write(f'{ctx.author}')
    f.write('\tpurged xd\n')
    f.close()
        
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You cant do that!")

@client.command()
@commands.has_any_role('Mod', 'Head Mod')
async def mpi(ctx):
  author = ctx.author
  await author.send(f"Hello {ctx.author}! \n as a Mod, here's your username and password:\n `username: Bot admin` \n `password: @079`\n \n Also if you forgot the url: https://control-panel.carnoval.repl.co \n\n DON'T SHARE THIS INFORAMTION WITH ANYONE \n `auto deleting message in 15 seconds...`", delete_after=15)
  await ctx.send("Message has been dmed to you, view it before it deletes itself...")
  
  f = open("user reports.txt", "a")
  f.write(f'{ctx.author} ran Website info as a Mod.\n')
  f.close()
  
@clear.error
async def mpi_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send("You cant do that!")
        f = open("user reports.txt", "a")
        f.write(f'{ctx.author} Tried to get website info by using Mod only secret command! Go get him.\n')
        f.close()

@client.slash_command()
async def site(ctx, level):
    if level == "dev":
        if ctx.author.id == 740981195159896184 or 309326655954878464 or 624494076846145536:
            author = ctx.author
            await author.send(f"Hello {ctx.author}! \n as a Developer of the bot, here's your username and password:\n `username: Bot dev` \n `password: bot dev 00`\n\n Also if you forgot the url: https://control-panel.carnoval.repl.co \n\n DON'T SHARE THIS INFORAMTION WITH ANYONE \n `auto deleting message in 15 seconds...`", delete_after=15)
            await ctx.response.send_message("Message has been dmed to you, view it before it deletes it self...",ephemeral=True)
  
            f = open("website info logs.txt", "a")
            f.write(f'{ctx.author} ran Website info as a Dev.\n')
            f.close()
        else:
            await ctx.author.send('ILLEGAL, expect a DM from a dev xd',ephemeral=True)
            f = open("user reports.txt", "a")
            f.write(f'{ctx.author} Tried to get website info by using Dev only secret command! Go get him.\n')
            f.close()
            pass
    elif level == "mod":
        modpass = website.mdpass
        if ctx.author.id == 728454308462460999 or 536640573113892874 or 568984677713444864:
            author = ctx.author
            await author.send(f"Hello {ctx.author}! \n as a Mod, here's your password: {modpass}\n  if you forgot the url: https://control-panel.carnoval.repl.co \n\n DON'T SHARE THIS INFORAMTION WITH ANYONE \n `auto deleting message in 15 seconds...`", delete_after=15)
            await ctx.response.send_message("Message has been dmed to you, view it before it deletes itself...")
  
            f = open("website info logs.txt", "a")
            f.write(f'{ctx.author} ran Website info as a Mod.\n')
            f.close()
        else:
            await ctx.author.send('ILLEGAL, expect a DM from a dev or mod xd')
            f = open("user reports.txt", "a")
            f.write(f'{ctx.author} Tried to get website info by using Mod only secret command! Go get him.\n')
            f.close()
            pass
    elif level == "topguys":
        if ctx.author.id == 441032877992574986 or 643867409802985503 or 601274881954414612:
            author = ctx.author
            await author.send('Damn, top guys, nice anyways the url is https://control-panel.carnoval.repl.co')

# ephemeral=True

@client.command()
@commands.has_any_role('Dev', 'Lead dev')
async def dpi(ctx):
  author = ctx.author
  await author.send(f"Hello {ctx.author}! \n as a Developer of the bot, here's your username and password:\n `username: Bot dev` \n `password: bot dev 00`\n\n Also if you forgot the url: https://control-panel.carnoval.repl.co \n\n DON'T SHARE THIS INFORAMTION WITH ANYONE \n `auto deleting message in 15 seconds...`", delete_after=15)
  await ctx.send("Message has been dmed to you, view it before it deletes it self...")
  
  f = open("website info logs.txt", "a")
  f.write(f'{ctx.author} ran Website info as a Dev.\n')
  f.close()
  
@clear.error
async def dpi_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send("You cant do that!")
        f = open("website info logs.txt", "a")
        f.write(f'{ctx.author} Tried to get website info by using Dev only secret command! Go get him.\n')
        f.close()

#this command isn't done...

# @client.command()
# @commands.has_any_role('Dev', 'Head Mod', 'Mod')
# async def memory(ctx, remembering, image_url):
#   #'''Remember someone, something, event, etc...'''
#   ctx.respoonse.send_message("Saved to server's memory... ppl will remember it")
#   channel = client.get_channel(923523947104981002)
#   await channel.send(f"*{author}*")

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
        await ctx.channel.send(f'{member} has been banned for `{reason}` by <@{authorid}> ')
    print(f'ban command run in {ctx.guild}')
    f = open("cmdlogs.txt", "a")
    f.write(f'{ctx.author}')
    f.write('\toooo they banned someone\n')
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
        await member.send(f'{author} has kicked you from {server} for `{reason}`. rejoin with this link {invitelink}')
        await ctx.response.send_message(f'Kicked {member} for you <@{authorid}>, they have recived another invite link but they have hopefully learned')
        await ctx.guild.kick(member, reason = reason)
    print(f'kick command run in {ctx.guild}')
    f = open("cmdlogs.txt", "a")
    f.write(f'{ctx.author}')
    f.write('\tkicked someone\n')
    f.close()


#fun commands idk,

@client.command()
async def redacted(ctx):
    await ctx.author.send('https://cdn.discordapp.com/attachments/903454233037254666/906806501061046302/unknown.png')
    f = open("cmdlogs.txt", "a")
    f.write(f'{ctx.author}')
    f.write('\t[REDACTED]\n')
    f.close()

@client.command()
async def aaron(ctx):
    author = ctx.author
    await author.send('you owe me ∞ money UwU')
    await author.send('https://cdn.discordapp.com/attachments/903454233037254666/906049968312311848/Screenshot_20210928-230318_Discord.png')
    f = open("cmdlogs.txt", "a")
    f.write(f'{ctx.author}')
    f.write('\taaron\n')
    f.close()

@client.command()
async def luke(ctx):
    author = ctx.author
    await author.send('UwU you t-touchy my tail')
    await author.send('https://cdn.discordapp.com/attachments/903454233037254666/904242228803829770/luke.png')
    await author.send('image 2 has been removed by request of the person who took the image')
    f = open("cmdlogs.txt", "a")
    f.write(f'{ctx.author}')
    f.write('\tluwuke\n')
    f.close()

@client.command()
async def sniper(ctx):
    author = ctx.author
    await author.send('https://cdn.discordapp.com/attachments/903454233037254666/904242035110846504/sniper.jpg')
    f = open("cmdlogs.txt", "a")
    f.write(f'{ctx.author}')
    f.write('\tsnipy wipy uwu\n')
    f.close()

@client.command(aliases=['Palisade'])
async def sneaky(ctx):
    author = ctx.author
    await author.send('https://cdn.discordapp.com/attachments/903454233037254666/904241982870810635/sneaky1.png')
    await author.send('https://cdn.discordapp.com/attachments/903454233037254666/904241944014753792/sneaky2.png')
    f = open("cmdlogs.txt", "a")
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
    f = open("cmdlogs.txt", "a")
    f.write(f'{ctx.author}')
    f.write('\tdecember will agressively pursuade your mother\n')
    f.close()

@client.command()
async def pointsr(ctx):
    author = ctx.author
    await author.send('https://i.imgur.com/Mpfov9C.png')
    await author.send('https://i.imgur.com/mcow06M.png')
    f = open("cmdlogs.txt", "a")
    f.write(f'{ctx.author}')
    f.write('\tPointsr is happy about that\n')
    f.close()

@client.command()
async def kelso(ctx):
    author = ctx.author
    await author.send('https://cdn.discordapp.com/attachments/903454233037254666/915046052233613332/unknown.png')
    f = open("cmdlogs.txt", "a")
    f.write(f'{ctx.author}')
    f.write('\tkelso funni joke mans\n')
    f.close()

@client.command()
async def cobra(ctx):
    author = ctx.author
    await author.send('https://cdn.discordapp.com/attachments/903454233037254666/915047792404222012/unknown.png')
    f = open("cmdlogs.txt", "a")
    f.write(f'{ctx.author}')
    f.write('\tcobra is sowwwy\n')
    f.close()

@client.command(aliases=["jessica","jessy"])
async def jess(ctx):
  author=ctx.author
  await author.send('---WARNING, the spoiler below is a link to an image with a pretty graphic topic, Vore, the act of eating someone/being eaten sexually, hence why it is in spoilers')
  await author.send('-noms you-')
  await author.send('-eats you-')
  await author.send('||https://cdn.discordapp.com/attachments/903454233037254666/930303339994943498/unknown.png||')
  await author.send('https://cdn.discordapp.com/attachments/903454233037254666/930303396005687376/unknown.png')
# unused commands
@client.slash_command()
async def bug_report(ctx):
    '''Depreciated, join our discord server'''
    await ctx.response.send_message('Depreciated, report bugs in our discord server, check my About Me to join it')




token = general.token
client.run(token)
