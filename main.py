# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord
from discord.ext import commands
import requests


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def brew(ctx, arg):
        response = requests.get("https://api.openbrewerydb.org/v1/breweries?by_city=" + arg)
        print(response.status_code)
        await ctx.send("Found " + str(len(response.json())) + " breweries in "  + arg)
        for brew in response.json():
            print(brew)
            name = brew["name"] 
            if brew["website_url"] != None:
                name += " " 
                name += brew["website_url"]
            await ctx.send(name)


# Do not forget to remove token before pushing
bot.run("[#insert token here#]")
