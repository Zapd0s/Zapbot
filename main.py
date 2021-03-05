import discord 
from discord.ext import commands
import os
import json
import random
import asyncio
import requests
import datetime
import asyncpraw
import time



client = commands.Bot(command_prefix = ">", intents = discord.Intents.all(), activity = discord.Activity(type=discord.ActivityType.listening, name= " >help"))
client.remove_command('help')

client.ecolor = discord.Color.from_rgb(0,0,255)

reddit = asyncpraw.Reddit(client_id = os.getenv("PRAW_CLIENT_ID"), 
                     client_secret = os.getenv("PRAW_CLIENT_SECRET"),
                     username = "Zapdos007",
                     password = os.getenv("PRAW_PASSWORD"),
                     user_agent = "Discord Bot")
      





@client.command()
async def joke(ctx):
  response = requests.get("https://icanhazdadjoke.com", headers = {"Accept": "text/plain"})
  embed = discord.Embed(title = "Joke", description = response.text, color = discord.Colour.from_hsv(random.random(), 1, 1))
  await ctx.send(embed = embed)


@client.command()
async def invite(ctx):
  embed = discord.Embed(title = "Thanks for considering!", description = f"[Click Here](http://bit.ly/ZapbotInvite) to invite me to your server! \n Currently, I'm in {len(client.guilds)} servers!", color = discord.Color.green())
  embed.set_footer(text = "or bit.ly/ZapbotInvite", icon_url = client.user.avatar_url)
  await ctx.send(embed = embed)



@client.command()
@commands.is_owner()
async def load(ctx, extension):
  client.load_extension(f"cogs.{extension}")
  await ctx.send(f"Loaded ``{extension}`` successfully")

@client.command()
async def server(ctx):
  all_roles = ""
  for role in ctx.guild.roles:
    all_roles += f"{role.mention} "

  guild = ctx.guild
  embed = discord.Embed(title = ctx.guild.name, decription = f"Information on {ctx.guild}", color = client.ecolor)
  embed.add_field(name = "Members", value = guild.member_count, inline = False)
  embed.add_field(name = "Channels", value = f"All channels: {len(guild.channels)} \n Text Chanels: {len(guild.text_channels)} \n Voice Channels: {len(guild.voice_channels)}", inline = False)
  embed.add_field(name = "ID", value = guild.id, inline = False)
  embed.add_field(name = "Owner", value = guild.owner, inline = False)
  embed.add_field(name = f"Roles ({len(guild.roles)})", value = all_roles, inline = False)
  embed.set_thumbnail(url = ctx.guild.icon_url)
  await ctx.send(embed = embed)

@client.command()
@commands.is_owner()
async def unload(ctx, extension):
  client.unload_extension(f"cogs.{extension}")
  await ctx.send(f"Unloaded ``{extension}`` successfully")

@client.command()
@commands.is_owner()
async def loadall(ctx):
  for filename in os.listdir("./cogs"):
    if filename.endswith('.py'):
      client.load_extension(f"cogs.{filename[:-3]}")
      await ctx.send(f"Loaded ``{filename[:-3]}`` successfully")

@client.event
async def on_ready():
  for filename in os.listdir("./cogs"):
    if filename.endswith('.py') and not filename.startswith('Automod'):
      client.load_extension(f"cogs.{filename[:-3]}")
      print(f"Loaded ``{filename[:-3]}`` successfully")
  client.load_extension('jishaku')
  os.environ["JISHAKU_NO_UNDERSCORE"] = "True"
  os.environ["JISHAKU_NO_DM_TRACEBACK"] = "True" 
  print("Ready")
  

  

@client.command()
@commands.is_owner()
async def calc(ctx, *, numbers):
  ans = eval(numbers)
  embed = discord.Embed(title = f"Calculation done: {ans}", description = f"**{numbers} = \n {ans}**", color = client.ecolor)
  await ctx.send(embed = embed)

@client.command()
async def ping(ctx):
  start = time.perf_counter()
  a = await ctx.send("Pinging...")
  end = time.perf_counter()
  dur = (end-start) * 1000
  embed = discord.Embed(title = "Pong!", description = f"**Response Time** \n ```{dur:.2f}ms``` \n **Websocket Latency** \n ```{round(((client.latency) * 1000), 2)}ms```", color = client.ecolor)
  await a.edit(embed = embed)
  


