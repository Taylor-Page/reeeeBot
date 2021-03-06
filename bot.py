import discord
from discord.ext import commands
import os

token = open('token.txt', 'r')
cmd = '?'

bot = commands.Bot(cmd)
bot.remove_command("help")
@bot.event
async def on_ready():
    print('BEEP BOOP AM ONLINE')

@bot.command(help="Makes the bot say Pong!")
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command(hidden=True)
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

@bot.command(hidden=True)
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


bot.run(token.readline()) 