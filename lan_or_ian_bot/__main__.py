#!/usr/bin/env python

import sys
import logging
import logging.config
import lan_or_ian_bot
from slackbot import settings
from slackbot.bot import Bot

settings.PLUGINS = ['lan_or_ian_bot.plugins.basic']

def main():
    kw = {
        'format': '[%(asctime)s] %(message)s',
        'datefmt': '%m/%d/%Y %H:%M:%S',
        'level': logging.DEBUG if settings.DEBUG else logging.INFO,
        'stream': sys.stdout,
    }
    logging.basicConfig(**kw)
    logging.getLogger('requests.packages.urllib3.connectionpool').setLevel(logging.WARNING)
    bot = Bot()
    bot.run()

if __name__ == '__main__':
    main()
