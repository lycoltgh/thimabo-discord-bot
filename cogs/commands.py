import discord
from discord.ext import commands
import random
from discord import Color as c

teal = c.teal()
magenta = c.magenta() #choose any colour, but be mindful of the discord.Color colours, they are wierd, unless you go with a custom RGB "system"

class Load(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def commands(self, ctx):
        em = discord.Embed(
            color=teal
        )
        em.add_field(name="`Prefix`", value='**My Prefix Is** - <', inline = False)
        em.add_field(name="Commands", value='Do <Commands to get a list of the finest commands i have to offer.', inline = False)
        em.add_field(name='Developer', value="Do <dev to see who made me!", inline = False)
        em.set_author(name="Information", icon_url="https://cdn.discordapp.com/attachments/787019308260917289/802610114187231242/gwb.gif")
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/787019308260917289/802610114187231242/gwb.gif")

        await ctx.send(embed=em)

print('LOADED')