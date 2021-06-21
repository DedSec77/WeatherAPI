import discord
from discord.ext import commands
from discord.ext.commands import Bot
import requests
import json
from colour import colours

API_KEY = ""
TOKEN = ""
url = "http://api.openweathermap.org/data/2.5/weather?"


bot = commands.Bot(command_prefix='/', help_command=None)
@bot.command(pass_context=True) #разрешаем передавать агрументы
async def weather(ctx, arg):
    city_name = arg
    Final_url = url + "appid=" + API_KEY + "&q=" + city_name
    weather_data = requests.get(Final_url).json()
 
    name = weather_data["name"]
    if "Rain" in weather_data["weather"][0]["main"]:
        weath = "Дождь"
        colors = colours.blue
        link = "https://i.pinimg.com/originals/a2/b9/bc/a2b9bc87ad46b6112da6459ab53bdb82.png"
    elif "Smoke" in weather_data["weather"][0]["main"]:
        weath = "Туман"
        colors = colours.teal
    elif "Snow" in weather_data["weather"][0]["main"]:
        weath = "Снег"
        colors = colours.light_grey
        link = "https://creazilla-store.fra1.digitaloceanspaces.com/emojis/58578/cloud-with-snow-emoji-clipart-md.png"
    elif "Clear" in weather_data["weather"][0]["main"]:
            weath = "Солнечно"
            colors = colours.orange
            link = "https://e7.pngegg.com/pngimages/317/848/png-clipart-happy-sunshine-cartoon-smile.png"
    elif "Clouds" in weather_data["weather"][0]["main"]:
            weath = "Облачно"
            colors = colours.dark_grey
            link = "http://clipart-library.com/img/1838469.png"
    else:
        weath = "Не смог найти"
        link = None
    county = weather_data["sys"]["country"]
    wind = weather_data["wind"]["deg"]

    embed = discord.Embed(
        title="WeatherAPI",
        description="Страна: " + county + "\n" + "Город: " + name + "\n"  + "Погода: " + weath + "\n" "Ветер: " + str(wind) + "deg" + "\n", 
        color=colors,
    )

    embed.set_image(url=link)
    #await ctx.send("Страна: " + county + "\n" + "Город: " + name + "\n"  + "Погода: " + weath + "\n" "Ветер: " + str(wind) + "deg" + "\n")
    await ctx.send(embed=embed)
bot.run(TOKEN)