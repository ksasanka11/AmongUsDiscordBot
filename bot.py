import os

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.all()
client = discord.Client(intents=intents)
dead_members = []

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    for guild in client.guilds:
        if guild.name == GUILD:
            break

        print(f"Bot is ready on {guild.name}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('-'):
        # print(message)
        if message.author.voice and message.author.voice.channel:
            channel = message.author.voice.channel
        else:
            await message.channel.send("You are not connected to a voice channel")
            return

        connected_members = channel.members
        # await message.channel.send('Welcome to Among us bot!!')
        if message.content.startswith('-mute'):
            for member in connected_members:
                await member.edit(mute=True)
            await message.channel.send("All members are muted")

        if message.content.startswith('-unmute'):
            for member in connected_members:
                if member not in dead_members:
                    await member.edit(mute=False)
            await message.channel.send("All living members unmuted")

        if message.content.startswith('-dead'):
            users = message.content.split(' ')[1:]
            if len(users) == 0:
                await message.channel.send("Mention atleast a single connected user.")
            else:
                for user in users:
                    member = discord.utils.get(connected_members, id=int(user[3:-1]))
                    # print(member)
                    if member is None:
                        invalid_user = discord.utils.get(message.guild.members, id=int(user[3:-1]))
                        await message.channel.send(f"{invalid_user.name} is not connected to voice channel")
                        return
                    dead_members.append(member)
                    await member.edit(mute=True)
                dead_members_str = '\n - '.join([member.name for member in dead_members])
                await message.channel.send(f"Members dead in this game:\n - {dead_members_str}")

        if message.content.startswith('-newgame'):
            for member in connected_members:
                    await member.edit(mute=False)
            await message.channel.send("A new game has started. All members unmuted.")

client.run(TOKEN)