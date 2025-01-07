import discord
from discord.ext import commands
from utils.servers import servers


class Benchmarks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @discord.slash_command(guild_ids=servers, name='ping', description='Checks the latency of the discord bot')
    async def ping(self, ctx):
        ms = int(self.bot.latency * 1000)
        await ctx.respond(f'Pong! latency: {ms}ms.') 


def setup(bot):
    bot.add_cog(Benchmarks(bot))