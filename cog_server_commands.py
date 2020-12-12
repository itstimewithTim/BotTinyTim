import discord
from discord.ext import commands
import asyncio
import checks

class ServerCommands(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name='hello', aliases=['greeting'])
    async def hello(self,ctx):
        await ctx.send('Hello there, Tim here!')
    
    @commands.command(name='invite', aliases=['inv'])
    async def invite(self,ctx):
        await ctx.send('You can invite other people to our server using this invite link --> https://discord.gg/PJJ3jJJ')
    
    @commands.command(name='folder', aliases=['gdrive'])
    async def folder(self,ctx):
        await ctx.send('You can make your own TinyTim emoji, use this folder --> https://drive.google.com/drive/folders/1eVwJUdt29F1xVGy5kUsYVneFcBirtIqh?usp=sharing')
