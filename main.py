import os
import discord
import yfinance as yf
import asyncio
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    print('process...')
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi! How can I help you.")
    if message.content.startswith('$price'):
        m = yf.Ticker('ETH-USD')
        hist = m.history(period='max')
        data = str(hist['Close'][-1])
        await message.channel.send('price is : ' + str(round(float(data), 2)) + '$')




client.run(TOKEN)