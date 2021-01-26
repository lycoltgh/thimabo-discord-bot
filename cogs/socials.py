import discord
from discord.ext import commands
import random
from discord import Color as c

teal = c.teal()
magenta = c.magenta()

class Socials(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def socials(self, ctx):
        scl = discord.Embed(
            color=magenta
        )
        scl.set_author(name='A collection of active socials, cough.', icon_url='https://cdn.discordapp.com/attachments/787019308260917289/800843165669130240/logo1.png')
        scl.set_thumbnail(url='https://cdn.discordapp.com/attachments/787019308260917289/800843165669130240/logo1.png')
        scl.add_field(name='Twitter', value='[Make Sure to drop a follow! Posting soon.](https://twitter.com/lycolt7)', inline=False)
        scl.add_field(name='Youtube', value='[Like + comment on recent video lol.](https://youtube.com/lycolt)', inline=False)
        scl.add_field(name='Instagram', value='[like recent post lel](https://instagram.com/lycolt7)')        

        await ctx.send(embed=scl)









def setup(client):
    client.add_cog(Socials(client))