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

@client.event
async def on_message(message):
    # Be shy about being yelled at
    if "BEN" in message.content:
        messages = { 
                     0:"It's not my fault I'm programmed this way...",
                     1:"I'm trying, I really am!",
                     2:"Please don't get mad, I'll try to do better",
                     3:"I'm sorry.",
                     4:"*flinches*",
                     5:"Please don't yell at me, I'm doing my best..."
                    }
        # Generate the random message.
        x = random.randint(0, 5)
        # Send it to the channel.
        await message.channel.send(messages[x])
    
    # There is a 4% chance of saying "Ok Zoomer"
    if random.randint(0, 25) == 4 or (str(message.author) == "Crimson#0884" and random.randint(0, 8) == 2)\
            or "ok boomer" in message.content.lower():
        await message.channel.send("Ok Zoomer")

    # 1 in 2 chance of actually responding so things don't get out of hand
    ran = random.randint(0, 1)
    if ran == 1:
        print("Passed roll. "+str(ran))
        # If the bot sent the message, do nothing
        if message.author == client.user:
            return
        else:
            # create a try function so that it sends a message to discord on an error
            try:
                # TODO: Split these functions off into command functions.
                # If someone mentions java, say "Java good" and react with a cup of java
                if "java" in message.content.lower():
                    await message.channel.send("Java good")
                    await message.add_reaction("☕")

                # If a message starts with "
                # TODO change this so it cuts off by sentence and can find it anywhere
                if message.content.startswith("I am "):
                    await message.channel.send("Hi, " + message.content[5:] + ", I'm Ben Steele!")

                # If a word ends in "er" make a "I hardly know er" joke
                words = message.content.split(" ")
                for word in words:
                    if len(word) > 3:
                        punctuation = [".", ",", "!", "?", ":", ";", "(", ")"]
                        word = word[:-1] if word[-1] in punctuation else word
                        if word[-2:].lower() == "er" and not word == "her":
                            await message.channel.send('"' + word[:-2] + " 'er\"? I 'ardly know 'er!")

            except Exception as e:
                # Error catching for the bot. Send a message with the error log if it breaks.
                await message.channel.send("Whoa, I didn't like that. You gave me the error:")
                await message.channel.send(str(e))
    else:
        print("Failed roll. " + str(ran))


@client.event
async def on_ready():
    print(f"logged on as: {client.user.name}\ntoken: {client.user.id}")

client.run(config.TOKEN)
