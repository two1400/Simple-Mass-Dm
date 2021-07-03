#DONT SKID

import discord

client = discord.Client()

@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      await user.send('ENTER MESSAGE HERE')
      print(f'Mesaged: {user_name}')
    except:
      print(f'Couldnt message: {user_name}')
     
client.run("ENTER TOKEN HERE", bot=False)     


#SIMPLE MASS DM CODED BY two#3082
