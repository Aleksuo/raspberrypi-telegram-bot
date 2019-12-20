from telegram.ext import Updater, CommandHandler, Filters

import logging
import os
import sys

from commands import *

print(os.environ["TELEGRAM_TOKEN"])
def get_config():
    token = ''
    username = ''
    try:
        token = os.environ["TELEGRAM_TOKEN"]
    except KeyError:
        print("Please set the environment variable TELEGRAM_TOKEN")
        sys.exit(1)

    if len(sys.argv) == 2:
        username = sys.argv[1]
    else:
        print("Please give a username for binding the bot.")
        sys.exit(1)
    return (token, username)


def main():
    token, username = get_config()
    updater = Updater(
        token=token, use_context=True)
    dispatcher = updater.dispatcher

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    print("Initializing handlers")
    filter = Filters.user(username="@"+username)
    start_handler = CommandHandler('start', start, filter)
    ip_handler = CommandHandler("ip", ip, filter)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(ip_handler)
    print("Started polling")
    updater.start_polling()


if __name__ == "__main__":
    main()
