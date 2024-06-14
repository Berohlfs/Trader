from telethon import TelegramClient, events
import re

api_id = '24176416'
api_hash = '4493def8358e3ab32cdd7bd0c08406a2'
phone_number = '5531999592002'
source_chat = 'PumpLiveKOTH' 
target_chat = 'paris_trojanbot'  

client = TelegramClient('MessageForwarder', api_id, api_hash)

async def main():
    await client.start()
    print("Client Created and Started")

    # Event handler
    @client.on(events.NewMessage(chats=source_chat))
    async def handler(event):
        # Message content
        message_content = event.message.message
        print(f"\n\nMENSAGEM NOVA: {message_content}")
        message_first_social = event.message.buttons[1][0].text
        print(f"Primeiro social: {message_first_social}")

        whale_regex = r'Whale:\s*(.*?)\s*%'
        whale_raw = re.search(whale_regex, message_content)

        dev_regex = r'Dev:\s*(.*?)\s*%'
        dev_raw = re.search(dev_regex, message_content)

        dev_is_out_regex = r'Dev:\s*(.*?)\s*is Out!'
        dev_is_out = re.search(dev_is_out_regex, message_content)

        replies_regex = r'Replies:\s*(.*?)\s*📈'
        replies_raw = re.search(replies_regex, message_content)

        if (whale_raw and (dev_raw or dev_is_out) and replies_raw):
            whale = float(whale_raw.group(1).split()[1])
            dev = float(dev_raw.group(1)) if (not dev_is_out) else 0
            replies = int(replies_raw.group(1))

            combined_percentage = (whale + dev) if whale != dev else whale

            print(f"\nWhale %: {whale}")
            print(f"Dev %: {dev}")
            print(f"Combined %: {combined_percentage}")
            print(f"Total replies: {replies}")

            flag = 6 if (dev == whale or dev == 0) else 12
            print(f"FLAG: {flag}")

            if(combined_percentage <= flag and replies >= 0 and message_first_social == "Website"):
                await client.send_message(target_chat, message_content)
                print(f"TOKEN ENVIADO AO TROJAN!")  
            else: 
                print(f"(RUGPULL ALERT) ou (Few replies) ou (Webiste inexistente).")
        else:
            return print("\nErro ao encontrar os dados necessários para análise.")

    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())