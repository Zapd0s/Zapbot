import discord 
from discord.ext import commands

class Help(commands.Cog):
  
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def help(self, ctx, category = None):
    if not category:
      embed = discord.Embed(title = "Help", description = "Thank you for using Zapbot", color = self.client.ecolor)
      embed.add_field(name = "Moderation", value  = "``kick`` ``ban`` ``warn`` ``warning`` ``mute`` ``unmute`` ``lock`` ``unlock`` ``purge`` ``nuke``", inline = False)
      embed.add_field(name = "Fun", value = "``secret`` ``joke``  ``8ball`` ``dice`` ``gayrate`` ``simprate`` ``spoiler`` ``mock`` ``meme`` ``post``", inline = False)
      embed.add_field(name = "Utility", value = "``userinfo`` ``server`` ``calc`` ``info`` ``snipe`` ``pinh`` ``giveinvite`` ``invite``", inline = False)
      embed.add_field(name = "Image Generation", value = "``magik`` ``pixel`` ``wanted`` ``triggered`` ``ascii``", inline = False)
      embed.add_field(name = "Invite :D", value = "[Click Me!](https://bit.ly/ZapbotInvite)", inline = False)
      embed.set_footer(text = "IF U HAVE ANY SUGGESTION / BUG REPORT DO IT BY USING >suggest OR >bug !!!")
      await ctx.send(embed = embed)
    if category == 'kick':
      await ctx.send("Command Name: kick \n Kicks a member from the server \n Required Permission: Kick Members")
    elif category == "ban":
      await ctx.send("Command Name: ban \n Bans a member permanently from the server \n Required Permission: Ban Members")
    elif category == "warn":
      await ctx.send("Command Name: warn \n Warns a member with a reason and posts an embed regarding it in #warnings (Channel will be created if it doesn't exist) \n Required Permission: Kick Members")
    elif category == "mute":
      await ctx.send("Command Name: mute \n Mutes a member by adding a role 'Muted' to them. \n Required Permission: Kick Members")
    elif category == "unmute":
      await ctx.send("Command Name: unmute \n Unmutes a muted person. \n Required Permission: Kick Members")
    elif category == "lock":
      await ctx.send("Command Name: lock \n Sets the given channel's permission for everyone to not send messages \n Required Permission: Manage Channels")
    elif category == "unlock":
      await ctx.send("Command Name: unlock \n Unlocks a locked channel \n ")
    elif category == "purge":
      await ctx.send("Command Name: purge \n Bulk deletes messages on the channel if member is specified will delete messages from that person alone. Number of messages defaults to 10 \n Required Permission: Manage Messsages")
    elif category == "nuke":
      await ctx.send("Command Name: purge \n Clones a channel and remakes it with the same permissions. Useful to remove unwanted pings \n Required Permission: Manage Channels")
    elif category == "secret":
      await ctx.send("Command Name: secret \n Send an anonymous message to someone. Works only on DMs to ensure privacy")
    elif category == "8ball":
      await ctx.send("Command Name: 8ball \n Ask a question to the 8ball")
    elif category == "gayrate":
      await ctx.send("Command Name: gayrate \n Will tell you how gay you are. \n ||https://media.tenor.com/images/11f11d685fe8b55401d16768f5e5789b/tenor.gif||")
    elif category == "simprate":
      await ctx.send("Command Name: simprate \n Will tell you how much of a simp you are")
    elif category == "mock":
      await ctx.send("cOManD nAmE: MOcK \n dO i neEd tO eXpLAiN tHIs?")
    elif category == "spoiler":
      await ctx.send("||C||||o||||m||||m||||a||||n||||n||||d|| ||N||||a||||m||||e|||| :||||I bet no one reads this||")
    elif category == "server":
      await ctx.send("Learn more about your server")
    elif category == "userinfo":
      await ctx.send("Learn about someone or... yourself?")
    elif category == "calc":
      await ctx.send("Make me do your homework")
    




def setup(client):
  client.add_cog(Help(client))