import crescent
import hikari
import random

#from bot.utils import Plugin

plugin = crescent.Plugin[hikari.GatewayBot, None]()

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
            randWord = random.choice(wordsFile.readLines)
        await ctx.respond(randWord)

#@plugin.include
#@crescent.command
#class three:
#    async def callback(self, ctx: crescent.Context) -> None:
#        await ctx.respond("Pong!")