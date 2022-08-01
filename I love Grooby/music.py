import discord
from discord.ext import commands
from youtubesearchpython import *
import youtube_dl




##def search_ez(Title):
##    try:
##        customSearch = VideosSearch(Title, limit = 1)
##        link = customSearch.result()['result'][0]['link']
##        return link
##    except:
##        return "https://www.youtube.com/results?search_query=rick+roll"


class music(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()

    async def join(self, ctx):

        if ctx.author.voice is None:
            await ctx.send("lol you're not in a voice channel")

        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await ctx.send("it's music time")
            await voice_channel.connect()
        else:
            await ctx.send("it's music time here")
            await ctx.voice_client.move_to(voice_channel)

    @commands.command()

    async def disconnect(self, ctx):
        await ctx.send("Hsin Lung says bye bye")
        await ctx.voice_client.disconnect()



    @commands.command()

    async def play(self, ctx, title):
        try:
            customSearch = VideosSearch(title, limit = 1)
            url = customSearch.result()['result'][0]['link']
        except:
            await ctx.send("Lmao your search wasn't valid, here's a classic instead")
            url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

        ctx.voice_client.stop()
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {"format": "bestaudio"}

        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download = False)
            url2 = info['formats'][0] ['url']
            source = discord.FFmpegPCMAudio(url2, **FFMPEG_OPTIONS)
            
            vc.play(source) 

    @commands.command()

    async def pause(self, ctx):
        await ctx.send("Paused")
        await ctx.voice_client.pause()

    @commands.command()

    async def resume(self, ctx):
        await ctx.send("resuming song xd")
        await ctx.voice_client.resume()
        
       
            
        
    


def setup(client):
    client.add_cog(music(client))