@client.command(aliases = ["bug"])
async def suggest(ctx, *, suggestion):
  zapdos = client.get_user(694839986763202580)

  await zapdos.send(f"New Suggestion by {ctx.author} \n {suggestion}")
  await ctx.send("Thank you for your suggestion / bug report! It helps a lot!")





@client.command()
async def info(ctx, elementii):
  with open('ptable.json') as f:
    data = json.load(f)
  for element in data:
    if elementii == element['name']:
      if element['phase'] == "Solid":
        element_density = f"{element['density']} g/cm³"
      elif element['phase'] == "Liquid":
        element_density = f"{element['density']} g/cm³"
      elif element['phase'] == "Gas":
        element_density = f"{element['density']} g/l"
      else:
        element_density = element['density']
      embed = discord.Embed(title = f"{element['name']} \n {element['phase']} \n {element['symbol']}", description = element['summary'], colour = discord.Colour.from_hsv(random.random(), 1, 1), url = element['source'])
      embed.add_field(name = "Appearence", value = element['appearance'])
      embed.add_field(name = "Category", value = element['category'])
      embed.add_field(name = "Atomic mass (g)", value = element['atomic_mass'])
      embed.add_field(name = "Boiling Point (degrees kelvin)", value = element['boil'])
      embed.add_field(name = "Melting Point (degrees kelvin", value = element['melt'])
      embed.add_field(name = "Density", value = element_density)
      embed.add_field(name = "Discovered By", value = element['discovered_by'])
      await ctx.send(embed = embed)
        

@client.command()
async def userinfo(ctx, member:discord.Member = None):
  async def strfdelta(tdelta, fmt):
    d = {"days": tdelta.days}
    d["hours"], rem = divmod(tdelta.seconds, 3600)
    d["minutes"], d["seconds"] = divmod(rem, 60)
    return fmt.format(**d)
  
  if member == None:
    member = ctx.author
  roles = [role for role in member.roles]
  today = datetime.datetime.now()
  joined = member.joined_at
  c = today - joined
  o = await strfdelta(c, "{days} Days {hours} Hours and {seconds} Seconds ago!")
  created = member.created_at
  d = today - created
  e = await strfdelta(d, "{days} Days {hours} Hours and {seconds} Seconds ago!")
  embed = discord.Embed(title = member.name, description = f"Information on {member.mention}", color = client.ecolor)
  embed.add_field(name = "Nickname (if there is any)", value = member.display_name, inline = False)
  embed.add_field(name="Created Account On", value=member.created_at.strftime(f"%a, %#d %B %Y, %I:%M %p UTC ({e})"), inline = False)
  embed.add_field(name="Joined Server On", value=member.joined_at.strftime(f"%a, %#d %B %Y, %I:%M %p UTC ({o})"), inline = False)
  embed.add_field(name="Roles", value="".join([role.mention for role in roles]), inline = False)
  embed.add_field(name="Highest Role", value=member.top_role.mention, inline = False)
  embed.set_thumbnail(url = member.avatar_url)
  await ctx.send(embed = embed)

snipe_message_content = None
snipe_message_author = None
snipe_message_id = None
snipe_message = None

@client.event
async def on_message_delete(message):
  global snipe_message_content
  global snipe_message_author
  global snipe_message_id
  global snipe_message

  snipe_message_content = message.content
  snipe_message_author = message.author
  snipe_message_id = message.id
  snipe_message = message
  await asyncio.sleep(60)

  if message.id == snipe_message_id:
      snipe_message_author = None
      snipe_message_content = None
      snipe_message_id = None
      snipe_message = None

@client.command()
async def snipe(ctx):
    if snipe_message_content==None:
        await ctx.send("Theres nothing to snipe.")
    else:
        embed = discord.Embed(title = f"{snipe_message_author.name}#{snipe_message_author.discriminator}", description = f"{snipe_message_content}", color = client.ecolor)
        created_time = snipe_message.created_at
        str_time = created_time.strftime('%m/%d/%Y, %H:%M:%S')
        embed.set_footer(text =f"Deleted at {str_time}")
        await ctx.send(embed=embed)
        return


