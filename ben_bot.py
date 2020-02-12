"""
file: ben_bot.py
author: Alex Sutay
"""
# Discord API.
import discord
# Using random.randint()
import random
# Config file, contains the token for the bot as a variable.
# TODO: Implement a proper CFG file.
import config

# Launch the default discord client.
client = discord.Client()


async def shy(message):
    print("Trigger: Shy")
    # Be shy about being yelled at
    messages = {
        0: "It's not my fault I'm programmed this way...",
        1: "I'm trying, I really am!",
        2: "Please don't get mad, I'll try to do better",
        3: "I'm sorry.",
        4: "*flinches*",
        5: "Please don't yell at me, I'm doing my best..."
    }
    # Generate the random message.
    x = random.randint(0, 5)
    # Send it to the channel.
    await message.channel.send(messages[x])


async def zoomer(message):
    print("Trigger: zoomer")
    await message.channel.send("Ok Zoomer")


async def java(message):
    print("Trigger: java")
    if random.randint(1, 20) == 13:
        await message.channel.send("😟🔫 Please, they're forcing me to say things I don't believe, "
                                   "please, don't listen to me, java bad, JAVA BAD!!\n"
                                   "er- I mean-")
    await message.channel.send("Java good")
    await message.add_reaction("☕")


async def dadjoke(message):
    print("Trigger: dad joke")
    # TODO change this so it cuts off by sentence and can find it anywhere
    if message.content.startswith("I am "):
        await message.channel.send("Hi, " + message.content[5:] + ", I'm Ben Steele!")


async def hardly(message):
    words = message.content.split(" ")
    for word in words:
        if len(word) > 3:
            punctuation = [".", ",", "!", "?", ":", ";", "(", ")"]
            word = word[:-1] if word[-1] in punctuation else word
            if word[-2:].lower() == "er" and not word == "her" and random.randint(1, 2) == 1:
                await message.channel.send('"' + word[:-2] + " 'er\"? I 'ardly know 'er!")


@client.event
async def on_message(message):
    # Now the actions are stored in a dictionary
    actions = {
        "BEN": shy,
        "Ok Boomer": zoomer,
        "java": java,
        "I am": dadjoke,
        "er": hardly,
    }

    # If the bot sent the message, do nothing
    if message.author == client.user:
        return
    else:
        # create a try function so that it sends a message to discord on an error
        try:
            # check the dictionary for any actions to trigger
            for key in actions.keys():
                if key in message.content.lower():
                    await actions[key](message)
            # have a 1 in 20 chance of triggering ok zoomer regardless
            if random.randint(1, 20) == 10:
                await zoomer(message)
        except Exception as e:
            # Error catching for the bot. Send a message with the error log if it breaks.
            await message.channel.send("Whoa, I didn't like that. You gave me the error:")
            await message.channel.send(str(e))


@client.event
async def on_ready():
    print(f"logged on as: {client.user.name}\ntoken: {client.user.id}")


client.run(config.TOKEN)
