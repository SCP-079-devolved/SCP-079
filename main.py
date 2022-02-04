import aiohttp
import aiofiles
import json
from server import start_server

from disnake.types import embed
from disnake.utils import get
from disnake.enums import ButtonStyle
from disnake.ext import commands
from config.cfg import general, messages, ppsize, website

#       Nightly build 0.2.3

# Start the server
start_server()
# making it so you can do `discord.` instead of `disnake.`
discord = disnake
# defining scp079
scp079 = commands.Bot(
    command_prefix=commands.when_mentioned_or(general.prefix),
    descripion="Luke did the dumb and yeeted the bot, now I'm here!",
    test_guilds=[899374265512624138, 933250800816377856], help_command=None, intents=discord.Intents.all(),
    case_insensitive=True
)
# making @client. work alongside @scp079.
client = scp079
bot = scp079
bot.warnings = {}  # guild_id : {member_id: [count, [(admin_id, reason)]]}
testing = scp079


# on start event
@scp079.event
async def on_ready():
    print(client.user.name, "is online")
    await scp079.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=general.MOTD))
    f = open("cmdlogs.txt", "a")
    f.write('Bot started\n')
    f.close()
    for guild in bot.guilds:
        bot.warnings[guild.id] = {}

        async with aiofiles.open(f"{guild.id}.txt", mode="a") as temp:
            pass

        async with aiofiles.open(f"{guild.id}.txt", mode="r") as file:
            lines = await file.readlines()

            for line in lines:
                data = line.split(" ")
                member_id = int(data[0])
                admin_id = int(data[1])
                reason = " ".join(data[2:]).strip("\n")

                try:
                    bot.warnings[guild.id][member_id][0] += 1
                    bot.warnings[guild.id][member_id][1].append((admin_id, reason))

                except KeyError:
                    bot.warnings[guild.id][member_id] = [1, [(admin_id, reason)]]


@testing.command()
async def apraxed(ctx):
    # I feel so dirty making this command
    author = ctx.author
    await author.send('https://cdn.discordapp.com/attachments/903454233037254666/937583373214441482/unknown.png')
    f = open("cmdlogs.txt", "a")
    f.write(f'{author}')
    f.write('\tApraxy Waxy UwU\n')
    f.close()


@testing.command()
async def carnoval(ctx):
    author = ctx.author
    await author.send("https://cdn.discordapp.com/attachments/903454233037254666/937582799165202483/unknown.png")
    f = open("cmdlogs.txt", "a")
    f.write(f'{author}')
    f.write('\tCarnoval UwU\n')
    f.close()


#@testing.command()
#async def ken(ctx):
#    author = ctx.author
#    await author.send("https://cdn.discordapp.com/attachments/767434336206979072/932866699391283200/unknown.png")
#    f = open("cmdlogs.txt", "a")
#    f.write(f'{author}')
#   f.write('\tKenny will slap your ass cheaks into your rectum\n')
#    f.close()


@testing.slash_command(pass_context=True, aliases=['yeettomuteland'], description="Mutes a specified user")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: disnake.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(
                mutedRole,
                view_channels=True,
                speak=False,
                send_messages=False,
                read_message_history=True,
                read_messages=True
            )
    embd = disnake.Embed(
        title=f"Muted {member} for `{reason}`",
        description=f"{member.mention} was muted by {ctx.author.mention} for {reason}",
        color=0xFF0000
    )
    await member.add_roles(mutedRole, reason=f"reason")
    await ctx.response.send_message(embed=embd)
    await member.send(f"You were muted in the server {guild.name} for {reason}")
    f = open("cmdlogs.txt", "a")
    f.write(f'{ctx.author}')
    f.write("\tMuted someone\n")
    f.close()

