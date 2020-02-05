"""
file: ben_bot.py
author: Alex Sutay
"""
import discord
import random
import config

client = discord.Client()


@client.event
async def on_message(message):
    # Be shy about being yelled at
    if "BEN" in message.content:
        x = random.randint(0, 5)
        if x == 0:
            await message.channel.send("It's not my fault I'm programmed this way...")
        elif x == 1:
            await message.channel.send("I'm trying, I really am!")
        elif x == 2:
            await message.channel.send("Please don't get mad, I'll try to do better")
        elif x == 3:
            await message.channel.send("I'm sorry.")
        elif x == 4:
            await message.channel.send("*flinches*")
        else:
            await message.channel.send("Please don't yell at me, I'm doing my best...")

    # 1 in 3 chance of actually responding so things don't get out of hand
    ran = random.randint(0, 1)
    if ran == 1:
        print("Passed roll."+str(ran))
        # If the bot sent the message, do nothing
        if message.author == client.user:
            return
        else:
            # create a try function so that it sends a message to discord on an error
            try:
                # If someone mentions java, say "Java good" and react with a cup of java
                if "java" in message.content.lower():
                    await message.channel.send("Java good")
                    await message.add_reaction("☕")

                # There is a 4% chance of saying "Ok Zoomer"
                if random.randint(0, 25) == 4 or (str(message.author) == "Crimson#0884" and random.randint(0, 8) == 2)\
                        or "ok boomer" in message.content.lower():
                    await message.channel.send("Ok Zoomer")

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
                await message.channel.send("Whoa, I didn't like that. You gave me the error:")
                await message.channel.send(str(e))
    else:
        print("Failed roll." + str(ran))


@client.event
async def on_ready():
    print("logged on as")
    print(client.user.name)
    print(client.user.id)


client.run(config.TOKEN)
