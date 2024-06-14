from telethon import TelegramClient, events
import re

api_id = '24176416'
api_hash = '4493def8358e3ab32cdd7bd0c08406a2'
phone_number = '5531999592002'
source_chat = 'PumpLiveKOTH' 
target_chat = 'odysseus_trojanbot'  

client = TelegramClient('MessageForwarder', api_id, api_hash)

async def main():
    await client.start()
    print("Client Created and Started")

    # Event handler
    @client.on(events.NewMessage(chats=source_chat))
    async def handler(event):
        # Message content
        message_content = event.message.message
        print(f"MENSAGEM NOVA: {message_content}")

        whale_regex = r'Whale:\s*(.*?)\s*%'
        whale_percentage = float(re.search(whale_regex, message_content).group(1).split()[1])

        dev_regex = r'Dev:\s*(.*?)\s*%'
        dev_percentage = float(re.search(dev_regex, message_content).group(1))

        if (whale_percentage and dev_percentage):
            combined_percentage = (whale_percentage + dev_percentage) if whale_percentage != dev_percentage else whale_percentage
            print(f"Whale %: {whale_percentage}")
            print(f"Dev %: {dev_percentage}")
            print(f"Combined %: {combined_percentage}")
            if(combined_percentage <= 8):
                # Sending to Trojan   
                await client.send_message(target_chat, message_content)
                print(f"TOKEN ENVIADO AO TROJAN!")   
            else: 
                print(f"Porcentagens muito altas... RUGPULL ALERT!")   
        else:
            return print("Whale and Dev percentages not found.")

    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())