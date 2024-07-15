from telethon import TelegramClient, events
import re
from dotenv import load_dotenv
import os

load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
phone_number = os.getenv('PHONE_NUMBER')
target_chat = os.getenv('TARGET_CHAT')
log_group = int(os.getenv('LOG_GROUP'))

client = TelegramClient('MessageForwarder', api_id, api_hash)

async def main():
    await client.start()
    print("Client Created and Started")

    source_chats = [
        "shmooscasino", 
        "wulfcalls", 
        "degenroshis", 
        "Cryptocowboyx", 
        "lyxedegen", 
        -1001500884162, # Exy's Lab
        -1001835320066, # BossMan Calls
        "LevisAlpha", 
        "CryptoZinTrades",
        "shahlito",
        # "evenmoredegen", 
        # -1002040294338, # Gem's calls
        # "luis100xcalls", 
        # "creepercalls", 
    ]  # Add your source chat IDs here

    @client.on(events.NewMessage(chats=source_chats))
    async def handler(event):
        # Message content
        message_content = event.raw_text
        source_chat_id = event.chat_id
        source_title = event.chat.title if event.chat else ''
        # Solana address regex
        solana_address_regex = r'[A-HJ-NP-Za-km-z1-9]{32,44}'
        solana_address = re.search(solana_address_regex, message_content)

        if solana_address:
            token_address = solana_address.group(0)

            await client.send_message(target_chat, token_address)

            await client.send_message(log_group, f"Token enviado ao Trojan!\n\nChatID: {source_chat_id}\nChat name: {source_title}\n\nToken: {token_address}")  
        else:
            await client.send_message(log_group, f"No solana address found.\n\nChatID: {source_chat_id}\nChat name: {source_title}")

    @client.on(events.NewMessage(chats=log_group))
    async def statusHandler(event):
        await client.send_message(log_group, 'We are up!\n\n' + str(source_chats))

    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())