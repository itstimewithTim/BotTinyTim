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

As a new member, you only have read-only access to our Server's Channels until you agree to our Server Rules :)

I hope you enjoy your stay! <:tinytim_happy:683131385703432293>''')