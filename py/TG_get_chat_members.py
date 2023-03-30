
import asyncio
import json
from telethon import TelegramClient, events

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
TOKENS_JSON = json.load(open('TOKENS.json'))

api_id = TOKENS_JSON['tg_MyApp_api_id']
api_hash = TOKENS_JSON['tg_MyApp_api_hash']


async def main():
    client = TelegramClient('session_name', api_id, api_hash)
    await client.start()

    # print((await client.get_me()).stringify())

    # await client.send_message('me', 'Hello! Talking to you from Telethon')
    print(await client.get_peer_id('parse1'))
    
    # async for user in client.iter_participants(-1001322924647):
    #     print(user.id)
    # users = await client.get_participants("enjoyteamclub")
    # print(users[0].first_name)

asyncio.run(main())
