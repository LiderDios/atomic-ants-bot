# bot.py
import os
import datetime
import discord
from dotenv import load_dotenv
from discord.ext import commands
import json

scrims = {
    "13/04/20 23:00":"Alpha Dragons",
    "13/05/20 23:00":"Atomic Throw",
    "13/06/20 23:00":"Keretix manco",
    "13/09/20 23:00":"Silver gm en cola abierta",
}

cadena_json = json.dumps(scrims)

print(cadena_json)

# escribe archivo json
with open('datos.json', 'w') as f:
    json.dump(cadena_json, f)


# lee archivo json

with open('datos.json', 'r') as f:
    cadena_json = json.load(f)

    print(cadena_json)

# Recibe el diccionario de scrims y devuelve un string con formato
# Team: XXXXXX - Fecha y hora: XX/XX/XX XX:XX
def dicc_string(diccionario):
    pass


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='scrims',help="Muestra todas las scrims.")
async def scrims(ctx, arg=""):
    if arg == "":
        await ctx.send(dicc_string(scrims))
    elif arg == "hoy":
        if hoy(scrims) is None:
            await ctx.send("No hay scrim hoy")
        else:
            await ctx.send(hoy(scrims))

@bot.command(name='nuevascrim',help="Agrega una scrim nueva, los argumentos son: team, fecha y hora en formato: DD/MM/AA HH:MM")
async def nuevascrim(ctx, arg1, arg2):
    pass

bot.run(TOKEN)