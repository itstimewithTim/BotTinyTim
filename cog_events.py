import discord
from discord.ext import commands
import asyncio
import checks

class ServerEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # Print all guilds which the bot has connected to
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Connected to the following guilds: {', '.join([guild.name for guild in self.bot.guilds])}")

    # Sends welcomer DM to new members
    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.send('''Hello! Welcome to our Discord Server!

As a new member, you have read-only access to a few channels to give you a taste of what our server is like.

In order to see the rest of the channels and to send messages, you first have to accept our rules. To do so, please visit <#550398466187067423> and react with the "T" <:tinytim_happy:683131385703432293>''')