import praw
from Google import create_service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from re import findall
import logging
from datetime import datetime

reddit = praw.Reddit(client_id='YNRmaCJKhq-6dw',
                     client_secret='ptkM4O_8HGCwn_SzEYOpGELEYv0xaw',
                     username='BaldakshBadal',
                     password='RedditPassword',
                     user_agent='Ballu')


def make_message():
    SORRY_MESSAGE = "I am sorry to disappoint you by not sending the files" \
                    " attached to this email. I don't want to get prosecuted"\
                    '. I have provided the links to the books below with any' \
                    ' other things you might need in order to' \
                    ' get access to the books. I hope you can forgive me.\n\n'
    DON_OF_DESIRE_LINK = 'https://b-ok.asia/book/5595127/c4565f\n'
    DIRTY_TALK_MASTERY_LINK = 'https://b-ok.asia/book/5749030/029f86\n'
    TOR_FOR_PC_LINK = 'https://www.torproject.org/download/\n'
    TOR_FOR_ANDROID_LINK = 'https://play.google.com/store/apps/details?id=org.torproject.torbrowser&hl=en_IN&gl=US\n'
    TOR_FOR_IOS_LINK = 'https://apps.apple.com/us/app/onion-browser/id519296448\n'
    UPVOTE_MESSAGE = 'Please upvote the post so more people can find the books faster.\n'
    REDDIT_POST_LINK = 'https://www.reddit.com/jze4dv\n'

    return (SORRY_MESSAGE +
            'Don of Desire Method: ' + DON_OF_DESIRE_LINK +
            'Dirty Talk Mastery: ' + DIRTY_TALK_MASTERY_LINK +
            '\n\n' +
            'You MIGHT need to install tor:-\n' +
            'Tor for PC: ' + TOR_FOR_PC_LINK +
            'Tor for android:' + TOR_FOR_ANDROID_LINK +
            'Tor for iOS: ' + TOR_FOR_IOS_LINK +
            '\n\n' +
            UPVOTE_MESSAGE +
            'My post: ' + REDDIT_POST_LINK)


def send_email(email_address):
    """Sends email to the 'email_address' parameter.
    This email will have the two books attached to it."""
    print(email_address, 'wants the books!')
    logging.basicConfig(filename='Bot.log', format='%(name)s : %(levelname)s : %(message)s', level=logging.INFO)
    logging.info('\n\n\n\n\n{} : {}'.format(datetime.today().replace(microsecond=0), email_address))
    CLIENT_SECRET_FILE = "credentials.json"
    API_NAME = 'gmail'
    API_VERSION = 'v1'
    SCOPES = ['https://mail.google.com/']
    service = create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    emailMsg = (make_message())

    mimeMessage = MIMEMultipart()
    mimeMessage['to'] = email_address
    mimeMessage['subject'] = 'Books'
    mimeMessage.attach(MIMEText(emailMsg, 'plain'))

    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

    message = service.users().messages().send(
        userId='me',
        body={'raw': raw_string}).execute()
    print(message)
    print(email_address, 'has received the books.')


def find_address(msg):
    """Given a string of text with an email address in it,
    this function will return the email address in the form of a string."""

    address = findall(r"[A-Za-z0-9.\-+_]+@[A-Za-z0-9.\-+_]+\.[A-Za-z]+", msg)
    if len(address) < 1:
        return None
    else:
        return address[0]


def send_confirmation_reply(message_id):
    reddit.comment(message_id).reply('The books have been sent to you! Please upvote the post '
                                     'so more people can find the books faster.Have a nice day!')







