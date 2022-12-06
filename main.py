
import configparser
import os

from fbchat import Client

from tune_exchange_bot.utils.helpers import parse_spotify_track_id


config = configparser.ConfigParser()
config.read(os.path.join("tune-exchange-bot", "tune_exchange_bot", "config", "config.ini"))

THREAD = config['facebook']['thread_id']


class CustomClient(Client):
    def onMessage(self, message_object, author_id, thread_id, thread_type, **kwargs):
        print(message_object, author_id, thread_id, thread_type)


client = Client(config['facebook']['email'], config['facebook']['pass'])

messages = client.fetchThreadMessages(THREAD, limit=10000)

with open("messages.txt", "w") as f:
    for message in messages:
        if message.text:
            try:
                f.write(message.text + "\n")
                print(parse_spotify_track_id(message.text))
            except:
                pass

# client.listen()
