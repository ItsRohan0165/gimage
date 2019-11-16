import discord
from discord.ext import commands
import random

from googleapiclient.discovery import build
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
   
   
@bot.command()
async def gg(ctx, *text : str):
    print('got here')

    """Searches google for an image described by input"""
    finaltext = " "
    
    for word in text:
        finaltext = finaltext + word + " "
    
    api_key = os.getenv("API")
    cse_id = os.getenv("CSE")

    def google_search(search_term, api_key, cse_id, **kwargs):
        service = build("customsearch", "v1", developerKey=api_key)
        res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
        pprint.pprint(res)
        return res['items']

    results = google_search(finaltext, api_key, cse_id, num=1, searchType= 'image')
    for result in results:
        formatText = "" + result['link'] + ""
        await ctx.send(formatText)

bot.run(os.getenv("TOKEN"))
