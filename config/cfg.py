import os

token=os.getenv("Token")
f=False
F=f
t=True
T=t

class general():
    # Is the ban appealable? T or F
    ban_appealable=f
    # Bot's prefix when not using slash commands
    prefix="/"
    # only fill out of ban_appealable = T or t
    if ban_appealable == t or T:
        appeals_server="discord.gg/CODEHERE"

class messages():
    ban_message = f'You have been banned from the server'
    kick_message = f'You have been kicked from the server'

#displaying what commands are public or private, use t and f reasons
class publiccommands():
    ban=f
    kick=f
    ping=t
    pp_size=t
    luke=f
