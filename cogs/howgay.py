import discord
from discord.ext import commands
import random

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client
        
    @commands.command(aliases=['8ball', 'test'])
    async def howgay(self, ctx):

        response = random.randrange(101)
        
        await ctx.send(f"He is defo {response}% Gay")




def setup(client):
    client.add_cog(Example(client))