@testing.slash_command(description="Unmutes a specified user.")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: disnake.Member):
    mutedRole = get(ctx.guild.roles, name="Muted")

    embd = disnake.Embed(
        title=f"{member} was unmuted",
        description=f"{member.mention} was unmuted by {ctx.author.mention}",
        color=0x00FF00
    )
    await member.remove_roles(mutedRole)
    await ctx.response.send_message(embed=embd)
    f = open("cmdlogs.txt", "a")
    f.write(f'{ctx.author}')
    f.write("\tUnmuted someone\n")
    f.close()

@scp079.command()
@commands.has_permissions(administrator=True)
async def warn(ctx, member: disnake.Member = None, *, reason=None):
    if member is None:
        return await ctx.send("The provided member could not be found or you forgot to provide one.")

    if reason is None:
        return await ctx.send("Please provide a reason for warning this user.")

    try:
        first_warning = False
        scp079.warnings[ctx.guild.id][member.id][0] += 1
        scp079.warnings[ctx.guild.id][member.id][1].append((ctx.author.id, reason))

    except KeyError:
        first_warning = True
        scp079.warnings[ctx.guild.id][member.id] = [1, [(ctx.author.id, reason)]]

    count = scp079.warnings[ctx.guild.id][member.id][0]

    async with aiofiles.open(f"{ctx.guild.id}.txt", mode="a") as file:
        await file.write(f"{member.id} {ctx.author.id} {reason}\n")

    await ctx.send(f"{member.mention} has {count} {'warning' if first_warning else 'warnings'}.")
    f = open("cmdlogs.txt", "a")
    f.write(f'{ctx.author}')
    f.write("\tWarned someone\n")
    f.close()

@scp079.event
async def on_member_join(self, member):
    guild = member.guild
    channel = "931055646122598453"

    to_send = f"Welcome {member.mention} to {guild.name}!"
    await channel.send(to_send)

@scp079.command()
@commands.has_permissions(administrator=True)
async def warnings(ctx, member: disnake.Member = None):
    if member is None:
        return await ctx.send("The provided member could not be found or you forgot to provide one.")

    embed = discord.Embed(title=f"Displaying Warnings for {member.name}", description="", colour=discord.Colour.red())
    try:
        i = 1
        for admin_id, reason in bot.warnings[ctx.guild.id][member.id][1]:
            admin = ctx.guild.get_member(admin_id)
            embed.description += f"**Warning {i}** given by: {admin.mention} for: *'{reason}'*.\n"
            i += 1
        if i >= 10:
            embed.add_field(name="WARNING", value="This user has more than 10 warnings", inline=False)
            embed.set_image(url="https://imgur.com/6ClVr5r")
        await ctx.send(embed=embed)

    except KeyError:  # no warnings
        await ctx.send("This user has no warnings.")
    f = open("cmdlogs.txt", "a")
    f.write(f'{ctx.author}')
    f.write("\tChecked someone's warnings\n")
    f.close()

@scp079.slash_command()
async def help(ctx):
    e = disnake.Embed(title=f"Scp-079 Help")
    e.set_footer(text=f'SCP-079 Premium')
    await ctx.response.send_message(embed=e, view=helpgui())


@testing.slash_command()
async def images(ctx):
    e = disnake.Embed(
        title="Test Embed Title",
        description="These are the built-in image commads included with SCP-079",
        color=0x5865fe
    )
    await ctx.response.send_message(embed=e, view=image())
    f = open("cmdlogs.txt", "a")
    f.write(f'{ctx.author}')
    f.write("\tRan the DM image command\n")
    f.close()

