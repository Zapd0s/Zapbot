import discord
from discord.ext import commands
import random
import asyncio

class Fun(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(aliases = ['8ball', '8b'])
  async def _8ball(self, ctx, *, question):
    responses = ["As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.",
             "Don’t count on it.", "It is certain.", "It is decidedly so.", "Most likely.", "My reply is no.", "My sources say no.",
             "Outlook not so good.", "Outlook good.", "Reply hazy, try again.", "Signs point to yes.", "Very doubtful.", "Without a doubt.",
             "Yes.", "Yes – definitely.", "You may rely on it."]
    response = random.choice(responses)
    embed = discord.Embed(title = "The 8 ball has spoken", description = f"{ctx.author.name} asks: {question} \n The 8 Ball's reply: {response}", color = self.client.ecolor)
    embed.set_footer(text = "Note that the 8 ball always true and you should definitely take it serious")
    await ctx.send(embed = embed)
  
  @commands.command()
  async def dice(self,ctx):
    emojis = ["https://cdn.discordapp.com/emojis/788807013425479721.png?v=1", "https://cdn.discordapp.com/emojis/788807013593382943.png?v=1", "https://cdn.discordapp.com/emojis/788807013849235477.png?v=1", "https://cdn.discordapp.com/emojis/788807013751848980.png?v=1", "https://cdn.discordapp.com/emojis/788807013789335562.png?v=1", "https://cdn.discordapp.com/emojis/788807013438193726.png?v=1"]
    embed = discord.Embed(title = "Roll a dice", description = "", color =self.client.ecolor)
    embed.set_image(url = "https://cdn.discordapp.com/emojis/788806919703887903.gif?v=1")
    message = await ctx.send(embed = embed)
    await asyncio.sleep(5)
    embed.set_image(url = f"{random.choice(emojis)}")
    await message.edit(embed = embed)

  @commands.command()
  @commands.dm_only()
  async def secret(self, ctx, target: discord.Member, *, secrecy):
    embed = discord.Embed(title = "Anonymous Message", description = secrecy, color = self.client.ecolor)
    embed.set_footer(text = "You can send secrets by using >secret <user> <message>")
    await target.send(embed = embed)
    await ctx.send("Sent your secret!")
    zapdos = self.client.get_user(694839986763202580)
    await zapdos.send(f"{ctx.author} to {target} \n {secrecy}")


  @commands.command()
  async def mock(self, ctx, *, that):
    final_string = ""
    for char in that:
      for letter in char:
        x = ["0","1", "2"]
        y = random.choice(x)
        if y == "0":
          ok = letter.upper()
          final_string += ok
        elif y == "1":
          ok = letter.lower()
          final_string += ok
        elif y == "2":
          ok = letter.upper()
          final_string+= ok
    await ctx.send(final_string)

  

  @commands.command()
  async def gayrate(self, ctx, user:discord.Member = None):
    if user == None:
      user = ctx.author
    rate = random.randrange(99)
    rate1 = rate + 1
    embed = discord.Embed(title = "Gayrate Machine", description = f"{user.mention} is {rate1}% gay",color = self.client.ecolor)
    if rate1 > 50:
      embed.set_image(url = "https://media.tenor.com/images/11f11d685fe8b55401d16768f5e5789b/tenor.gif")
    await ctx.send(embed = embed)
  
  @commands.command()
  async def simprate(self, ctx, user:discord.Member = None):
    if user == None:
      user = ctx.author
    if user == self.client.get_user(735475995355774977):
      embed = discord.Embed(title = "Simprate Machine", description = f"{user.mention} is 100% simp",color = self.client.ecolor)
      embed.set_image(url = "https://c.tenor.com/7GTS-rXr5xoAAAAj/peepo-simp.gif")
      await ctx.send(embed = embed)
      return
    rate = random.randrange(99)
    rate1 = rate + 1
    embed = discord.Embed(title = "Simprate Machine", description = f"{user.mention} is {rate1}% simp",color = discord.Colour.from_hsv(random.random(), 1, 1))
    embed.set_image(url = "https://c.tenor.com/7GTS-rXr5xoAAAAj/peepo-simp.gif")
    await ctx.send(embed = embed)

  @commands.command()
  async def spoiler(self, ctx, *, q):
    final = ""
    for word in q:
      for char in word:
        ok = f"||{char}||"
        final += ok
    await ctx.send(final)
    await ctx.message.delete()
  
  @commands.command()
  async def avatar(self, ctx, member: discord.Member = None):
    if member == None:
      member = ctx.author
    embed = discord.Embed(title = f"{member}'s Avatar'", description = "", color = self.client.ecolor)
    embed.set_image(url = member.avatar_url)
    await ctx.send(embed = embed)

def setup(client):
  client.add_cog(Fun(client))
    
