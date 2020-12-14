import Modules
import praw
import logging

reddit = praw.Reddit(client_id='YNRmaCJKhq-6dw',
                     client_secret='ptkM4O_8HGCwn_SzEYOpGELEYv0xaw',
                     username='BaldakshBadal',
                     password='RedditPassword',
                     user_agent='Ballu')


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




