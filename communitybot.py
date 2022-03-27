import discord

client = discord.Client()

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

    if msg.startswith('$ping'):
        await message.channel.send("Pong!")

    if msg.startswith('$help'):
        await message.channel.send("$hello - Hello World\n$ping - Pong\n$help - This message")

client.run("token")
