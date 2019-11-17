import discord
from discord.ext import commands
import random

from googleapiclient.discovery import build
import discord.channel
import pprint
import asyncio
import os

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='/',description=description)

bot.remove_command('help')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    print(bot)

@bot.command()
async def define(ctx, *text: str):
    finaltext = 'define '
    for word in text:
        finaltext = finaltext + word  + " "
    
    api_key = os.getenv("API")
    cse_id = os.getenv("CSE")
    def google_search(ctx, search_term, api_key, cse_id, **kwargs):
        service = build("customsearch", "v1", developerKey=api_key)
        res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
        pprint.pprint(res)
        return res['items']    
    results = google_search(finaltext, api_key, cse_id, num=1)
    for result in results:
        formatText="```" + result['snippet'] + "```"
        await ctx.send(formatText)
@bot.command()
async def search(ctx, *text : str):
    print('got here')

    """Searches google for an image described by input"""
    finaltext = " "
    
    for word in text:
        finaltext = finaltext + word + " "
    
    api_key = os.getenv("API")
    cse_id = os.getenv("CSE")

    def google_search(ctx, search_term, api_key, cse_id, **kwargs):
        service = build("customsearch", "v1", developerKey=api_key)
        res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
        pprint.pprint(res)
        return res['items']

    results = google_search(finaltext, api_key, cse_id, num=1, searchType= 'image')
    for result in results:
        formatText = "" + result['link'] + ""
        await ctx.send(formatText)

@bot.command()
async def Noice(ctx):
    await ctx.send("http://is2.4chan.org/vg/1486404760144.gif")

@bot.command()
async def Hariotttt(ctx):
    """Post ainsley"""
    await ctx.send("https://ih0.redbubble.net/image.37276369.1324/flat,800x800,075,f.u2.jpg")
@bot.command()
async def JoJo(ctx):
    """Asks if JOJO"""
    await ctx.send("http://i3.kym-cdn.com/photos/images/original/001/195/575/abf.jpg")
@bot.command()
async def Tides(ctx):
    """How quickly the tides turn"""
    await ctx.send("http://i1.kym-cdn.com/photos/images/original/001/072/409/23c.gif")


bot.run(os.getenv("TOKEN"))
