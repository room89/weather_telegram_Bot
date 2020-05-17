import telegram

import secdist


def main():
    bot = telegram.Bot(token=secdist.secdist['bot']['token'])
    while True:
        try:
            bot.get_updates(new_offset)

            last_update = bot.get_last_update()

            last_update_id = last_update['update_id']
            last_chat_text = last_update['message']['text']
            last_chat_id = last_update['message']['chat']['id']

            if last_chat_text.lower() == '/hello':
                bot.send_message(last_chat_id, 'Hello')

            new_offset = last_update_id + 1
        except KeyboardInterrupt:
            exit()
        except IndexError:
            pass


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