class image(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=15)

    @disnake.ui.button(label="Apraxed", style=ButtonStyle.gray)
    async def apraxed(
            self, button: disnake.ui.Button, ctx: disnake.MessageInteraction
    ):
        await ctx.response.send_message('Check your DMS', ephemeral=True)
        author = ctx.author
        await author.send('https://cdn.discordapp.com/attachments/903454233037254666/937583373214441482/unknown.png')
        f = open("cmdlogs.txt", "a")
        f.write(f'{author}')
        f.write('\tApraxy Waxy UwU\n')
        f.close()

    @disnake.ui.button(label="carnoval", style=ButtonStyle.gray)
    async def carnoval(
            self, button: disnake.ui.Button, ctx: disnake.MessageInteraction
    ):
        author = ctx.author
        await ctx.response.send_message('Check your DMS', ephemeral=True)
        await author.send("https://cdn.discordapp.com/attachments/903454233037254666/937582799165202483/unknown.png")
        f = open("cmdlogs.txt", "a")
        f.write(f'{author}')
        f.write('\tCarnoval UwU\n')
        f.close()

    @disnake.ui.button(label="ken", style=ButtonStyle.gray)
    async def ken(
            self, button: disnake.ui.Button, ctx: disnake.MessageInteraction
    ):
        author = ctx.author
        await ctx.response.send_message('Check your DMS', ephemeral=True)
        await author.send("https://cdn.discordapp.com/attachments/767434336206979072/932866699391283200/unknown.png")
        f = open("cmdlogs.txt", "a")
        f.write(f'{author}')
        f.write('\tKenny will slap your ass cheaks into your rectum\n')
        f.close()

    @disnake.ui.button(label="redacted", style=ButtonStyle.gray)
    async def redacted(
            self, button: disnake.ui.Button, ctx: disnake.MessageInteraction
    ):
        await ctx.response.send_message('Check your DMS', ephemeral=True)
        await ctx.author.send(
            'https://cdn.discordapp.com/attachments/903454233037254666/906806501061046302/unknown.png')
        f = open("cmdlogs.txt", "a")
        f.write(f'{ctx.author}')
        f.write('\t[REDACTED]\n')
        f.close()

    @disnake.ui.button(label="aaron", style=ButtonStyle.gray)
    async def aaron(
            self, button: disnake.ui.Button, ctx: disnake.MessageInteraction
    ):
        author = ctx.author
        await ctx.response.send_message('Check your DMS', ephemeral=True)
        await author.send('you owe me ∞ money UwU')
        await author.send(
            'https://cdn.discordapp.com/attachments/903454233037254666/906049968312311848/Screenshot_20210928-230318_Discord.png')
        f = open("cmdlogs.txt", "a")
        f.write(f'{ctx.author}')
        f.write('\taaron\n')
        f.close()

    @disnake.ui.button(label="luke", style=ButtonStyle.gray)
    async def luke(
            self, button: disnake.ui.Button, ctx: disnake.MessageInteraction
    ):
        author = ctx.author
        await ctx.response.send_message('Check your DMS', ephemeral=True)
        await author.send('UwU you t-touchy my tail')
        await author.send('https://cdn.discordapp.com/attachments/903454233037254666/904242228803829770/luke.png')
        f = open("cmdlogs.txt", "a")
        f.write(f'{ctx.author}')
        f.write('\tluwuke\n')
        f.close()

    @disnake.ui.button(label="sniper", style=ButtonStyle.gray)
    async def sniper(
            self, button: disnake.ui.Button, ctx: disnake.MessageInteraction
    ):
        await ctx.response.send_message('Check your DMS', ephemeral=True)
        author = ctx.author
        await author.send('https://cdn.discordapp.com/attachments/903454233037254666/904242035110846504/sniper.jpg')
        f = open("cmdlogs.txt", "a")
        f.write(f'{ctx.author}')
        f.write('\tsnipy wipy uwu\n')
        f.close()

    @disnake.ui.button(label="sneaky", style=ButtonStyle.gray)
    async def sneaky(
            self, button: disnake.ui.Button, ctx: disnake.MessageInteraction
    ):
        await ctx.response.send_message('Check your DMS', ephemeral=True)
        author = ctx.author
        await author.send('https://cdn.discordapp.com/attachments/903454233037254666/904241982870810635/sneaky1.png')
        await author.send('https://cdn.discordapp.com/attachments/903454233037254666/904241944014753792/sneaky2.png')
        f = open("cmdlogs.txt", "a")
        f.write(f'{ctx.author}')
        f.write('\tWALL\n')
        f.close()

    @disnake.ui.button(label="december", style=ButtonStyle.gray)
    async def december(
            self, button: disnake.ui.Button, ctx: disnake.MessageInteraction
    ):
        await ctx.response.send_message('Check your DMS', ephemeral=True)
        author = ctx.author
        await author.send(
            'https://cdn.discordapp.com/attachments/903454233037254666/903454303887433808/MirMfPscvzz9Gp1v9Ht2AsHvjZrPx903zOXAXltYiXlTGg4sq5k8KXsmqpyjPX34tbUOG5PT6GisBCtDRrU19YiNSUVAceCFK8hEAgEgneXNyJWAoFAIBC8CkKsBAKBQLDmEWIlEAgEgjWPECuBQCAQrHmEWAkEAoFgzSPESiAQCARrHiFWAoFAIFjzCLESCAQCwZpHiJVAIBAI1jxCrAQCgUCw5hFiJRAIBII1jxArgUAgEKx5hFgJBAKBYM0jxEogEAgEax4hVgKBQCBY8wixEggEAsEa5yjP4liNfAZxcP4AAAAAElFTkSuQmCC.png' \
            )
        await author.send(
            'https://cdn.discordapp.com/attachments/903454233037254666/903454373043109928/IWSvBzO7ZAAAAABJRU5ErkJggg.png'
        )
        await author.send(
            'https://cdn.discordapp.com/attachments/903454233037254666/903454391498076170/BzGf2butOoxyAAAAAElFTkSuQmCC.png'
        )
        await author.send(
            'https://cdn.discordapp.com/attachments/903454233037254666/903454410900930570/x8XIKFENCaRlwAAAABJRU5ErkJggg.png'
        )
        f = open("cmdlogs.txt", "a")
        f.write(f'{ctx.author}')
        f.write('\tdecember will agressively pursuade your mother\n')
        f.close()

    @disnake.ui.button(label="pointsr", style=ButtonStyle.gray)
    async def pointsr(
            self, button: disnake.ui.Button, ctx: disnake.MessageInteraction
    ):
        await ctx.response.send_message('Check your DMS', ephemeral=True)
        author = ctx.author
        await author.send('https://i.imgur.com/Mpfov9C.png')
        await author.send('https://i.imgur.com/mcow06M.png')
        await author.send('https://cdn.discordapp.com/attachments/903454233037254666/937588771937984553/unknown.png')
        f = open("cmdlogs.txt", "a")
        f.write(f'{ctx.author}')
        f.write('\tPointsr is happy about that\n')
        f.close()

    @disnake.ui.button(label="kelso", style=ButtonStyle.gray)
    async def kelso(
            self, button: disnake.ui.Button, ctx: disnake.MessageInteraction
    ):
        await ctx.response.send_message('Check your DMS', ephemeral=True)
        author = ctx.author
        await author.send('https://cdn.discordapp.com/attachments/903454233037254666/915046052233613332/unknown.png')
        f = open("cmdlogs.txt", "a")
        f.write(f'{ctx.author}')
        f.write('\tkelso funni joke mans\n')
        f.close()

    @disnake.ui.button(label="cobra", style=ButtonStyle.gray)
    async def cobra(
            self, button: disnake.ui.Button, ctx: disnake.MessageInteraction
    ):
        await ctx.response.send_message('Check your DMS', ephemeral=True)
        author = ctx.author
        await author.send('https://cdn.discordapp.com/attachments/903454233037254666/915047792404222012/unknown.png')
        f = open("cmdlogs.txt", "a")
        f.write(f'{ctx.author}')
        f.write('\tcobra is sowwwy\n')
        f.close()

