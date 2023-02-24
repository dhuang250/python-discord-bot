import discord
import random
from discord.ext import commands
from discord import TextChannel

print(discord.__version__)
intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='$', case_insensitive=True)

location = None

destination = None

userID = None     # ENTER ID of ADMIN HERE


# announcement command (rcv and say)

# DESCRRIPTION: use this command inside a discord text channel to set channel as desired announcement channel.
#               Once used, the channel id will be set to location above
@client.command()
async def rcv(ctx):
    if ctx.author.id == userID:
        global location
        location = ctx.channel
        print(ctx.channel)
    else:
        await ctx.send("cant use this command. not dev of this bot")


# DESCRIPTION: use within any other channel to produce an announcement in the text channel that has its channel id
#              saved in the location variable above
@client.command()
async def say(ctx, *, msg=None):
    print(location)
    if ctx.author.id == userID:
        arr = msg.split()
        if "@" in arr:
            print("cant ping yet. need to add function")
        ctx.channel = location
        await ctx.channel.send(msg)
    else:
        await ctx.channel.send("cant use command. not dev of this bot")


# DESCRIPTION: notifies when the bot in online
@client.event
async def on_ready():
    print('Bot is ready.')


# DESCRIPTION: send server latency
@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)} ms')


# DESCRIPTION: hello world
@client.command()
async def hello(ctx):
    await ctx.send("hello")


# DESCRIPTION: retrieves user id
@client.command()
async def getUserID(ctx, *, user_id=None):
    if user_id is not None:
        print(user_id[3:-1])
        await ctx.send("done")
    else:
        await ctx.send("member parameter required")


@client.command()
async def pinguser(ctx, *, user_id=None):
    if user_id is not None:
        member = await ctx.guild.fetch_member(user_id[3:-1])
        await ctx.send(f'{member.mention}')
    else:
        await ctx.send("no member")


# DESCRIPTION: kick user from server
@client.command()
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason = reason)


# DESCRIPTION: ban user from server. user cannot rejoin until unbanned
@client.command()
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)


# DESCRIPTION: unban a banned user from server
@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    name, discriminator = member.split('#')

    for entry in banned_users:
        user = entry.user

        if (user.name, user.discriminator) == (name, discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.name}#{user.discriminator}')


client.run('<insert token>')

