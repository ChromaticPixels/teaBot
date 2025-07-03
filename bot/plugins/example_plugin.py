import crescent
import hikari
#from bot.utils import Plugin

plugin = crescent.Plugin[hikari.GatewayBot, None]()

@plugin.include
@crescent.command
class ping:
    async def callback(self, ctx: crescent.Context) -> None:
        await ctx.respond("Pong!")