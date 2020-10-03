# bot.py
import os
import datetime
import discord
from dotenv import load_dotenv
from discord.ext import commands

scrims = {
    datetime.datetime(2020,10,8,23):"Alpha Dragons",
    datetime.datetime(2020,10,3,23):"Atomic Throw",
    datetime.datetime(2020,10,13,23):"Keretix manco",
    datetime.datetime(2020,10,12,23):"Silver gm en cola abierta",
}

# Recibe el diccionario de scrims y devuelve un string con formato
# Team: XXXXXX - Fecha y hora: XX/XX/XX XX:XX
def dicc_string(diccionario):
    string = ""
    for keys in diccionario:
        string += f"Team: {diccionario[keys]} - Fecha y hora: {keys.strftime('%d/%m/%y a las %X')}\n"
    return string

def hoy(diccionario):
    for keys in diccionario:
        if keys.strftime("%d/%m/%y") == datetime.datetime.now().strftime("%d/%m/%y"):
            return f"Team: {diccionario[keys]} - Fecha y hora: {keys.strftime('%d/%m/%y a las %X')}"

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='scrims',help="Muestra todas las scrims.")
async def test(ctx, arg=""):
    if arg == "":
        await ctx.send(dicc_string(scrims))
    elif arg == "hoy":
        if hoy(scrims) is None:
            await ctx.send("No hay scrim hoy")
        else:
            await ctx.send(hoy(scrims))

bot.run(TOKEN)