#DONT SKID
import discord

client = discord.Client()

@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      await user.send('YOUR MESSAGE')
      print(f"messaged: {user.name}")
    except:
       print(f"couldnt message: {user.name}")

client.run('YOUT TOKEN', bot=False)    


#SIMPLE MASS DM CODED BY two#3082
