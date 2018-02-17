from discord.ext import commands
from cogs.utils.checks import embed_perms
import discord

'''Module for miscellaneous commands'''


class Malicious:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def hubbub(self, ctx):
        """Create hubbub."""
        mention = ""

        for user in ctx.guild.members:
            if user.bot:
                continue

            mention += user.mention + "\n"

            if len(mention) >= 1977:
                await ctx.send(mention)
                mention = ""

        message = await ctx.send(mention)

    @commands.command(pass_context=True)
    async def shubbub(self, ctx):
        """Create hubbub silently."""
        await ctx.message.delete()
        mention = ""

        for user in ctx.guild.members:
            if user.bot:
                continue

            mention += user.mention + "\n"

            if len(mention) >= 1977:
                message = await ctx.send(mention)
                await message.delete()
                mention = ""

        message = await ctx.send(mention)
        await message.delete()

    @commands.command(pass_context=True)
    async def large(self, ctx):
        """Spam chat."""
        await ctx.message.delete()
        await ctx.send('\u2800' + ('\n' * 1998) + '\u2800')

    @commands.command(pass_context=True)  # largest when I figure out how to delay executions
    async def larger(self, ctx):
        """Spam chat... but larger."""
        spam = '\u2800' + ('\n' * 1998) + '\u2800'
        await ctx.message.delete()
        await ctx.send(spam)
        await ctx.send(spam)
        await ctx.send(spam)

    @commands.command(pass_context=True)
    async def de(self, ctx, name):
        """Embeds an image from discordemoji.com"""
        await ctx.message.delete()
        if embed_perms(ctx.message):
            try:
                await ctx.message.channel.send(content=None, embed=discord.Embed().set_image(url="https://discordemoji.com/assets/emoji/{}.png".format(name)))
            except:
                return

def setup(bot):
    bot.add_cog(Malicious(bot))

