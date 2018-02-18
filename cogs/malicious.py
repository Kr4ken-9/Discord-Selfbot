from discord.ext import commands
from cogs.utils.checks import embed_perms
from urllib.request import Request, urlopen
import json
import discord

'''Module for miscellaneous commands'''


class Malicious:
    def __init__(self, bot):
        self.bot = bot
        self.emojis = []
        self.update_emojis()

    def update_emojis(self):
        try:
            request = Request('https://discordemoji.com/api', headers={'User-Agent': 'Mozilla/5.0'})
            data = urlopen(request).read()
            self.emojis = json.loads(data)
        except:
            print('Failed to make a request to discordemoji.')
            return
        
        print('Successfully updated emojis!')

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

        emoji = next((x for x in self.emojis if x['title'] == name), None)

        if embed_perms(ctx.message) and emoji:
            try:
                await ctx.message.channel.send(content=None, embed=discord.Embed().set_image(url=f"https://discordemoji.com/assets/emoji/{emoji['slug']}.png"))
            except:
                return
    
    @commands.command(pass_context=True)
    async def update_de(self):
        """Updates cached emojilist"""
        self.update_emojis()

def setup(bot):
    bot.add_cog(Malicious(bot))

