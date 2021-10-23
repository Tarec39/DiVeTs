import discord
import config
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
        await msg.channel.send(twitter.nyaa(msg.content).extractDirectLink())

client.run(config.TOKEN)