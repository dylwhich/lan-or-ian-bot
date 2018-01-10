from slackbot.bot import listen_to

@listen_to('Ian')
def the_person(message):
    message.reply("Ian, the person", in_thread=True)

@listen_to('lan')
def the_department(message):
    message.reply("LAN, the department/network", in_thread=True)
