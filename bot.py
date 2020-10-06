# bot.py
import os
import datetime
#from datetime import datetime
import discord
from dotenv import load_dotenv
from discord.ext import commands
import json
import asyncio

# escribir
def escribir(arg1, arg2):
    # Ejemplo de como guardar los datos. 
    # "13/04/20 23:00":"Alpha Dragons",

    try: # Si el archivo .json ya existe directamente pasar los args

        #Abro el archivo .json y lo guardo en una variable
        with open('datos.json', 'r') as f:
            cadena_json = json.load(f)

        cadena_json[arg1] = arg2 # Agrego los dos argumentos como nuevas entradas del diccionario .json

    except Exception as err: # Si falla al abrir el .json porque no existe lo crea primero y despues lo pasa
        print("Creando archivo .json debido a:", err)
        with open('datos.json', 'w') as f:
            json.dump({}, f, sort_keys=True, indent=2)
        
        #Abro el archivo .json y lo guardo en una variable
        with open('datos.json', 'r') as f:
            cadena_json = json.load(f)

        cadena_json[arg1] = arg2 # Agrego los dos argumentos como nuevas entradas del diccionario .json


    try:
        # escribe en el archivo el dato
        with open('datos.json', 'w') as f:
            json.dump(cadena_json, f, sort_keys=True, indent=2) # Agrego el cadena_json modificado a datos.json

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

# Muestra todas las scrim programadas
def mostrar_scrims():
    with open('datos.json', 'r') as f:
        cadena_json = json.load(f)

    scrims = "" # Iniciar variable para ir pasando las scrims a type string.
    for keys in cadena_json:
        scrims += f"Fecha y hora: {keys} - Equipo: {cadena_json[keys]}\n"
    
    return scrims # Devuelve el string formateado, si no hay scrims programadas devuelve un string vacio.

# Devuelve un string que dice si hay scrim hoy.
def scrim_hoy():
    with open('datos.json', 'r') as f:
        cadena_json = json.load(f)

    hoy = "" # Iniciar variable para pasar la scrim de hoy.
    for keys in cadena_json:
        if keys[0:8] == datetime.datetime.now().strftime("%d/%m/%y"):
            hoy += f"Fecha y hora: {keys} - Equipo: {cadena_json[keys]}\n"
    
    if hoy == "": # Si no se encontro ninguna scrim hoy.
        return "Hoy no hay scrim."
    else: # Sino devuelve la scrim programada para el dia.
        return hoy

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='scrims',help="Muestra todas las scrims.")
async def todasscrim(ctx, arg=""):
    if arg == "":
        if mostrar_scrims() != "":
            await ctx.send(mostrar_scrims())
        else:
            await ctx.send("No hay ninguna scrim programada.")
    elif arg == "hoy":
        await ctx.send(scrim_hoy())

@bot.command(name='nuevascrim',help="Agrega una scrim nueva, los argumentos son: team, fecha y hora en formato: DD/MM/AA HH:MM")
async def nuevascrim(ctx, arg1, arg2):

    # Recupero la respuesta de la funcion escribir 
    rta = escribir(arg1, arg2)
    
    # el comando funciona asi. arg1 arg2
    # $nuevascrim "09/19/18 13:55" asdf

    datetime_object = datetime.datetime.strptime(arg1, '%d/%m/%y %H:%M')
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

@bot.command(name='limpiar_la_db_los_fines_de_semana',help="No usar este comando")
async def limpiar_archivo(ctx):
    el_autor = ctx.author.name
    print(el_autor)

    if(el_autor!="LiderDios"):
        print("puto el que lee")
        # await ctx.send(arg)
        await ctx.send(f"Ud. señor, {ctx.author}, no tiene permiso de ejecutar este comando. Besitos.")
        return
    else:
     with open("datos.json", "w") as output: 
          print("Archivo borrado ")
    await ctx.send(f"Listo, {ctx.author}, el archivo se limpió.")






bot.run(TOKEN)