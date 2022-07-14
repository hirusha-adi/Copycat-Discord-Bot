import discord
from datetime import datetime
from discord.ext import commands
import os

data = {
    "title": "CopyCat Bot",
    "repo": "https://github.com/hirusha-adi/Copycat-Discord-Bot",
    "prefix": "rb"
}

client = commands.Bot(command_prefix=data['prefix'])


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


@client.event
async def on_ready():
    print(f'We have logged in as {client.user} | {client.user.id}')


@client.command()
async def help(ctx):
    embed = discord.Embed(title=data['title'], url=data['repo'],
                          description="Help for {title}".format(
                              title=data['title']),
                          timestamp=datetime.utcnow(),
                          color=0x00FFFF)
    embed.set_author(name=client.user.name,
                     url=data['title'], icon_url=client.user.avatar_url)
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/877796755234783273/997036774037655602/unknown.png")
    embed.add_field(name=f"{data['prefix']}help",
                    value="Display help", inline=False)
    embed.add_field(name=f"{data['prefix']}start [@user]",
                    value="Start repeating a user", inline=False)
    embed.add_field(name=f"{data['prefix']}stop [@user]",
                    value="Stop repeating a user", inline=False)
    embed.add_field(name=f"About This Project",
                    value="Made by Github user **@hirusha-adi**. This project is completely free and open source and under the MIT License", inline=False)
    embed.set_footer(text=f'Requested by {ctx.author.name}')
    await ctx.send(embed=embed)
    await ctx.send()


@client.command()
async def start(ctx):
    pass


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    msg = message.content

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
                pass
            elif check_on_off() == "on":
                await message.channel.send(str(msg))
            else:
                await message.channel.send("Something else is wrong - please ask ZeaCeR#5641 to check the code")
        except Exception as e:
            await message.channel.send(f'An error has occured: {e}')

if __name__ == "__name__":
    with open("token.key", "r", encoding='utf-8') as _token_file:
        TOKEN = _token_file.read()
    client.run(TOKEN)
