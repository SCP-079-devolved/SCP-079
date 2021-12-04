import os
# import dotenv

class config():
    f=False
    F=f
    t=True
    T=t

class general():
    MOTD = 'Now 100% More Slash Commands! | Febuary 2022'
    token=os.getenv("Token")
    bot_icon_emoji = "<:079:900247468845977610>"
    # Is the ban appealable? T or F
    ban_appealable=config.f # just change the f to t if it is configurable then go to the `if ban_appealable` if statement
    default_currency_name = "sweptbux" # set your own currency name in banksystem class using this format: "{NAME}"
    # Bot's prefix when not using slash commands
    prefix="."
    # only fill out of ban_appealable = T or t
    if ban_appealable:
        appeals_server="discord.gg/CODEHERE"
    elif ban_appealable == False:
        appeals_server="This is an unappealable ban"

class messages():
    #default reasons for the stuff listed below
    ban_message = f'You have been banned for breaking the rules.'
    kick_message = f'You have been kicked from the server.'

class banksystem():
    # name of the currency
    name = general.default_currency_name
    # Emoji embed code for the emoji
    icon = "<:Sweptbux:900246927847866428>"

class website():
    mdpass = os.getenv("mod_pass")
    dvpass = os.getenv("dev_pass")

class ppsize():
    mn = 1
    mx = 500
    rare = 501
    unit = "inches"
    logs = "ppsize.txt"
# LORE TIME: We had to use different classes for this to make importing easier and so it's easier to sort through stuff
