import discord
from discord.ext import commands
import random
from discord import Color as c

teal = c.teal()
magenta = c.magenta()

class Shop(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def shop(self, ctx):
        scl = discord.Embed(
            color=magenta
        )
        scl.set_author(name='Get yourself some code, at a great price!', icon_url='https://cdn.discordapp.com/attachments/787019308260917289/800843165669130240/logo1.png')
        scl.set_thumbnail(url='https://cdn.discordapp.com/attachments/787019308260917289/800843165669130240/logo1.png')
        scl.set_footer(text='Man, what a shop.')
        scl.add_field(name='Auth System', value='`Best Auth System` - **A fast, mode.js auth system, can create custom keys, eg. lycolt. also can generate keys, eg. XXXX-XXXX-XXXX', inline=False)
        scl.add_field(name='You Name It', value='`The YNI Program` - **You name it, mangisto will code it, (if he can)**', inline=False)
        scl.add_field(name='Discord Bots', value='`Discord Bot` - **Feature Rich discord bots, custom logo, status, and prefix** ')      
        scl.add_field(name='VPS Hosting', value='`VPS Service` - **Mangisto owns his own servers. He beats any prices of vps hosting services out there.**')

        await ctx.send(embed=scl)


def setup(client):
    client.add_cog(Shop(client))