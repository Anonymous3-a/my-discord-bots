import discord

client = discord.Client()

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	pic_ext = ['.jpg','.png','.jpeg']
	for ext in pic_ext:
		if message.content.endswith(ext):
			await client.delete_message(message)

client.run("Gotta remember to censor those tokens")
