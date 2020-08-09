# movie_genre_bot.py
import os
import requests
import array as arr
import json

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

# keep sensitive information in .ENV
TOKEN = os.getenv('DISCORD_TOKEN') 
KEY = os.getenv('KEY') 

bot = commands.Bot(command_prefix='!') # prefix command to call bot

@bot.command(name='categories', help='lists possible categories to choose from')
async def categories(ctx):
    genList = genreList()
    for i in genList:
        await ctx.send(i) # send result into chat


@bot.command(name='top', help='shows top movies from chosen genre')
async def top(ctx, message):
    movieList = createList()
    result = []
    for genre in movieList:
        if(genre[0].strip() == message.capitalize()):
            for movie in range(1,len(genre)):
               await ctx.send(genre[movie].strip())

@bot.command(name='movie', help='searches for movies by title')
async def omdb(ctx, *message):
    query = '+'.join(message)
    url = 'http://www.omdbapi.com/?t=' + query + '&plot=full&apikey=' + KEY
    response = get_query(url)
    response = json.dumps(response, sort_keys=True, indent=4)
    await ctx.send(response)

def genreList():
    """retrieve and outputs possible genres to choose from in chat"""
    lst = createList()
    genreList = []
    for i in lst:
        genreList.append(i[0].strip())
    return genreList

def createList():
    """create 2d array with each row contains a genre"""
    file = open('movie_data.txt', 'r')
    lst = []
    for i in range(28):
        temp = []
        for j in range (6):
            temp.append(file.readline())
        lst.append(temp)
    return lst

def check_valid_status(request):
    """ensures that website can be accessed"""
    if request.status_code == 200:
        return request.json()
    return False

def get_query(url):
    """call on website API to recieve JSON information"""
    request = requests.get(url)
    data = check_valid_status(request)
    return data
bot.run(TOKEN)
