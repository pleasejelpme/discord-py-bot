import discord
import aiosqlite
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
    async def poke(self, ctx, user: Option(discord.Member, required=True)): # type: ignore
        await ctx.respond(f'<@{ctx.author.id}> sent a poke to <@{user.id}>')


    @discord.slash_command(guild_ids=servers, name='add_user', description='Add user to the database')
    @commands.has_permissions(moderate_members=True)
    async def add_user(self, ctx, user: Option(discord.Member, required=True)): # type: ignore
        try:
            conn = await aiosqlite.connect('botdb.db')
            cursor = await conn.cursor()
            await cursor.execute('INSERT INTO users VALUES(?, ?)', (user.id, ctx.guild.id))
            await conn.commit()
            await cursor.close()
            await conn.close()

            await ctx.respond(f'User <@{user.id}> added successfully to the database!')
        except Exception as e:
            print(f'Error: {e}')
            await ctx.respond('Ocurrio un error al agregar al usuario')


def setup(bot):
    bot.add_cog(User(bot))