class helpgui(disnake.ui.View):

    def __init__(self):
        super().__init__(timeout=15)

    @disnake.ui.button(label="Invite", style=ButtonStyle.red)
    async def invite_link(
            self, button: disnake.ui.Button, ctx: disnake.MessageInteraction
    ):
        await ctx.response.send_message("The bot doesn't have an invite link at this current time, sorry",
                                        ephemeral=True)

    @disnake.ui.button(label="Commands", style=ButtonStyle.blurple)
    async def cmds(
            self, button: disnake.ui.Button, ctx: disnake.MessageInteraction
    ):
        embed = disnake.Embed(title=f"SCP-079 Commands")
        embed.add_field(name="Mod Commands", value="/ban\n/kick\n/clear\n/pp_reset\n/warn\n/warns\n/mute\n/unmute",
                        inline=True)
        embed.add_field(name="Fun Commands", value="/pp_size\n/rps\n/pp_width\n/meme", inline=True)
        embed.add_field(name="Image Commands",
                        value=
                        ".apraxed\n.carnoval\n.cobra\n.kelso\n.luke\n.redacted\n.dc\n.aaron\n.sneaky\n.sniper\n.pointsr",
                        inline=True)
        await ctx.response.send_message(embed=embed)


@scp079.slash_command(pass_context=True)
async def meme(ctx):
    embed = disnake.Embed(title="meme", description="trolling intensifies")
    async with aiohttp.ClientSession() as cs:
        sub = random.randint(1, 2)
        if sub == 1:
            async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
                res = await r.json()
                embed.set_image(res['data']['children'][random.randint(0, 25)]['data']['url'])
                await ctx.response.send_message(embed=embed)
        if sub == 2:
            async with cs.get('https://www.reddit.com/r/memes/new.json?sort=hot') as r:
                res = await r.json()
                embed.set_image(res['data']['children'][random.randint(0, 25)]['data']['url'])
                await ctx.response.send_message(embed=embed)


