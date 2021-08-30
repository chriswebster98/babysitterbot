"""A module used to handle the swearsitter cog."""
from discord.ext import commands
from babysitter.utils import regex_finder

class SwearSitter(commands.Cog, name="Swear Sitter"):
    """A cog used to handle language used in a server."""

    #banned_words = []
    # list of words go here

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("SwearSitter is now ready!")


    @commands.Cog.listener('on_message')
    async def swear_patrol(self, message):
        """Used to patrol the server and give abuser's strikes."""
        checked_message = regex_finder(message.content, self.banned_words)

        if checked_message and message.author != self.bot.user:
            # if multiple foul words, join into one string
            foul_words = ' '.join(checked_message)

            warning_message = "{} - you are being warned for using the following language " \
                "in this server: {}".format(message.author.mention, foul_words)
            await message.reply(warning_message)

    

def setup(bot):
    bot.add_cog(SwearSitter(bot))