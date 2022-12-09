from time import sleep

from fbchat import Client

from tune_exchange_bot import config, facebook
from tune_exchange_bot.utils.facebook import process_message


THREAD = config['facebook']['thread_id']


def recieve_message(message_object, author_id, thread_id, thread_type, **kwargs):
    if thread_id == THREAD or True:
        process_message(message_object)


facebook.onMessage = recieve_message

if __name__ == "__main__":
    check_last_limit = config["general"].get("check_last_limit")
    if check_last_limit:
        messages = facebook.fetchThreadMessages(THREAD, limit=check_last_limit)[::-1]
        for message_object in messages:
            process_message(message_object)

    while True:
        try:
            facebook.listen()
        except Exception:
            sleep(30)
            facebook = Client(config['facebook']['email'], config['facebook']['pass'])
            facebook.listen()