# multiplication (coming soon)
def multiply(x, y):
    return x * y


# @client.slash_command()
# async def help(ctx):
#  e=disnake.Embed(title = f"{general.botname} Help")
#  e.set_footer(text = f'<:dani:930306330340753418> {general.botname}')

# class helpgui(disnake.ui.View):

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
async def lock(ctx, channel: disnake.TextChannel = None):
    '''Lock Command'''
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.response.send_message('Channel locked.')


@client.slash_command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel: disnake.TextChannel = None):
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
        embed = disnake.Embed(title=f"{ctx.author} your pp width is...", description="1 inch u noob", color=0x5867f2)
    else:
        embed = disnake.Embed(title=f"{ctx.author} your pp width is...",
                              description=f"{random.randint(1, 10)} inches", color=0x5867f2)
    await ctx.response.send_message(embed=embed)
    print(f'command pp_width run in {ctx.guild}')
    f = open("cmdlogs.txt", "a")
    f.write(f'{ctx.author}')
    f.write('\tMesured width of their dick\n')
    f.close()


# @client.command()
# async def slowmode(ctx, time: int, *, multiplier = None):
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
    a = option.lower()
    RPC = ['rock', 'paper', 'scissors']
    b = RPC[random.randrange(0, 2)]
    if a in RPC:
        if a == b:
            embed = discord.Embed(title='RPS results', description=f'{ctx.author.mention}: {a}\nMe: {b}',
                                  color=0x808080)
            embed.set_footer(text=f'Loss!')
            await ctx.send(embed=embed)
        elif a == 'rock' and b == 'scissors':
            embed = discord.Embed(title='RPS results', description=f'{ctx.author.mention}: {a}\nMe: {b}',
                                  color=0xFFDF00)
            await ctx.send(embed=embed)
        elif a == 'scissors' and b == 'rock':
            embed = discord.Embed(title='RPS results', description=f'{ctx.author.mention}: {a}\nMe: {b}')
            embed.set_footer(text=f'Loss!')
            await ctx.send(embed=embed)
        elif a == 'paper' and b == 'rock':
            embed = discord.Embed(title='RPS results', description=f'{ctx.author.mention}: {a}\nMe: {b}',
                                  color=0xFFDF00)
            await ctx.send(embed=embed)
        elif a == 'rock' and b == "paper":
            embed = discord.Embed(title='RPS results', description=f'{ctx.author.mention}: {a}\nMe: {b}')
            embed.set_footer(text=f'Loss!')
            await ctx.send(embed=embed)
        elif a == 'scissors' and b == "paper":
            embed = discord.Embed(title='RPS results', description=f'{ctx.author.mention}: {a}\nMe: {b}',
                                  color=0xFFDF00)
            await ctx.send(embed=embed)
        elif a == "paper" and b == "scissors":
            embed = discord.Embed(title='RPS results', description=f'{ctx.author.mention}: {a}\nMe: {b}')
            embed.set_footer(text=f'Loss!')
            await ctx.send(embed=embed)

        else:
            await ctx.send("That's not a choice")
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
    e = discord.Embed(title="ping", description=(f"Pong\n\nPing={ping}ms."))
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
        yes = random.randint(ppsize.mx, ppsize.rare)
        if yes == ppsize.rare:
            embed = discord.Embed(title=f"{ctx.author} your pp size is...",
                                  description=("501 inches, wait something ain't right here"), color=0x5867f2)
            print(ctx.author, "GOT 501 inches!!")
            await ctx.response.send_message(embed=embed)
            await channel.send(
                f'ATTENTION @everyone, user <@{ctx.author.id}> got the RAREST dick size, '
                f'501 inches is impossible but they still got it, congrats! ')
            f = open("ppsize.scp079", "a")
            f.write(f'{ctx.author} =>\t\t')
            f.write('501!\n')
            f.close()
        else:
            embed = discord.Embed(title=f"{ctx.author} your pp size is...", description=("500 inches"), color=0x5867f2)
            await ctx.response.send_message(embed=embed)
            f = open("ppsize.scp079", "a")
            f.write(f'{ctx.author} =>\t\t')
            f.write(f'500\n')
            f.close()

    elif size == 335:
        rare = random.randint(1, 500)
        if rare == 470:
            embed = discord.Embed(title=f"{ctx.author} your pp size is...", description=(
                "hold up, wait a minute, we're having an error... your pp size is 502 somehow?"))
            await ctx.response.send_message(f"yo <@&910068859573256212> look at this...", embed=embed)
            print(ctx.author, "GOT 502 inches!!")
            f = open("ppsize.scp079", "a")
            f.write(f'{ctx.author} =>\t\t')
            f.write('502?\n')
            f.close()
        else:
            embed = discord.Embed(title=f"{ctx.author} your pp size is...", description=(f"{rare} inches"))
            await ctx.response.send_message(embed=embed)
            f = open("ppsize.scp079", "a")
            f.write(f'{ctx.author} =>\t\t')
            f.write(f'{size}\n')
            f.close()
    else:
        embed = discord.Embed(title=f"{ctx.author} your pp size is...", description=(f"{size} inches"), color=0x5867f2)
        await ctx.response.send_message(embed=embed)
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
    await author.send(
        f"Hello {ctx.author}! \n as a Mod, here's your username and password:\n `username: Bot admin` \n `password: @079`\n \n Also if you forgot the url: https://control-panel.carnoval.repl.co \n\n DON'T SHARE THIS INFORAMTION WITH ANYONE \n `auto deleting message in 15 seconds...`",
        delete_after=15)
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


