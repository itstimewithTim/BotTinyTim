import discord
from discord.ext import commands
import asyncio
import shelve
import checks
import re
import itertools

class BumpLeaderboard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.mentionpattern = re.compile('<@!?\d+>')
        self.bumpLb = shelve.open('bumpLb', writeback=True)
        try:
            self.bumpLb['score']
        except:
            self.bumpLb['score'] = {}
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == 302050872383242240: # As of 09/20/2020, Disboard's Bot ID is 302050872383242240
            if message.embeds and 'Bump done' in message.embeds[0].description:
                memberid = int(re.findall(self.mentionpattern, message.embeds[0].description)[0].lstrip('<@!').rstrip('>'))
                print(memberid)
                try:
                    self.bumpLb['score'][memberid] += 1
                except:
                    self.bumpLb['score'][memberid] = 1
                self.bumpLb.sync()
                await message.channel.send('Your successful bump has been recorded into my leaderboard')
                await asyncio.sleep(60*60*2)
                await message.channel.send('It has been 2 hours, so we can `!d bump` Disboard again! <:Blob_Knight:692763435951194163>')

    @commands.command(name='add')
    @checks.Janitor()
    async def add(self, ctx, person=None, amount=1):
        # User(with Moderator permission) adds <amount> to their own score or to the score of mentioned person.
        if person:
            matches = re.findall(self.mentionpattern, person)
            if matches:
                userid = int(matches[0].lstrip('<@!').rstrip('>'))
            else:
                await ctx.send('The syntax is `s?add @mention <AMOUNT>`')
                return
        else:
            userid = ctx.author.id
        try:
            self.bumpLb['score'][userid] += amount
        except:
            self.bumpLb['score'][userid] = 1
        self.bumpLb.sync()
        await ctx.send(f'Successfully added score by {amount}')

    @commands.command(name='subt')
    @checks.Janitor()
    async def subt(self, ctx, person=None, amount=1):
        # User(with Moderator permission) subtracts <amount> to their own score or to the score of mentioned person.
        if person:
            matches = re.findall(self.mentionpattern, person)
            if matches:
                userid = int(matches[0].lstrip('<@!').rstrip('>'))
            else:
                await ctx.send('The syntax is `s?subt @mention <AMOUNT>`')
                return
        else:
            userid = ctx.author.id
        try:
            self.bumpLb['score'][userid] += -1*amount
        except:
            self.bumpLb['score'][userid] = 1
        self.bumpLb.sync()
        await ctx.send(f'Successfully subtracted score by {amount}')

    @commands.command(name='leaderboard', aliases=['lb'])
    async def leaderboard(self, ctx, page=1):
        # Sort all userid:score pairs in the dictionary, produce a generator which will create (userid,score) sorted by score
        sortedlb = ((userid, self.bumpLb['score'][userid]) for userid in sorted(self.bumpLb['score'], key=self.bumpLb['score'].get, reverse=True))
        sortedlb = itertools.islice(sortedlb, 10*(page-1), 10*page)
        # Create the formatted list of users
        userlist = ""
        allmembers = ctx.guild.members
        for pos, (userid, score) in enumerate(sortedlb):
            try:
                user=await self.bot.fetch_user(userid)
            except:
                pass
            if user==None:
                print(userid, user)
                continue
            userlist += f"`{str(pos+1+(page-1)*10).zfill(2)}.`{user.mention} - **{score}** bumps\n"
        # Create the embed
        lbembed = discord.Embed(
            title=f"Bumping Leaderboard (Page {page})",description=userlist,color=discord.Color(16711680)
        )
        lbembed.set_footer(
            text="Hint: t?lb <PAGE>"
        )

        #Send the embed
        await ctx.send(embed=lbembed)