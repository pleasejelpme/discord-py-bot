import discord
from discord import Option
from discord.ext import commands
from utils.servers import servers


class User(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @discord.slash_command(guild_ids=servers, name='check_users', description='Test user cog')
    async def user(self, ctx):
        await ctx.respond('Checking users cog')


    @discord.slash_command(guild_ids=servers, name='poke', description='Send a poke to a user')
    @commands.has_permissions(moderate_members=True)
    async def poke(self, ctx, user: Option(discord.Member, required=True)):
        await ctx.respond(f'<@{ctx.author.id}> sent a poke to <@{user.id}>')


def setup(bot):
    bot.add_cog(User(bot))