import discord
from discord.ext import commands
import random
from discord import Color as c

teal = c.teal()
magenta = c.magenta()

class Ban(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def ban(self, ctx, member : discord.Member, reason=None):
        
        if reason == None:

            no = discord.Embed(color=teal)
            no.add_field(name='Whoopsie!', value=f"{ctx.author.mention}, You didn't provide a reason!" )

            await ctx.send(embed=no)
        else:

            yes = discord.Embed(color=magenta)
            yes.add_field(name='**tut tut!**', value=f'Naughty Naughty! You have been banned from `{ctx.guild.name}`')

            await member.send(embed=yes)
            await member.ban(reason=reason)


def setup(client):
    client.add_cog(Ban(client))