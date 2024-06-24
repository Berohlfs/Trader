from telethon import TelegramClient, events
import re
from dotenv import load_dotenv
import os

load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
phone_number = os.getenv('PHONE_NUMBER')
target_chat = os.getenv('TARGET_CHAT')
status_check_chat = os.getenv('STATUS_CHECK_CHAT')

client = TelegramClient('MessageForwarder', api_id, api_hash)

async def main():
    await client.start()
    print("Client Created and Started")

    source_chats = [
        "shmooscasino", 
        "wulfcalls", 
        "degenroshis", 
        "luis100xcalls" , 
        "creepercalls", 
        "Cryptocowboyx",  
        "lyxedegen", 
        "evenmoredegen", 
        "Diorscabal" 
    ]  # Add your source chat IDs here

    @client.on(events.NewMessage(chats=source_chats))
    async def handler(event):
        # Message content
        message_content = event.message.message
        print(f"\n\nMENSAGEM NOVA: {message_content}")
        source_chat_id = event.chat_id
        # Solana address regex
        solana_address_regex = r'[A-HJ-NP-Za-km-z1-9]{44}'
        solana_address = re.search(solana_address_regex, message_content)

        if solana_address:
            token_address = solana_address.group(0)

            await client.send_message(target_chat, token_address)
            print(f"Call de {source_chat_id}" )
            print(f"TOKEN ENVIADO AO TROJAN!")  
        else:
            print("No Solana address found.")

    @client.on(events.NewMessage(chats=status_check_chat))
    async def handler(event):
        print('Status checked!')
        await client.send_message(status_check_chat, 'we are up')

    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())