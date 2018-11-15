import discord
import asyncio
import random
import pickle
import os

heroku buildpacks:set heroku/python
client = discord.Client()

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

@client.event
async def on_message(message):
	if message.content.startswith('!tellmeajoke'):
		await client.send_message(message.channel, 'Piss off ye little shit!')
	elif message.content.startswith('!d6'):
		d6 = random.choice(['1','2','3','4','5','6'])
		await client.send_message(message.channel, d6)
	elif message.content.startswith('!d4'):
		d4 = random.choice(['1','2','3','4'])
		await client.send_message(message.channel, d4)
	elif message.content.startswith('!d8'):
		d8 = random.choice(['1','2','3','4','5','6','7','8'])
		await client.send_message(message.channel, d8)
	elif message.content.startswith('!d10'):
		d10 = random.choice(['1','2','3','4','5','6','7','8','9','10'])
		await client.send_message(message.channel, d10)
	elif message.content.startswith('!d12'):
		d12 = random.choice(['1','2','3','4','5','6','7','8','9','10','11','12'])
		await client.send_message(message.channel, d12)
	elif message.content.startswith('!d20'):
		d20 = random.choice(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'])
		await client.send_message(message.channel, d20)
	elif message.content.startswith('!dHundred'):
		dHundred = random.choice(['10','20','30','40','50','60','70','80','90','100'])
		await client.send_message(message.channel, dHundred)
	elif message.content.startswith('!yeet'):
		await client.send_message(message.channel, 'This bitch empty!')
	elif message.content.startswith('!stuck'):
		await client.send_message(message.channel, 'Ask a GM or a DM for assistance.')
	elif message.content.startswith('!currentversion'):
		await client.send_message(message.channel, 'Current Campaign: Custom 5e.')
	elif message.content.startswith('!NameGenM'):
		NameGenM = random.choice(['Corzo','Dalari','Sindero','Bolthemir','Grund','Grunheir','Kilgan','Guzuu','Folomir','Draegen','Torgest','Baltor','Baldur','Remus','Solomon','Dzirgo','Rowan'])
		await client.send_message(message.channel, NameGenM)
	elif message.content.startswith('!NameGenF'):
		NameGenF = random.choice(['Caletta','Fetari','Sindri','Malengos','Sheikk','Aeryn','Aurra','Isalli','Uda','Aseldi','Solmera','Ivevi','Nesioti','Lounja','Gogneth','Mzira',])
		await client.send_message(message.channel, NameGenF)
	elif message.content.startswith('!NameGenN'):
		NameGenN = random.choice(['Udan','Odehr','Hurgial','Alva','Kade','Kil','Autsu','Isal','Cognir','Loshnar','Wynn','Irven'])
		await client.send_message(message.channel, NameGenN)
	elif message.content.startswith('!botscript'):
		await client.send_message(message.channel, 'I run on Python 3.3 and the Discord API package!')
	elif message.content.startswith('!secret1'):
		await client.send_message(message.channel, 'If you want to be a Dungeon Master, send the words -chooga book- to Ronin.')

	if message.content.startswith('Who am I?'):
		await client.send_message(message.channel, 'You are an adventurer!')

	if message.content.startswith('What are you Bjornolf?'):
		await client.send_message(message.channel, 'I am the digital embodiement of the owner of this server! He is probably away studying or learning how to update me right now.')
		
client.run('NDQ2ODI2NTQ5OTg4MDMyNTEz.Dd-rSg.045RGfgGCYFCTsVURexnOaMzymM')
