import discord
# This is the only dependency for discord bots

from random import *
from discord.ext import commands
# for voice control LOL 
import youtube_dl

from insultgenerator import phrases 

def insult():
    return phrases.get_so_insult_with_action_and_target("Your Mom", "she")



client = commands.Bot(command_prefix = " ? ")
players = {}

@client.event
# README: For python APIs,  discord bots are event/callback analyzed (kinda sucks I wanted to do it in Java) 
# The decorator thingy (@client.evemt) is essentially awaiting a new event
# Before asynchronously performing said action in function 

async def on_ready():
    print("We have logged in as {0.user}, he probably has a big peepee".format(client))




@client.event

async def on_message(message):
    if message.author == client.user: #we don't wanna do anyt if the bot sends a message 
        return


    if message.content.startswith("$homework"):
        # for the bot, commands are prefixed with a dolla sign 
        await message.channel.send("hi scrub, you have a grand total of " + str(randint(69, 100)) + " pieces of homework, better get to it!")


    if message.content.startswith("$yomama"):
        await message.channel.send(insult())

@client.command(pass_context = True)


async def join(ctx):

    if ctx.author.voice is None:
        await ctx.send("lol you're not in a voice channel")

    voice_channel = ctx.author.voice.channel
    if ctx.voice_client is None:
        await voice_channel.connect()
    else:
        await ctx.voice_client.move_to(voice_channel)
        
@client.command(pass_context = True)

async def leave(ctx):
    await ctx.voice_client.disconnect()

@client.command(pass_context = True)

async def play(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.created_ytdl_player(url)
    players[server.id] = player
    player.start() 
        

client.run("ODYwODg3NTczMzQ0ODEzMDc2.YOByCA.0oFTNzyLqO3ejVDSNTJTByWwFzo")
        
        


        
        
    
    

