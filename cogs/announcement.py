import discord
from discord.ext import commands
import random
from discord import Color as c

teal = c.teal()
magenta = c.magenta()

print('LOADED ANNOUNCEMENT')

class Announcement(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(aliases=['ancmnt'])
    async def accouncement(self, ctx):
        anc = discord.Embed(
            color=magenta
        )
        anc.set_author(name='Important Announcement', icon_url='https://cdn.discordapp.com/attachments/787019308260917289/800843165669130240/logo1.png')
        anc.set_footer(text='tip: you can follow this channel to get updates in your personal server!')
        anc.add_field(name='**Must Read**', value='Hey, i uploaded! make sure to go and drop a `BIG FAT LIKE` on the video \n - a comment is hugely appreciated!', inline=False)
        anc.add_field(name='**Video Link**', value='You can find the epic video [here](https://youtu.be/Z8Ql-csVoa4)')
        anc.add_field(name='Sponsor', value='Thank you to Retro Recoveries for now sponsoring me! \n A giveaway will be held soon for a luna key!', inline=False)
            

        await ctx.send(embed=anc)





def setup(client):
    client.add_cog(Announcement(client))
