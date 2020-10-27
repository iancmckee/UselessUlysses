import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix="!")
aux_verbs = []

@client.event
async def on_ready():
    print("Useless Bot")

@client.event
async def on_message(message):
    if message.content.lower()[0:5] == ('!help'):
        await message.channel.send("I'm a super basic bot. here are your options.... \n \n"
                                   "!auxverbs\t-->\tgives you a list of auxiliary  \n"
                                   "!chess \t-->\t tells you who sucks at chess\n"
                                   "!whosucksatchess \t-->\t same as above "
                                   "\n\n"
                                   "That concludes the options")
    if message.content.lower()[0:9] == "!auxverbs":
        # I need to figure out how to have global variables so I can' stop double defining this.
        await message.channel.send("Auxiliary Verbs are: " + "am, is, are, was were, "
                                                             "being, been, be, Have, has, "
                                                             "had, do, does, did, will, would, "
                                                             "shall, and should")
    if message.content.lower()[0:16] == "!whosucksatchess" or message.content.lower()[0:6] == "!chess":
        await message.channel.send("Harry sucks at Chess")
    if str(message.author) != "UselessUlysses#7456":
        if "ass " in message.content:
            phrase = message.content[message.content.find("ass "):].replace("ass ", "ass!")
            firstSpace = phrase.find(" ")
            if firstSpace == -1:
                assPhrase = phrase.replace("!", "-")
            else:
                assPhrase = phrase[:firstSpace + 1].replace("!", "-")
            if assPhrase[len(assPhrase.rstrip())-1:].rstrip() == "s":
                begin = "What are "
            else:
                begin = "What's an "
            if phrase[assPhrase.find('-')+1:len(assPhrase)].rstrip() not in ["am", "is", "are", "was" "were", "being", "been", "be", "Have",
                 "has", "had", "do", "does", "did", "will", "would", "shall", "should"]:
                await message.channel.send(begin + assPhrase.rstrip() + "?", file=discord.File('spongebob.png'))

key = os.environ.get('USELESS_ULYSSES_KEY')
client.run(key)