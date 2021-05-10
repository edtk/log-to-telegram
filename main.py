import os
import time
from dotenv import load_dotenv
import telebot

# Load .env
load_dotenv()

API_TOKEN = os.environ['API_TOKEN']
CHAT_ID = os.environ['CHAT_ID']
FILE_PATH = os.environ['FILE_PATH']

# Init Telegram Bot
tb = telebot.TeleBot(API_TOKEN, parse_mode=None)


def reading_log_files(filename):
    with open(filename, "r") as f:
        data = f.read().splitlines()
    return data


def log_generator(filename, period=15):
    data = reading_log_files(filename)
    while True:
        time.sleep(period)
        new_data = reading_log_files(filename)
        yield new_data[len(data):]
        data = new_data


if __name__ == '__main__':
    x = log_generator(FILE_PATH)
    for lines in x:
        # lines will be a list of new lines added at the end
        print(lines)
        for message in lines:
            if message:
                tb.send_message(CHAT_ID, message)
