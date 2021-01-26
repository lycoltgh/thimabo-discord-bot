import discord
from discord.ext import commands
import random

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

@commands.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
        responses = [
                    'It is certain',
                    'Maybe No?',
                    'No You!',
                    'What Do You Think?',
                    'Srsly?',
                    'Nah',
                    'Hmmmmmmmmmmmm?',
                    'Nup',
                    'Do You Think Im Stupid?',
                    'noooooooooooo it is not',
                    'i cant',
                    'Come Ask Later Plz Im Tired',
                    'Come Ask Later',
                    'It is decidedly so',
                    'Without a doubt',
                    'Yes definitely',
                    'You may rely on it',
                    'As I see it, yes',
                    'Most likely',
                    'Outlook good',
                    'Yes',
                    'Signs point to yes',
                    'Reply hazy try again',
                    'Ask again later',
                    'Better not tell you now',
                    'Cannot predict now',
                    'Concentrate and ask again',
                    'My reply is no',
                    'My sources say no',
                    'Outlook not so good',
                    'Very doubtful']
        await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")




def setup(client):
    client.add_cog(Example(client))