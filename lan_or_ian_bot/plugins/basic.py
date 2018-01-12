from slackbot.bot import listen_to
import re

RE_IAN = '\\bIan\\b'
RE_LAN = '\\blan\\b'
RE_ANY = RE_IAN + '|' + RE_LAN

def repl_multi(text):
    return re.sub(RE_LAN, '`LAN`', re.sub(RE_IAN, '`Ian`', text))

def handle_multiple(message):
    has_ian = re.search(RE_IAN, message.body['text'])
    has_lan = re.search(RE_LAN, message.body['text'])

    if has_ian and has_lan:
        message.reply(">>>" + repl_multi(message.body['text']), in_thread=True)
        return True

    return False

@listen_to(RE_ANY)
def the_person(message):
    if not handle_multiple(message):
        if re.search(RE_IAN, message.body['text']):
            message.reply("`Ian`", in_thread=True)
        elif re.search(RE_LAN, message.body['text']):
            message.reply("`LAN`", in_thread=True)
