import os
import discord
import wikipedia
from dotenv import load_dotenv
from discord.ext import commands

def main():
    load_dotenv()

    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True

    wikipedia.set_lang('es')
    bot = commands.Bot(command_prefix='!', intents=intents)

    cogs = ['wiki', 'benchmarks', 'users']

    for cog in cogs:
        bot.load_extension(f'cogs.{cog}')


    try: 
        print('Reading token...')
        token = os.getenv('TOKEN')
        print('Token obtained...')
    except:
        raise ValueError('Error obtaining the token')


    @bot.event
    async def on_ready():
        print(f'{bot.user} up and running...')


    bot.run(token)


if __name__ == '__main__':
    print('################ DISCORD BOT ###############')
    main()