# bot.py
import os
import datetime
from datetime import datetime
import discord
from dotenv import load_dotenv
from discord.ext import commands
import json


# print(cadena_json)

def escribir(arg1, arg2):
    # Ejemplo de como guardar los datos. 
    # "13/04/20 23:00":"Alpha Dragons",

    # Obtengo los parametros y los guardo en un dicc.
    scrims = {
        arg1:arg2
    }
    # Se dumpea a json
    cadena_json = json.dumps(scrims)

    try:
        # escribe en el archivo el dato
        with open('datos.json', 'a') as f:
            json.dump(cadena_json, f)

            rta={}
            rta['Estado'] = True
            rta['Respuesta'] = "Se agrego correctamente el dato."
            # Retorno que se agrego bien
            return rta

    # si no se pudo agregar, retorno el error
    except Exception as erroR:
        # error para que veamos nosotros. 
        print ("Error al abrir la base de datos", erroR)
        # Le devuelvo el error al usuario 
        rta={}
        rta['Estado'] = False
        rta['Respuesta'] = "Error al agregar el dato."
        # Retorno que se agrego bien
        return rta

# # lee archivo json
# cadena_json = eval(json.load(f))
# with open('datos.json', 'r') as f:
#     cadena_json = json.load(f)

#     print(cadena_json)

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
async def todasscrim(ctx, arg=""):
    await ctx.send(arg)
    pass

@bot.command(name='nuevascrim',help="Agrega una scrim nueva, los argumentos son: team, fecha y hora en formato: DD/MM/AA HH:MM")
async def nuevascrim(ctx, arg1, arg2):

    # Recupero la respuesta de la funcion escribir 
    rta = escribir(arg1, arg2)
    
    # el comando funciona asi. arg1 arg2
    # $nuevascrim "09/19/18 13:55" asdf

    datetime_object = datetime.strptime(arg1, '%m/%d/%y %H:%M')

    print(datetime_object, "formato fecha hora.")

    # Obtengo la respuesta de la funcion
    if rta['Estado'] is False:
        # Si la respuesta de la funcion es false, entonces devuelvo la respueta
        await ctx.send(rta['Respuesta'])
        # y retorno.
        return rta['Estado']

    
    if rta['Estado'] is True:
        await ctx.send(rta['Respuesta'])
        return rta['Estado']
    pass

bot.run(TOKEN)