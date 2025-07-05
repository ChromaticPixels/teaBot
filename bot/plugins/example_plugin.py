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

# view with crescent context passed for additional utility
class ContextView(miru.View):
    def __init__(self, ctx: crescent.Context, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.players = 0
        self.crescent_ctx = ctx

    # define a new TextSelect menu with two options (vestigal template that might be useful)
    @miru.text_select(
        placeholder="Select me!",
        options=[
            miru.SelectOption(label="Option 1"),
            miru.SelectOption(label="Option 2"),
        ],
    )
    async def basic_select(self, ctx: miru.ViewContext, select: miru.TextSelect) -> None:
        await ctx.respond(f"You've chosen {select.values[0]}!")

    # join tea (TODO: once per user; currently inf per user)
    @miru.button(label="Players: 0", style=hikari.ButtonStyle.PRIMARY)
    async def basic_button(self, ctx: miru.ViewContext, button: miru.Button) -> None:
        self.players += 1
        button.label = f"Players: {self.players}"
        await ctx.edit_response(components=self)
        await ctx.respond("Joined!", flags=hikari.MessageFlag.EPHEMERAL)

    # cancel view
    @miru.button(label="Abort!", style=hikari.ButtonStyle.DANGER)
    async def stop_button(self, ctx: miru.ViewContext, button: miru.Button) -> None:
        await ctx.respond("The host has aborted.")
        self.stop()

    async def on_timeout(self) -> None:
        # no interactions so no ctx available to respond with...
        if self.players == 0:
            # ...thus, moderate scuff
            await self.crescent_ctx.respond("Nobody joined? How drab...")
            return None
        await self.message.respond(f"It seems {self.players} player(s) were interested.")

@plugin.include
@crescent.command
async def ping(ctx: crescent.Context) -> None:
    view = ContextView(ctx, timeout=3.0)
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