import discord
from discord.ext import commands
import random
from discord import Color as c

teal = c.teal()
magenta = c.magenta() 

class Load(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def info(self, ctx):
        em = discord.Embed(
            color=teal
        )
        em.add_field(name="Thimabo's Server!", value='Welcome to thimabos server. Make sure you say hello in general!', inline = False)
        em.add_field(name="Rules", value='Makes sure you read our `rules` channel.', inline = False)
        em.add_field(name='What do we do? ', value="Thimabos server is a great place to chill and chat, also provides big giveaways, and downloads!", inline = False)
        em.set_author(name="Information", icon_url="https://cdn.discordapp.com/attachments/787019308260917289/802610114187231242/gwb.gif")
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/787019308260917289/802610114187231242/gwb.gif")

        await ctx.send(embed=em)





def setup(client):
    client.add_cog(Load(client))
