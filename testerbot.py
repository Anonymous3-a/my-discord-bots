import discord
import os
import requests
import json
import random

client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]

starter_encouragements = [
    "Cheer up!",
    "Hang in there.",
    "You are a great person/bot!"
]

thx_variations = [
    "thanks testerbot",
    "thanks, testerbot",
    "thank you testerbot",
    "thank you, testerbot",
    "thanks' testerbot",
    "thanks', testerbot",
    "thanks testerbot.",
    "thanks, testerbot.",
    "thank you testerbot.",
    "thank you, testerbot.",
    "thanks' testerbot.",
    "thanks', testerbot."
]


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith("$hello"):
        await message.channel.send("World!")

    if msg.startswith("$inspire"):
        quote = get_quote()
        await message.channel.send(quote)

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))
    
    if msg.startswith("$add"):
        await message.channel.send("Please DM my creator, sc29#5942 if you want to add something.\nPS. May I reccomend my friend, CommunityBot? To add them, ask the admin to add them. The link is: https://tinyurl.com/commubot")

client.run("No stealies")