#@client.slash_command()
#async def site(ctx, level):
#    if level == "dev":
#        if ctx.author.id == 740981195159896184 or 309326655954878464 or 624494076846145536:
#            author = ctx.author
#            await author.send(
#                f"Hello {ctx.author}! \n as a Developer of the bot, here's your username and password:\n `username: Bot dev` \n `password: bot dev 00`\n\n Also if you forgot the url: https://control-panel.carnoval.repl.co \n\n DON'T SHARE THIS INFORAMTION WITH ANYONE \n `auto deleting message in 15 seconds...`",
#                delete_after=15)
#            await ctx.response.send_message("Message has been dmed to you, view it before it deletes it self...",
#                                            ephemeral=True)
#
#            f = open("website info logs.txt", "a")
#            f.write(f'{ctx.author} ran Website info as a Dev.\n')
#            f.close()
#        else:
#            await ctx.author.send('ILLEGAL, expect a DM from a dev xd', ephemeral=True)
#            f = open("user reports.txt", "a")
#            f.write(f'{ctx.author} Tried to get website info by using Dev only secret command! Go get him.\n')
#            f.close()
#            pass
#    elif level == "mod":
#        modpass = website.mdpass
#        if ctx.author.id == 728454308462460999 or 536640573113892874 or 568984677713444864:
 #           author = ctx.author
 #           await author.send(
 #               f"Hello {ctx.author}! \n as a Mod, here's your password: {modpass}\n  if you forgot the url: https://control-panel.carnoval.repl.co \n\n DON'T SHARE THIS INFORAMTION WITH ANYONE \n `auto deleting message in 15 seconds...`",
 #               delete_after=15)
 #           await ctx.response.send_message("Message has been dmed to you, view it before it deletes itself...")

