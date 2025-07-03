import crescent
import hikari

from bot.model_wrapper.model import Model

Plugin = crescent.Plugin[hikari.GatewayBot, Model]
