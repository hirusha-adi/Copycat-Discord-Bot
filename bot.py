import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix='(')


def make_on():
    file = open("status.txt", "w")
    file.write("on")
    file.close()


def make_off():
    file = open("status.txt", "w")
    file.write("off")
    file.close()


def check_on_off():
    file = open("status.txt", "r")
    status = file.read()
    file.close()
    return status


make_off()


TOKEN = open("token.key").read()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('(help'):
        big_shit = f'''```{str(message.author)} requested Help!
(help -> show this
(pleasestartrepeating -> start
(pleasestoprepeating -> stop
(info -> information about the bot
(status -> send the status```
'''
        await message.channel.send(big_shit)

    if msg.startswith('(pleasestartrepeating'):
        try:
            make_on()
            await message.channel.send("Started")
        except Exception as e:
            await message.channel.send(f"An error has occured while changing status to 'on': {e}")

    if msg.startswith('(pleasestoprepeating'):
        try:
            make_off()
            await message.channel.send("Stopped")
        except Exception as e:
            await message.channel.send(f"An error has occured while changing status to 'on': {e}")

    if msg.startswith('(info'):
        await message.channel.send(f'This bot is made by ZeaCeR#5641 - Using this bot for illegal activites / cyber bullying is prohibited!')
        await message.channel.send(f'Current Status: {check_on_off()}')

    if msg.startswith('(status'):
        await message.channel.send(check_on_off())

    if msg.startswith('(inv'):
        await message.channel.send("https://discord.com/api/oauth2/authorize?client_id=865913735427653632&permissions=8&scope=bot")

    else:
        try:
            if check_on_off() == "off":
                # await message.channel.send("Please switch this on and try again")
                pass
            elif check_on_off() == "on":
                # + str(message.author.mention)
                await message.channel.send(str(msg))
            else:
                await message.channel.send("Something else is wrong - please ask ZeaCeR#5641 to check the code")
        except Exception as e:
            await message.channel.send(f'An error has occured: {e}')

client.run(TOKEN)
