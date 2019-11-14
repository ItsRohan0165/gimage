import discord
from discord.ext import commands
import random

from googleapiclient.discovery import build
import discord.channel
from discord.channel import Channel
import discord.message
from discord.message import Message
import discord.server
from discord.server import Server
import pprint
import asyncio


description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='/',description=description)

@bot.event
async def on_ready():
    bot.send_message('238261264818634752', 'boop')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    print(bot)

@bot.command()
async def define(*text: str):
    finaltext = 'define '
    for word in text:
        finaltext = finaltext + word  + " "
    
    api_key = "AIzaSyDWpZCMkyw6g-VackfIQ-zqIZwXpxxoC6w"
    cse_id = "002090988512210948953:3llemhwwasw"
    def google_search(search_term, api_key, cse_id, **kwargs):
        service = build("customsearch", "v1", developerKey=api_key)
        res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
        pprint.pprint(res)
        return res['items']    
    results = google_search(finaltext, api_key, cse_id, num=1)
    for result in results:
        formatText="```" + result['snippet'] + "```"
        await bot.say(formatText)
@bot.command()
async def gg(*text : str):
    print('got here')

    """Searches google for an image described by input"""
    finaltext = " "
    
    for word in text:
        finaltext = finaltext + word + " "
    
    api_key = "AIzaSyDEI9ei37MeTgaDyQhayyXSdHPM8ZJ4Gfk"
    cse_id = "001464282721790659668:_ja4f_we2rk"

    def google_search(search_term, api_key, cse_id, **kwargs):
        service = build("customsearch", "v1", developerKey=api_key)
        res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
        pprint.pprint(res)
        return res['items']

    results = google_search(finaltext, api_key, cse_id, num=1, searchType= 'image')
    for result in results:
        formatText = "" + result['link'] + ""
        await bot.say(formatText)

bot.run("NjE0MDcyNjc4NDM3MDkzMzk2.XczxKA.YdNDpnIX8L4aFVVN20A8Oogzon0")
