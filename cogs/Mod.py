import discord
from discord.ext import commands
import asyncio
import random
import typing
import sqlite3

class Mod(commands.Cog):
  
  def __init__(self, client):
    self.client = client
  


  @commands.command()
  @commands.guild_only()
  @commands.has_permissions(manage_roles = True)
  async def addrole(self, ctx, member:discord.Member, role:discord.Role):
    await member.add_roles(role)
    embed = discord.Embed(title = "Role added", description = f"Added the role {role.mention} to {member.mention}", color = discord.Color.random())
    embed.set_footer(text = f"Action by {ctx.author.name}")
    embed.set_timestamp(ctx.message.created_at)

  @commands.command()
  @commands.guild_only()
  @commands.has_permissions(kick_members = True)
  async def kick(self, ctx, member: discord.Member,*, reason = None):
    await member.kick(reason = reason)
    embed = discord.Embed(title = "Kick Successful", description = f"{member} was successfully yeeted out of the server")
    embed.set_image(url = "https://media.tenor.com/images/27f16871c55a3376fa4bfdd76ac2ab5c/tenor.gif")
    embed.set_footer(text = f"Action taken by {ctx.author.display_name}")
    await ctx.send(embed = embed)
  
  @commands.command()
  @commands.guild_only()
  @commands.has_permissions(ban_members = True)
  async def ban(self, ctx, member: discord.Member = None, *, reason = None):
    if member == None:
      embed = discord.Embed(title = "Ban Hammer ready", description = "Who should I yeet?")
      embed.set_image(url = "https://media.tenor.com/images/7895bffb008b21f3e347ddbd4297697a/tenor.gif")
      await ctx.send(embed = embed)
      return
    await member.ban(reason = reason)
    embed = discord.Embed(title = "Ban Successful", description = f"{member} was ban hammered")
    embed.set_footer(text = f"Action taken by {ctx.author.display_name}")
    embed.set_image(url = "https://media.tenor.com/images/7895bffb008b21f3e347ddbd4297697a/tenor.gif")
    await ctx.send(embed = embed)

  @commands.command()
  @commands.has_permissions(ban_members = True)
  async def unban(self, ctx, id:int):
    member = discord.Object(id=id) 
    try:
      await ctx.guild.fetch_ban(member)
    except discord.NotFound:
      await ctx.send(f"{member} is not banned!")
    else:
      await ctx.guild.unban(member)
      await ctx.send(f"Unbanned {member}")

  @commands.command()
  @commands.guild_only()
  @commands.has_permissions(manage_channels = True)
  async def nuke(self, ctx):
    pos = ctx.channel.position
    def check(message):
      return message.author == ctx.author and message.channel == ctx.channel
    await ctx.send(f" {ctx.author.mention}, You sure about that? Reply with a 'yes' or 'no'")
    try:
      confirm = await self.client.wait_for('message', check = check, timeout = 30)
    except asyncio.TimeoutError:
      await ctx.send("Okay no nuking today")
    if confirm.content == "yes":
      await ctx.send(f"Purging {ctx.channel.mention}...")
      new_channel = await ctx.channel.clone()
      await ctx.channel.delete()
      await new_channel.edit(position = pos)
      embed = discord.Embed(title = "Nuked this Channel!", description = "Want to invite me to your servers? \n [Click Here!](https://bit.ly/ZapbotInvite)", color = self.client.ecolor)
      await new_channel.send(embed = embed)
  
  @commands.command()
  @commands.guild_only()
  @commands.has_permissions(manage_messages = True)
  async def purge(self, ctx,target: typing.Optional[discord.Member] = None, amount: int = 10):
      if not target:
        deleted = await ctx.channel.purge(limit = amount)
        await ctx.send(f"Deleted **{len(deleted)-1}** messages", delete_after = 5)
      else:
        def check(message):
          return message.author == target
        deleted = await ctx.channel.purge(limit = amount, check = check)
        await ctx.send(f"Deleted **{len(deleted)}** messages from {target.name}", delete_after = 5)

      

  @commands.command()
  @commands.guild_only()
  @commands.has_permissions(kick_members = True)
  async def mute(self, ctx, member:discord.Member):
    muted_role = discord.utils.get(ctx.guild.roles,name='Muted')
    if not muted_role:
      await ctx.send("Mute role not found. Creating mute mole")
      muted_role = await ctx.guild.create_role(name = "Muted")
      await ctx.send(f"{muted_role.mention} role creating. Applying overwrites... may take a while")
      for channel in ctx.guild.text_channels:
        await channel.set_permissions(muted_role, send_messages = False)
    
    await member.add_roles(muted_role)
    embed = discord.Embed(title = "Mute Successful", description = f"Added the role {muted_role.mention} to {member.mention}", colour = self.client.ecolor)
    await ctx.send(embed = embed)

  @commands.command()
  @commands.guild_only()
  @commands.has_permissions(kick_members = True)
  async def unmute(self, ctx, member:discord.Member):
      muted_role = discord.utils.get(ctx.guild.roles,name='Muted')
      if muted_role in member.roles:
        await member.remove_roles(muted_role)
        embed = discord.Embed(title = "Unmute Successful", description = f"Removed the role {muted_role.mention} from {member.mention}", colour = self.client.ecolor)
        await ctx.send(embed = embed)
      else:
        await ctx.send("That member is not muted!")
  
  @commands.command()
  @commands.guild_only()
  @commands.has_permissions(manage_channels = True)
  async def lock(self, ctx, channel: discord.TextChannel = None):
    if channel == None:
      channel = ctx.channel
    await channel.set_permissions(ctx.guild.default_role,read_messages=True, send_messages=False)
    embed = discord.Embed(title = "Locked the channel", description = f"{channel.mention} is locked down", colour = self.client.ecolor)
    await ctx.send(embed = embed)
    if channel != ctx.channel:
      await channel.send(embed = embed)
  
  @commands.command()
  @commands.guild_only()
  @commands.has_permissions(manage_channels = True)
  async def unlock(self, ctx, channel: discord.TextChannel = None):
    if channel == None:
      channel = ctx.channel
    await channel.set_permissions(ctx.guild.default_role,read_messages=True, send_messages=True)
    embed = discord.Embed(title = "Unlocked the channel", description = f"{channel.mention} is unlocked", colour = self.client.ecolor)
    await ctx.send(embed = embed)
    if channel != ctx.channel:
      await channel.send(embed = embed)

  @commands.command()
  @commands.has_permissions(kick_members = True)
  async def warn(self, ctx, member: discord.Member = None, *, reason = None):
    if member == None:
      await ctx.send("Mention someone to warn!")
    else:
      embed = discord.Embed(title = f"Warned {member}", description = f"{member.mention} was warned. \n Reason: {reason}", colour = discord.Colour.from_hsv(random.random(), 1, 1))
      embed.set_footer(text = f"Action taken by moderator {ctx.author.name}")
      await ctx.send(embed = embed)
      warn_channel = discord.utils.get(ctx.guild.channels,name =  "warnings")
      if warn_channel == None:
        warn_channel = await ctx.guild.create_text_channel("warnings")
        await warn_channel.set_permissions(ctx.guild.default_role, send_messages = False)
      await warn_channel.send(embed = embed)
  



def setup(client):
  client.add_cog(Mod(client))