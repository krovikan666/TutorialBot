import discord

token = 'NTAyMzAxOTY2MDUxODM1OTEx.Dql9Xw.7Re4UE7CnHXNIMALkeEqtyM-Ung'
client = discord.Client()


@client.event
async def on_ready():
    print('The bot is ready!')
    await client.change_presence(game=discord.Game(name='Making a bot'))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == 'Hello':
        await client.send_message(message.channel, 'World')

client.run(token)