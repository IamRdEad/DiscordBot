import os
import discord
from discord.ext import commands
from replit import db
from keep_alive import keep_alive
import time

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def info(ctx):
    await ctx.send(ctx.guild)
    await ctx.send(ctx.author)
    await ctx.send(ctx.message.id)


@bot.command()
async def dm_all(ctx, *, args=None):
    if ctx.author.id != 247406043372584960:
        return
    counter, Gcounter, Fcounter = 1, 0, 0
    if args is not None:
        members = ctx.guild.members
        for m in members:
            if m.bot:
                continue
            if counter % 50 != 50:
                time.sleep(5)
            else:
                time.sleep(420)
            counter = counter + 1
            await ctx.send('trying to send message to: ' + str(m.display_name))
            await ctx.send('this is message nubmer: ' + str(counter))
            try:
                await m.send(args)
                await ctx.send("Message was send")
                Gcounter = Gcounter + 1
            except:
                await ctx.send('didnt work')
                Fcounter = Fcounter + 1
        await ctx.send("Sent messaged to: " + str(Gcounter) +
                       "\n failed to send to: " + str(Fcounter) +
                       "\n success rate is: " + str((Gcounter / counter) * 100) + "%")
    else:
        await ctx.send('please provide a message')


@bot.command()
async def dm_Arena(ctx, *, args=None):
    if args is not None:
        members = ctx.guild.members
        for m in members:
            print(m.display_name)
            try:
                for role in m.roles:
                    if role.name == 'Arena':
                        await m.send(args)
            except:
                print('didnt work')
    else:
        await ctx.send('please provide a message')


@bot.command()
async def dm_Duel(ctx, *, args=None):
    if args is not None:
        members = ctx.guild.members
        for m in members:
            try:
                for role in m.roles:
                    if role.name == 'Duels':
                        await m.send(args)
            except:
                print('didnt work')
    else:
        await ctx.send('please provide a message')


@bot.command()
async def dm_Guess(ctx, *, args=None):
    if args is not None:
        members = ctx.guild.members
        for m in members:
            try:
                for role in m.roles:
                    if role.name == 'Guess The Elo':
                        await m.send(args)
            except:
                print('didnt work')
    else:
        await ctx.send('please provide a message')


@bot.command()
async def dm_Test(ctx, *, args=None):
    if args is not None:
        members = ctx.guild.members
        for m in members:
            try:
                for role in m.roles:
                    if role.name == 'Testing':
                        await m.send(args)
            except:
                print("didn't work")
    else:
        await ctx.send('please provide a message')
keep_alive()
bot.run(os.environ['Toekn'])
