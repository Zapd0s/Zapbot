import discord
from discord.ext import commands
import os
import asyncdagpi

class Image(commands.Cog):
  
  def __init__(self,client):
    self.client = client
    self.dagpi = asyncdagpi.Client(os.getenv("DAGPI_TOKEN"))

  
  @commands.command()
  async def pixel(self, ctx, member: discord.Member):
    url = str(member.avatar_url_as(format="png", size=1024))
    img = await self.dagpi.image_process(asyncdagpi.ImageFeatures.pixel(), url)
    file = discord.File(fp=img.image,filename=f"pixel.{img.format}")
    await ctx.send(file = file)

  @commands.command()
  async def triggered(self, ctx, member: discord.Member):
    async with ctx.channel.typing():
      url = str(member.avatar_url_as(format="png"))
      img = await self.dagpi.image_process(asyncdagpi.ImageFeatures.triggered(), url)
      file = discord.File(fp=img.image,filename=f"triggered.{img.format}")
      await ctx.send(file = file)

  @commands.command()
  async def wasted(self, ctx, member: discord.Member):
    async with ctx.channel.typing():
      url = str(member.avatar_url_as(format="png"))
      img = await self.dagpi.image_process(asyncdagpi.ImageFeatures.wasted(), url)
      file = discord.File(fp=img.image,filename=f"wasted.{img.format}")
      await ctx.send(file = file)

  @commands.command()
  async def ascii(self, ctx, member: discord.Member):
    async with ctx.channel.typing():
      url = str(member.avatar_url_as(format="png"))
      img = await self.dagpi.image_process(asyncdagpi.ImageFeatures.ascii(), url)
      file = discord.File(fp=img.image,filename=f"ascii.{img.format}")
      await ctx.send(file = file)

  @commands.command()
  async def wanted(self, ctx, member: discord.Member):
    async with ctx.channel.typing():
      url = str(member.avatar_url_as(format="png"))
      img = await self.dagpi.image_process(asyncdagpi.ImageFeatures.wanted(), url)
      file = discord.File(fp=img.image,filename=f"wanted.{img.format}")
      await ctx.send(file = file)

  @commands.command()
  async def magik(self, ctx, member: discord.Member):
    async with ctx.channel.typing():
      url = str(member.avatar_url_as(format="png"))
      img = await self.dagpi.image_process(asyncdagpi.ImageFeatures.magik(), url)
      file = discord.File(fp=img.image,filename=f"magik.{img.format}")
      await ctx.send(file = file)

def setup(client):
  client.add_cog(Image(client))
