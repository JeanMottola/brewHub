# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord
from discord.ext import commands
import requests


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)




@bot.command(brief='$city [city] [number of breweries returned]', description='returns a set amount or all breweries in a given city, if no int passed in args all breweries will be returned')
async def city(ctx, city_name, number_of_breweries = float("inf") ):
        response = requests.get("https://api.openbrewerydb.org/v1/breweries?by_city=" + city_name)
        print(response.status_code)
        await ctx.send("Found " + str(len(response.json())) + " breweries in "  + city_name)
        counter = 0
        for brew in response.json():
            print(brew)
            name = brew["name"] + "\nType of brewery: " + brew["brewery_type"] + "\nLocation: " + brew["city"] + ", " + brew["state"]
            if brew["website_url"] != None:
                name += " " 
                name += brew["website_url"]
            await ctx.send(name)
            await ctx.send("-------------------------------------------")
            counter+=1
            if counter == number_of_breweries:
                break

@bot.command(brief='$randbrew', description='returns random brewery')
async def randbrew(ctx):
    response = requests.get("https://api.openbrewerydb.org/v1/breweries/random")
    
    response_list = response.json()
    print(response_list[0]["name"])
    body = response_list[0]["name"] + "\nType of brewery: " + response_list[0]["brewery_type"] + "\nLocation: " + response_list[0]["city"] + ", " +response_list[0]["state"]
    if response_list[0]["website_url"]:
        body = body + "\n" + response_list[0]["website_url"]
    await ctx.send(body)
    


# Do not forget to remove token before pushing
bot.run("insert token here")

