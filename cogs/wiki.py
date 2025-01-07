import discord
import wikipedia
from discord.ext import commands
from discord import option
from utils.format_text import format_wiki_text
from utils.servers import servers


class Wiki(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @discord.slash_command(guild_ids=servers, name='wiki', description='Searchs for a wikipedia article')
    @option('Search', description='Search term...', type=str)
    async def wiki(self, ctx, search: str):
        await ctx.channel.trigger_typing()

        try:
            wikisearch = wikipedia.summary(search, sentences=1)
            url = wikipedia.page(search).url
            summary = format_wiki_text(wikisearch)
            await ctx.respond(summary)
            await ctx.respond(url)
        except wikipedia.exceptions.DisambiguationError as e:
            await ctx.respond(f'Multiple results found: {', '.join(e.options)}')
        except wikipedia.exceptions.PageError:
            await ctx.respond('No results found.')
    

def setup(bot):
    bot.add_cog(Wiki(bot))