# This example requires the 'members' and 'message_content' privileged intents to function.

import discord
from discord.ext import commands
import random
import requests
import re
import json

from schemas import InitUser, PlanningDate

from datetime import datetime

API_HOST="localhost"
API_PORT=5000 
API_URL=f"http://{API_HOST}:{API_PORT}"
API_URL="https://5000-morphee31-wylloffice-0vpof08g98v.ws-eu95.gitpod.io"

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.group()
async def woop(ctx):
    """List of woop commands
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'{ctx.subcommand_passed} is not woop command')


@woop.command(name="init")
async def _init(ctx, firstname: str, lastname: str, email: str = None):
    """Create your account : <firstname> <lastname> <email>
    """
    user = InitUser(
        user_id=f"{ctx.author.id}",
        firstname=firstname,
        lastname=lastname,
        email=email
    )
    check_user_exist = requests.get(
        url=f"{API_URL}/user/{ctx.author.id}",
        )

    if check_user_exist.status_code == 404:
        response = requests.post(
            url=f"{API_URL}/user",
            json=json.loads(user.json())
            )
        if response.status_code == 200:
            await ctx.send(f"Bienvenue {firstname.capitalize()} {lastname.capitalize()} ! Ton compte a bien été enregistré.")
        else:
            await ctx.send(f"Erreur inconnu !")
    else:
        await ctx.send(f"Ton compte existe déjà !")



@woop.command(name="add")
async def _add(ctx, date: str, period: str="day"):
    """Reserve a place in Wyllhouse openspace : <dd/mm/yyyy> [<null ou am ou pm>}"""
    try:
        planning_date = PlanningDate(
            day=date,
            period=period
        )
    except:
        await ctx.send(f"{date} : est au mauvais format.")

    check_user_exist = requests.get(
        url=f"{API_URL}/user/{ctx.author.id}",
        )

    if check_user_exist.status_code == 200:
        response = requests.post(
            url=f"{API_URL}/planning/{ctx.author.id}/add_date",
            json=json.loads(planning_date.json())
            )
        if response.status_code == 200:
            if period != "day":
                _period = "matin" if period == "am" else "après-midi"
            else:
                _period = ""
            await ctx.send(f"Ta réservation est enregistre pour le {date} {_period}")
        else:
            await ctx.send(f"Erreur inconnu !")
    else:
        await ctx.send(f"Ton compte n'existe pas, tu peux le créer avec la commande \"!woop_init <prénom> <nom> <email>\"")


@woop.command("rm")
async def _rm(ctx, date: str):
    """ Supprime reservation : <dd/mm/yyyy>"""
    if not re.match("^([0-2][0-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)\d{4}$", date):
        await ctx.send(f"{date} : est au mauvais format.")

    check_user_exist = requests.get(
        url=f"{API_URL}/user/{ctx.author.id}",
        )

    if check_user_exist.status_code == 200:
        response = requests.delete(
            url=f"{API_URL}/planning/{ctx.author.id}/remove_date",
            params={
                "date": date
            }
            )
        if response.status_code == 200:
            await ctx.send(f"Ta réservation pour le {date} a été supprimé")
        else:
            await ctx.send(f"Erreur inconnu !")
    else:
        await ctx.send(f"Ton compte n'existe pas, tu peux le créer avec la commande \"!woop_init <prénom> <nom> <email>\"")


@woop.command("list")
async def _list(ctx, date: str):
    """ Liste les reservations pour une journée donnée : <dd/mm/yyyy> or today"""
    if date == "today":
        _date = datetime.now().strftime("%d-%m-%Y")
    elif re.match("^([0-2][0-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)\d{4}$", date):
        _date = datetime.strptime(date, "%d/%m/%Y").strftime("%d-%m-%Y")
    else:
        await ctx.send(f"{date} : est au mauvais format.")
    response = requests.get(
        url=f"{API_URL}/planning/{_date}"
        )
    if response.status_code == 200:
        users = list()
        users = [f"{user['firstname'].capitalize()} {user['lastname'].capitalize()}" for user in response.json()]
        if users:
            await ctx.send(f"Liste des présents pour le {date} : {', '.join(users)}")
        else:
            await ctx.send(f"Pas de réservation pour le {date}")
    else:
        await ctx.send(f"Erreur inconnu !")
    


if __name__ == "__main__":
    token = input("Discord token : ")
    bot.run(token)