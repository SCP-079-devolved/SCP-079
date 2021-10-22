import disnake, os, random, aiohttp, json
from disnake.ext import commands
from config.cfg import general, messages
from server import runserver

runserver()
sent_users = []
discord = disnake

scp079=commands.Bot(command_prefix=general.prefix, descripion = "Luke did the dumb and yeeted the bot, now I'm here!", test_guilds=[899374265512624138], help_command=None)
client = scp079

@scp079.event
async def on_ready():
    print(client.user.name,"is online")
    await scp079.change_presence(status=discord.Status.idle, activity = discord.Game(name = "Febuary 2022"))

@client.slash_command()
async def pp_width(ctx):
    embed = discord.Embed(title = f"{ctx.author} your pp width is...", description = (f"{random.randint(1, 10)} inches"), color = 0x5867f2)
    await ctx.response.send_message(embed = embed)

@client.slash_command()
async def comedy(ctx):
    await ctx.send(file=discord.File("images/comedy.png"))

@client.slash_command()
async def ping(ctx):
    ping = int(round(client.latency, 3) * 1000)
    e=discord.Embed(title="ping", description=(f"Pong\n\nPing={ping}ms."))
    await ctx.response.send_message(embed=e)

@client.slash_command()
async def pp_size(ctx):
    embed = discord.Embed(title = f"{ctx.author} your pp size is...", description = (f"{random.randint(1, 500)} inches"), color = 0x5867f2)
    await ctx.response.send_message(embed = embed)

@client.slash_command()
@commands.has_any_role('Dev', 'Head Mod', 'Mod')
async def ban(ctx, member: discord.Member,* ,reason = None):
      if reason == None:
           reason = messages.ban_message
      author = ctx.author
      authorid = ctx.author.id
      await member.send(f'You have been banned from {ctx.guild.name} for {reason} by {author}')
      await ctx.guild.ban(member, reason = reason)
      await ctx.channel.send(f'{member} has been banned for {reason} by <@{authorid}> ')

@client.slash_command()
@commands.has_any_role('Dev', 'Head Mod', 'Mod')
async def kick(ctx, member: discord.Member,* ,reason = None):
    if member == ctx.author:
        await ctx.response.send_message('no banning yourself noob')
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

class Confirm(disnake.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    # When the confirm button is pressed, set the inner value to `True` and
    # stop the View from listening to more input.
    # We also send the user an ephemeral message that we're confirming their choice.
    @disnake.ui.button(label='Shut down', style=disnake.ButtonStyle.red)
    async def confirm(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await interaction.response.send_message('Pls do secret command or type `.cancel`')
        @client.command()
        async def shut(ctx, *, reason):
          await ctx.send("Shutting down...")
          print(f'{client.user} has shutted down by {ctx.author} because {reason}')
          exit()
        
        @client.command()
        async def cancel(ctx):
          await ctx.send("Shut down process canceled.")
          return
        self.value = True
        self.stop()

    # This one is similar to the confirmation button except sets the inner value to `False`
    @disnake.ui.button(label='Cancel', style=disnake.ButtonStyle.green)
    async def cancel(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await interaction.response.send_message('Cancelling')
        self.value = False
        self.stop()

# @client.slash_command()
# @client.command()
# async def shutdown(ctx: commands.Context):
#    #"""Shuts the bot down (use this only on critical times)"""
   # We create the view and assign it to a variable so we can wait for it later.
#    view = Confirm()
#    await ctx.send('You want to shut me down? really?', view=view)
   # Wait for the View to stop listening for input...
#    await view.wait()
#    if view.value is None:
#        print('hm')
#    elif view.value:
#        print('Shut down happened')
#    else:
#        print('Shut down canceled')

@client.slash_command()
async def bug_report(ctx, title, *, description):
  '''Use this to report a bug! '''
  print(f'A bug report from {ctx.author}:\n Title:\n {title} \n Description: \n {description}\n ')
  await ctx.response.send_message(f'Bug has been reported! Thanks 😉')

token = (os.getenv('Token'))
client.run(token)