@client.command()
async def post(ctx,*, sub):
    try:
        await ctx.send("Please wait while I go fetch your post!")
        all_submissions = []
        subreddit = await reddit.subreddit(sub)
        top_posts = subreddit.top(limit = 25)
        async for post in top_posts:
            all_submissions.append(post)
        random_post = random.choice(all_submissions)
        if random_post.over_18:
            random_post = random.choice(all_submissions)
        if random_post.is_self:
          em = discord.Embed(title = random_post.title, description = random_post.selftext, color = client.ecolor)
          em.set_footer(text = f"Upvotes: {random_post.score}")
          await ctx.send(embed = em)
          return
          
        name = random_post.title
        url = random_post.url
        em = discord.Embed(title = name, color = client.ecolor)
        em.set_image(url = url)
        em.set_footer(text = f"Upvotes: {random_post.score}")
        await ctx.send(embed = em)
    except Exception as e:
        await ctx.send(e)



@client.command()
async def meme(ctx):
    async with ctx.channel.typing():
      all_submissions = []
      subreddit = await reddit.subreddit("memes")
      top_posts = subreddit.top(limit = 25)
      async for post in top_posts:
          all_submissions.append(post)
      random_post = random.choice(all_submissions)
      
      name = random_post.title
      url = random_post.url
      em = discord.Embed(title = name, color = client.ecolor, url = url)
      em.set_image(url = url)
      em.set_footer(text = f"Upvotes: {random_post.score}")
      await ctx.send(embed = em)
      return
















      
@client.command()
@commands.is_owner()
async def dm(ctx,member:discord.Member, *, msg):
  await member.send(msg)


@client.command()
async def emojify(ctx,*,strng):
  final_str = ""
  for word in strng.lower():
    for char in word:
      if char == "a":
        final_str += "<a:Letter_A:791612089394790412>"
      if char == "b":
        final_str += "<a:Letter_B:791612085657796638>"
      if char == "c":
        final_str += "<a:Letter_C:791612094063181824>"
      if char == "d":
        final_str += "<a:Letter_D:791612106843750440>"
      if char == "e":
        final_str += " <a:Letter_E:791612112002351125>"
      if char == "f":
        final_str += " <a:Letter_F:791612116175028244>"
      if char == "g":
        final_str += "<a:Letter_G:791612128246890546>"
      if char == "h":
        final_str += " <a:Letter_H:791612133276254229>"
      if char == "i":
        final_str += "<a:Letter_I:791612137813704704>"
      if char == "j":
        final_str += "<a:Letter_J:791612149255503893>"
      if char == "k":
        final_str += "<a:Letter_K:791612153584025650>"
      if char == "l":
        final_str += "<a:Letter_L:791612158340497409>"
      if char == "m":
        final_str += "<a:Letter_M:791612170395451392>"
      if char == "n":
        final_str += "<a:Letter_N:791612174342291506>"
      if char == "o":
        final_str += "<a:Letter_O:791612178578407464>"
      if char == "p":
        final_str += "<a:Letter_P:791612191991660544>"
      if char == "q":
        final_str += "<a:Letter_Q:791612197209243678>"
      if char == "r":
        final_str += " <a:Letter_R:791612201675915275>"
      if char == "s":
        final_str += "<a:Letter_S:791612212996472833>"
      if char == "t":
        final_str += "<a:Letter_T:791612217056559105>"
      if char == "u":
        final_str += "<a:Letter_U:791612221637394453>"
      if char == "v":
        final_str += "<a:Letter_V:791612234069180417>"
      if char == "w":
        final_str += "<a:Letter_W:791612239119515688>"
      if char == "x":
        final_str += "<a:Letter_X:791612243523534849>"
      if char == "y":
        final_str += "<a:Letter_Y:791612255711789056>"
      if char == "z":
        final_str += "<a:Letter_Z:791612259876470804>"
      if char == " ":
        final_str += " "
  embed = discord.Embed(title = f"{ctx.author.name} says", description = final_str, color = client.ecolor)
  await ctx.send(embed = embed)









client.run(os.getenv("TOKEN"))