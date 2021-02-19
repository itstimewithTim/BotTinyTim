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

    @commands.command(name='rules')
    async def rules(self,ctx):
        embedrules = discord.Embed(
            title="These are the rules of our Discord Server:",
            colour=discord.Colour(0xfeffff),
            description="""<:timtime_1:722592663936827512> **Be excellent to one another**. The following is not permitted:
`(1)`    NSFW comments or images.
`(2)`    Obscene or Racial speech/images.
`(3)`    Unwanted spam via DM.
`(4)`    Unauthorized advertisement. 
`(5)`    Verbal abuse, insults, or threats towards others.
`(6)`    Repeatedly pinging the same person.
`(7)`    Advocating for or encouraging any of the above behavior.

<:timtime_2:722592655586099223> **Abide by** the [Terms of Service](https://discordapp.com/tos), the [Community Guidelines](https://discordapp.com/guidelines) and the [Partner Code of Conduct](https://support.discordapp.com/hc/en-us/articles/360024871991-Discord-Partnership-Code-of-Conduct).

<:timtime_3:722592647369195591> **Respect the Staff**. The staff will try to be fair and unbiased on every account.  If you feel the staff was unfair or biased, please post a screenshot of it at <#679850652117237780>. Those screenshots will be reviewed by Tim.

```By joining and remaining in this Discord Server, you agree to have read, understood, and agreed to abide by our server’s rules and the consequences of any offenses.```"""
            )
        embedrules.set_thumbnail(
            url="https://images-ext-2.discordapp.net/external/1kI2hwZ0JjdJ6OOErXGkJ3jDe_9H-EQUjdLz3t5lRvg/%3Fsize%3D1024/https/cdn.discordapp.com/icons/545008229160058910/64be58286d39f3db5d997b65172f5fd7.png"
            )
        embedrules.set_footer(
            text="Last Reviewed: 02/19/2021",
            icon_url="https://images-ext-2.discordapp.net/external/1kI2hwZ0JjdJ6OOErXGkJ3jDe_9H-EQUjdLz3t5lRvg/%3Fsize%3D1024/https/cdn.discordapp.com/icons/545008229160058910/64be58286d39f3db5d997b65172f5fd7.png"
            )

        await ctx.send(embed=embedrules)
    
    @commands.command(name='invite', aliases=['inv'])
    async def invite(self,ctx):
        await ctx.send('You can invite other people to our server using this invite link --> https://discord.gg/PJJ3jJJ')
    
    @commands.command(name='folder', aliases=['gdrive'])
    async def folder(self,ctx):
        await ctx.send('You can make your own TinyTim emoji, use this folder --> https://drive.google.com/drive/folders/1eVwJUdt29F1xVGy5kUsYVneFcBirtIqh?usp=sharing')
