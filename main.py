import os
import discord
import random
import wikipedia
from dotenv import load_dotenv
from discord.ext import commands
from discord import option
from utils.format_text import format_wiki_text

def main():
    load_dotenv()

    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True

    wikipedia.set_lang('es')
    bot = commands.Bot(command_prefix='!', intents=intents)

    servers = [1207823899577024572]

    try: 
        print('Reading token...')
        token = os.getenv('TOKEN')
        print('Token obtained...')
    except:
        raise ValueError('Error obtaining the token')


    @bot.event
    async def on_ready():
        print(f'{bot.user} up and running...')


    @bot.slash_command(guild_ids=servers, name='wiki', description='Searchs for a wikipedia article')
    @option('Search', description='Search term...', type=str)
    async def wiki(ctx, search: str):
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


    @bot.slash_command(guild_ids=servers, name='ping', description='Checks the latency of the discord bot')
    async def ping(ctx):
        ms = int(bot.latency * 1000)
        await ctx.respond(f'Pong! latency: {ms}ms.')


    bot.run(token)


if __name__ == '__main__':
    print('################ DISCORD BOT ###############')
    main()