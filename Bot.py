import Modules
import praw
import logging

# [censored] = censored

reddit = praw.Reddit(client_id='[censored]',
                     client_secret='[censored]',
                     username='[censored]',
                     password='[censored]',
                     user_agent='[censored]')


logging.basicConfig(filename='Bot.log', level=logging.INFO)


def execute_bot():
    for message in reddit.inbox.unread():
        if message.subreddit == 'redpillbooks':
            address = Modules.find_address(message.body)
            if address is not None:
                logging.info(message)
                Modules.send_email(address)
                message.mark_read()
                Modules.send_confirmation_reply(message)
                print('\n')


execute_bot()




