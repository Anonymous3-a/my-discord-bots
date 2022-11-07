import discord

intents = discord.Intents.none() # Replace none with whatever you need
client = discord.Client(intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('$hello'):
        await message.channel.send("World!")

client.run("TOKEN HERE")
