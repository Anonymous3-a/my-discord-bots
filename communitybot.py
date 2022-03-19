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

client.run("OTUzODQ4MzU2ODM1MzAzNTM1.YjKigQ.hZPMH9ATed8F1YNaQp_Sxaj4xmM")