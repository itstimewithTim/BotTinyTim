# This is version TinyTim_2.1
import discord #Discord library
from discord.ext import commands
from discord.utils import get
import asyncio
import os #One of Python's standard libraries
import checks
from cog_events import ServerEvents #this one allows me to send welcomer DM to new members
from cog_bump_leaderboard import BumpLeaderboard #this one has all the code related to the Disboard bump leaderboard

# Create the client object
bot = commands.Bot(command_prefix='t?')

TOKEN = os.environ['DTOKEN'] #This will reference the DTOKEN that was defined in my .bashrc

# Terminate the bot when the command t?exit is run
@bot.command(name='exit')
@checks.DiMod()
async def exit(ctx):
    #s.close()
    await ctx.send('Goodbye, see you later!')
    quit()

#Add the cog_events.py Cog
bot.add_cog(ServerEvents(bot))

#Add the cog_bump_leaderboard.py Cog
bot.add_cog(BumpLeaderboard(bot))

# Begin running the bot
bot.run(TOKEN)