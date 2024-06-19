from telethon import TelegramClient, events
import re

api_id = '29979879'
api_hash = '648942e486bf97a31d9106dbb8cd26f0'
phone_number = '5531998100509'

target_chat = 'diomedes_trojanbot'

client = TelegramClient('MessageForwarder', api_id, api_hash)

async def main():
    await client.start()
    print("Client Created and Started")

    source_chats = ["shmooscasino", "wulfcalls", "degenroshis", "luis100xcalls" , "creepercalls", "Cryptocowboyx", "lyxedegen", "evenmoredegen", "Diorscabal"]  # Add your source chat IDs here

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

    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())