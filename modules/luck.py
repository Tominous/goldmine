"""Definition of the bot's Luck module.'"""
import random

from discord.ext import commands
from .cog import Cog

class Luck(Cog):
    """Commands that require some luck to use.
    Lose the coin toss for me, will you?
    """

    @commands.command()
    async def choose(self, *choices: str):
        """Chooses between choices given.
        Syntax: choose [choice 1] [choice 2] [choice 3] [etc...]"""
        await self.bot.say(random.choice(choices))

    @commands.command()
    async def flip(self):
        """Flips a virtual coin... or a person!
        Syntax: flip"""
        await self.bot.say('The coin toss revealed... ' + random.choice(['Heads', 'Tails'] + '!'))

    @commands.command()
    async def roll(self, dice: str):
        """Rolls a virtual dice in [# of rolls]d[Range: 1-N] format.
        Syntax: roll [number of rolls]d[max number, normally 6]"""
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await self.bot.say('Format has to be in NdN!')
            return

        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await self.bot.say(result)