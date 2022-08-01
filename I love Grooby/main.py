import discord
from discord.ext import commands
import music 

token = "ODYzMzYzMzEzNjQ3NDg0OTI4.YOlzvg.pc3JsCSb0bw6ZmFQh6PQ17Z2CAA"
client = commands.Bot(command_prefix = "?" , intents = discord.Intents.all())

cogs = [music]

for i in range(len(cogs)):
    cogs[i].setup(client)
    print("Music_bot logged in xd")



client.run(token)
