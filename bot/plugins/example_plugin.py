import crescent
import hikari
import random
import os
import json
import asyncio
import miru
from collections import Counter

from bot.model import MyModel

plugin = crescent.Plugin[hikari.GatewayBot, MyModel]()

os.chdir(f"{os.getcwd()}/bot/plugins")

# Define a new custom View that contains 3 items
class BasicView(miru.View):

    # Define a new TextSelect menu with two options
    @miru.text_select(
        placeholder="Select me!",
        options=[
            miru.SelectOption(label="Option 1"),
            miru.SelectOption(label="Option 2"),
        ],
    )
    async def basic_select(self, ctx: miru.ViewContext, select: miru.TextSelect) -> None:
        await ctx.respond(f"You've chosen {select.values[0]}!")

    # Define a new Button with the Style of success (Green)
    @miru.button(label="Click me!", style=hikari.ButtonStyle.SUCCESS)
    async def basic_button(self, ctx: miru.ViewContext, button: miru.Button) -> None:
        await ctx.respond("You clicked me!")

    # Define a new Button that when pressed will stop the view
    # & invalidate all the buttons in this view
    @miru.button(label="Stop me!", style=hikari.ButtonStyle.DANGER)
    async def stop_button(self, ctx: miru.ViewContext, button: miru.Button) -> None:
        self.stop()  # Called to stop the view

@plugin.include
@crescent.command
async def ping(ctx: crescent.Context) -> None:
    view = BasicView()
    await ctx.respond("Pong!", components=view)
    ctx.client.model.miru.start_view(view)

@plugin.include
@crescent.command
async def word(ctx: crescent.Context) -> None:
    with open("scrabble_words_24.txt", "r") as wordsFile:
        randWord = random.choice(wordsFile.readlines())
    await ctx.respond(randWord)

@plugin.include
@crescent.command
async def three(ctx: crescent.Context) -> None:
    with open("scrabble_threes_24.json", "r") as threesFile:
        randThree = ", ".join(str(i) for i in random.choice(Counter(json.load(threesFile)).most_common(1400)))
    await ctx.respond(randThree)

async def tea_hook(ctx: crescent.Context) -> None:
    star_msg = await ctx.respond("Star        walker")
    await asyncio.sleep(5)


@plugin.include
@crescent.hook(tea_hook)
@crescent.command
async def tea(ctx: crescent.Context) -> None:
    await ctx.respond("piss tea")