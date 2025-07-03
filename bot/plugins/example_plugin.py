import crescent
import hikari
import random
import os
import json
from collections import Counter

#from bot.utils import Plugin

plugin = crescent.Plugin[hikari.GatewayBot, None]()

os.chdir(f"{os.getcwd()}/bot/plugins")

@plugin.include
@crescent.command
class ping:
    async def callback(self, ctx: crescent.Context) -> None:
        await ctx.respond("Pong!")

@plugin.include
@crescent.command
class word:
    async def callback(self, ctx: crescent.Context) -> None:
        with open("scrabble_words_24.txt", "r") as wordsFile:
            randWord = random.choice(wordsFile.readlines())
        await ctx.respond(randWord)

@plugin.include
@crescent.command
class three:
    async def callback(self, ctx: crescent.Context) -> None:
        with open("scrabble_threes_24.json", "r") as threesFile:
            randThree = ", ".join(str(i) for i in random.choice(Counter(json.load(threesFile)).most_common(1400)))
        await ctx.respond(randThree)