#            f = open("website info logs.txt", "a")
#            f.write(f'{ctx.author} ran Website info as a Mod.\n')
#            f.close()
#        else:
#            await ctx.author.send('ILLEGAL, expect a DM from a dev or mod xd')
#            f = open("user reports.txt", "a")
#            f.write(f'{ctx.author} Tried to get website info by using Mod only secret command! Go get him.\n')
#            f.close()
#            pass
 #   elif level == "topguys":
 #       if ctx.author.id == 441032877992574986 or 643867409802985503 or 601274881954414612:
 #           author = ctx.author
 #           await author.send('Damn, top guys, nice anyways the url is https://control-panel.carnoval.repl.co')

# this command isn't done...



@client.slash_command()
@commands.has_any_role('Dev', 'Head Mod', 'Mod', 'pointsr3')
async def ban(ctx, member: discord.Member, *, reason=None):
    '''To Ban anyone you want in the server! (MOD command)'''
    if member == ctx.author:
        ctx.respoonse.send_message('no banning yourself')
    else:
        if reason == None:
            reason = messages.ban_message
        author = ctx.author
        authorid = ctx.author.id
        await member.send(f'You have been banned from {ctx.guild.name} for {reason} by {author}')
        await ctx.guild.ban(member, reason=reason)
        await ctx.channel.send(f'{member} has been banned for `{reason}` by <@{authorid}> ')
    print(f'ban command run in {ctx.guild}')
    f = open("cmdlogs.txt", "a")
    f.write(f'{ctx.author}')
    f.write('\toooo they banned someone\n')
    f.close()


@client.slash_command()
@commands.has_any_role('Dev', 'Head Mod', 'Mod')
async def kick(ctx, member: discord.Member, *, reason=None):
    '''To Kick anyone you want in the server! (MOD command)'''
    if member == ctx.author:
        await ctx.response.send_message('no kicking yourself noob')
        pass
    else:
        if reason == None:
            reason = messages.kick_message
        author = ctx.author
        authorid = ctx.author.id
        invitelink = await ctx.channel.create_invite(max_uses=1, unique=True)
        server = ctx.guild
        await member.send(f'{author} has kicked you from {server} for `{reason}`. rejoin with this link {invitelink}')
        await ctx.response.send_message(
            f'Kicked {member} for you <@{authorid}>, they have recived another invite link but they have hopefully learned')
        await ctx.guild.kick(member, reason=reason)
    print(f'kick command run in {ctx.guild}')
    f = open("cmdlogs.txt", "a")
    f.write(f'{ctx.author}')
    f.write('\tkicked someone\n')
    f.close()

# unused commands
@client.slash_command()
async def bug_report(ctx):
    '''Depreciated, join our discord server'''
    await ctx.response.send_message('Depreciated, report bugs in our discord server, check my About Me to join it')


token = general.token
client.run(token)
