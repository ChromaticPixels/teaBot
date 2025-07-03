import os
import crescent
import dotenv
import hikari
import asyncio
import uvloop

from bot.model import Model

uvloop.install()
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

dotenv.load_dotenv()

bot = hikari.GatewayBot(os.environ["TOKEN"])

model = Model()

client = crescent.Client(bot, model)
client.plugins.load_folder("bot.plugins")

bot.subscribe(hikari.StartingEvent, model.on_start)
bot.subscribe(hikari.StoppedEvent, model.on_stop)

bot.run()
