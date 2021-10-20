import os

token=os.getenv("Token")
f=False
F=f
t=True
T=t
Default = "sweptbux"

class general():
    bot_icon_emoji = "<:079:900247468845977610>"
    # Is the ban appealable? T or F
    ban_appealable=f
    # Bot's prefix when not using slash commands
    prefix="."
    # only fill out of ban_appealable = T or t
    if ban_appealable:
        appeals_server="discord.gg/CODEHERE"

class messages():
    ban_message = f'You have been banned from the server'
    kick_message = f'You have been kicked from the server'

class banksystem():
    name = Default
    # Emoji embed code for the emoji
    icon = "<:Sweptbux:900246927847866428>"