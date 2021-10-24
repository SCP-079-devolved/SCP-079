import os

class config():
    f=False
    F=f
    t=True
    T=t

class general():
    token=os.getenv("Token")
    bot_icon_emoji = "<:079:900247468845977610>"
    # Is the ban appealable? T or F
    ban_appealable=config.f # just change the f to true if it is configurable then go to the `if ban_appealable` if statement
    default_currency_name = "sweptbux" # set your own currency name in banksystem class using this format: "{NAME}"
    # Bot's prefix when not using slash commands
    prefix="."
    # only fill out of ban_appealable = T or t
    if ban_appealable:
        appeals_server="discord.gg/CODEHERE"
    elif ban_appealable == False:
        appeals_server="This is an unappealable ban"

class messages():
    ban_message = f'You have been banned from the server'
    kick_message = f'You have been kicked from the server'

class banksystem():
    name = general.default_currency_name
    # Emoji embed code for the emoji
    icon = "<:Sweptbux:900246927847866428>"

