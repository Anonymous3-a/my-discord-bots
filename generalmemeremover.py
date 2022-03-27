import discord

client = discord.Client()

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	# If the message contains an attachment and it is in #general, delete it
	if message.attachments and message.channel.name == 'general':
		await message.delete()
		await message.channel.send("Deleted attachment in #general (I hope it was a meme)")

client.run("Token")
