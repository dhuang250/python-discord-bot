import discord
import random
from discord.ext import commands
from discord import TextChannel

client = commands.Bot(command_prefix='$', case_insensitive=True)

location = None

destination = None

userID = None # ENTER ID of ADMIN HERE


# my announcement command

@client.command()
async def rcv(ctx):
    if ctx.author.id == userID:
        global location
        location = ctx.channel
        print(ctx.channel)
    else:
        await ctx.send("cant use this command. not dev of this bot")


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



@client.event
async def on_ready():
    print('Bot is ready.')


@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)} ms')


@client.command()
async def hello(ctx):
    await ctx.send("hello")



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


client.run('<insert token>')

