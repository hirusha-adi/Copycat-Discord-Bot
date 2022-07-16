import os
import json
from datetime import datetime

import discord
from discord.ext import commands

# load settings
with open(os.path.join(os.getcwd(), 'settings.json'), 'r', encoding='utf-8') as _file:
    settings = json.load(_file)

# instantiate bot
client = commands.Bot(command_prefix=settings['prefix'])
client.remove_command('help')


def _make_on():
    file = open("status.txt", "w")
    file.write("on")
    file.close()


def _make_off():
    file = open("status.txt", "w")
    file.write("off")
    file.close()


def _check_on_off():
    file = open("status.txt", "r")
    status = file.read()
    file.close()
    return status


# switch off on startup by default
_make_off()


@client.event
async def on_ready():
    print(f'We have logged in as {client.user} | {client.user.id}')


@client.command()
async def help(ctx):
    embed = discord.Embed(title=settings['title'], url=settings['repo'],
                          description="Help for {title}".format(
                              title=settings['title']),
                          timestamp=datetime.utcnow(),
                          color=0x00FFFF)
    embed.set_author(name=client.user.name,
                     url=settings['repo'], icon_url=client.user.avatar_url)
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/877796755234783273/997036774037655602/unknown.png")
    embed.add_field(name=f"`{settings['prefix']}help`",
                    value="Display help", inline=False)
    embed.add_field(name=f"`{settings['prefix']}start`",
                    value="Start repeating", inline=False)
    embed.add_field(name=f"`{settings['prefix']}stop`",
                    value="Stop repeating", inline=False)
    embed.add_field(name=f"`{settings['prefix']}status`",
                    value="Current repeating status", inline=False)
    embed.add_field(name=f"Current Status",
                    value=f"*{_check_on_off()}*", inline=False)
    embed.add_field(name=f"Source Code",
                    value="[Click Here](https://github.com/hirusha-adi/Copycat-Discord-Bot)", inline=False)
    embed.set_footer(text=f'Requested by {ctx.author.name}')
    await ctx.send(embed=embed)
    return


@client.command()
async def start(ctx):
    _make_on()
    embed = discord.Embed(title=settings['title'], url=settings['repo'],
                          description=f"**New Status**: *{_check_on_off()}*",
                          timestamp=datetime.utcnow(),
                          color=0x00FFFF)
    embed.set_footer(text=f'Requested by {ctx.author.name}')
    await ctx.send(embed=embed)


@client.command()
async def stop(ctx):
    _make_off()
    embed = discord.Embed(title=settings['title'], url=settings['repo'],
                          description=f"**New Status**: *{_check_on_off()}*",
                          timestamp=datetime.utcnow(),
                          color=0x00FFFF)
    embed.set_footer(text=f'Requested by {ctx.author.name}')
    await ctx.send(embed=embed)


@client.command()
async def status(ctx):
    embed = discord.Embed(title=settings['title'], url=settings['repo'],
                          description=f"**Status**: *{_check_on_off()}*",
                          timestamp=datetime.utcnow(),
                          color=0x00FFFF)
    embed.set_footer(text=f'Requested by {ctx.author.name}')
    await ctx.send(embed=embed)


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    msg = message.content

    # repeat
    try:
        if _check_on_off() == "off":
            pass
        elif _check_on_off() == "on":
            await message.channel.send(str(msg))
        else:
            await message.channel.send(f"Something else is wrong - please report at {settings['repo']}")
    except Exception as e:
        await message.channel.send(f'An error has occured: {e}')

    await client.process_commands(message)

# load token
with open("token.key", "r", encoding='utf-8') as _token_file:
    TOKEN = _token_file.read()

client.run(TOKEN)
