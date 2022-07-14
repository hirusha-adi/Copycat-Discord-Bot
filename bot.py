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


_make_off()


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
    embed.add_field(name=f"{data['prefix']}status",
                    value="Current repeating status", inline=False)
    embed.add_field(name=f"Current Status",
                    value=f"{_check_on_off()}", inline=False)
    embed.add_field(name=f"About This Project",
                    value="Made by Github user **@hirusha-adi**. This project is completely free and open source and under the MIT License", inline=False)
    embed.set_footer(text=f'Requested by {ctx.author.name}')
    await ctx.send(embed=embed)
    return


@client.command()
async def start(ctx, user: discord.Member):
    embed = discord.Embed(title=data['title'], url=data['repo'],
                          description=f"Status: **{_check_on_off()}**",
                          timestamp=datetime.utcnow(),
                          color=0x00FFFF)
    embed.set_footer(text=f'Requested by {ctx.author.name}')
    await ctx.send(embed=embed)


@client.command()
async def stop(ctx, user: discord.Member):
    return


@client.command()
async def status(ctx):
    embed = discord.Embed(title=data['title'], url=data['repo'],
                          description=f"Status: **{_check_on_off()}**",
                          timestamp=datetime.utcnow(),
                          color=0x00FFFF)
    embed.set_footer(text=f'Requested by {ctx.author.name}')
    await ctx.send(embed=embed)


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('(pleasestartrepeating'):
        try:
            _make_on()
            await message.channel.send("Started")
        except Exception as e:
            await message.channel.send(f"An error has occured while changing status to 'on': {e}")

    if msg.startswith('(pleasestoprepeating'):
        try:
            _make_off()
            await message.channel.send("Stopped")
        except Exception as e:
            await message.channel.send(f"An error has occured while changing status to 'on': {e}")

    else:
        try:
            if _check_on_off() == "off":
                pass
            elif _check_on_off() == "on":
                await message.channel.send(str(msg))
            else:
                await message.channel.send("Something else is wrong - please ask ZeaCeR#5641 to check the code")
        except Exception as e:
            await message.channel.send(f'An error has occured: {e}')

if __name__ == "__name__":
    with open("token.key", "r", encoding='utf-8') as _token_file:
        TOKEN = _token_file.read()
    client.run(TOKEN)
