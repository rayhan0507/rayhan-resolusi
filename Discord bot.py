import discord
import os
import json
import requests
import random


intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)


def get_quote():
  response = requests.get('https://zenquotes.io/api/random')
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return quote

sad_word = [
  'sedih', 'depresi', 'kecewa','menangis', 'nangis', 'nangis nih'
]

starter_encouragements = [
  'santai bang :grin:',
  'bro kau itu adalah orang terbaik di hidupku:relaxed:',
  'jangan gitu :C',
  'move on!',
  'jangan sedih dan kecewa',
  'jangan bicara seperti itu',
  'cengeng amat',
  'cengeng:joy:',
  'cengeng bgt:nerd:'
]


@client.event
async def on_ready():
  print('Kita berhasil masuk ke {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!hi gwen'):
    await message.channel.send('hi rayhan!')

  if message.content.startswith('!selamat malam'):
    await message.channel.send('selamat malam')

  if message.content.startswith('!selamat pagi'):
    await message.channel.send('selamat pagi')

  if message.content.startswith('!selamat siang'):
    await message.channel.send('selamat siang')

  if message.content.startswith('!maaf'):
    await message.channel.send('dimaafkan')

  if message.content.startswith('!inspirasi'):
    random_quote = get_quote()
    formatted_quote = f"*{random_quote}*"
    await message.channel.send(formatted_quote)

  if any(word in message.content.lower() for word in sad_word):
    await message.channel.send(random.choice(starter_encouragements))

  # ngecek kata
  if 'gwen' in message.content.lower():
    await message.channel.send(f"kenapa? bang<@{message.author.id}>!")

  # Daftar kata-kata kasar yang ingin diawasi
  kata_kasar = ['bodoh']
  if any(kata in message.content.lower() for kata in kata_kasar):
    await message.channel.send(
        f"gak boleh ngomong kasar <@{message.author.id}>!")

  # kata gak jadi
  kata_tidak_jadi = [
      '!tidak apa apa', '!gpp', '!nvm', '!bukan lu', '!bukanlu', '!bukan kamu',
      '!gapapa', '!gak jadi', '!gjdi', '!tdk apa apa', '!tdk apa'
  ]
  if any(kata in message.content.lower() for kata in kata_tidak_jadi):
    await message.channel.send('oh ok')
  

try:
  client.run(os.environ['TOKEN'])
except Exception as e:
  print(f'Ada kesalahan: {e}')
