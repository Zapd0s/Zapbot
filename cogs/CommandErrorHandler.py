import discord
from discord.ext import commands


class CommandErrorHandler(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        
        if hasattr(ctx.command, 'on_error'):
            return

        cog = ctx.cog
        if cog:
            if cog._get_overridden_method(cog.cog_command_error) is not None:
                return

        error = getattr(error, 'original', error)
        embed = discord.Embed(title = "ERROR", description = f"{error}", color = discord.Color.from_rgb(255,0,0))
        embed.set_thumbnail(url = "https://cdn.discordapp.com/emojis/807936734871420939.gif?v=1")
        embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
        embed.set_footer(text = "The error has been sent to the developer for fixing!", icon_url = self.client.user.avatar_url)
        await ctx.send(embed = embed)

        


def setup(client):
    client.add_cog(CommandErrorHandler(client))