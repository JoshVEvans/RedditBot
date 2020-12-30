import praw
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def main():
    reddit = praw.Reddit(username = 'SnekBotReddit',
                    password = 'joshuaevans2003!',
                    client_id = 'eiG17bKMV--z4Q',
                    client_secret = 'n1bz222d6RT7Ac-N3SIKpjB6Slo5rA',
                    user_agent = 'SnekBot by /u/SnekBotReddit -- https://github.com/JoshVEvans/RedditBot')

    subreddit = reddit.subreddit('all')
    white_list = ['give away', 'giving away', 'giveaway']
    black_list = ['cum']

    for submission in subreddit.stream.submissions():
        send, subject, body = False, None, None

        for word in white_list:
            for bad in black_list:
                if word in submission.title.lower() and bad not in submission.title.lower(): #lowercase all submission titles:
                    subject, body = f"{submission.title}", f"reddit.com{submission.permalink}"

                    send = True
                    break

            if send == True:
                print(f"Title: {subject} \nUrl: {body}")
                sendMail(subject, body)
                print('--------------------------------------------------')

                send = False

        



def sendMail(subject, msg):
    sender, password, server, port = 'snekredditbot@gmail.com', 'pythonbot', 'smtp.gmail.com', 465

    server = smtplib.SMTP_SSL(server, port)
    server.login(sender, password)

    message = MIMEMultipart()
    message['From'], message['To'], message['Subject'] = sender, 'snekredditbot@gmail.com', subject

    message.attach(MIMEText(msg, 'plain'))
    server.send_message(message)


main()