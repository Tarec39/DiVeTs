import discord
import config
# import getDirectVideoLink
import twitter

client = discord.Client()

@client.event
async def on_ready():
    print("ログインしました。")

@client.event
async def on_message(msg):
    if msg.author.bot:
        return

    if 'https://twitter.com/' in msg.content:
        await msg.channel.send("Sup")
        twitter.nyaa(msg.content)

client.run(config.TOKEN)