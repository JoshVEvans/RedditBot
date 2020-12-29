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
    key_words = ['give away', 'giving away', 'giveaway']
    
    for submission in subreddit.stream.submissions():
        for word in key_words:
            if word in submission.title.lower(): #lowercase all submission titles:
                print(f"Title: {submission.title} \nUrl: reddit.com{submission.permalink}")
                
                sendMail(f"{submission.title}",
                         "reddit.com{submission.permalink}")
                print('--------------------------------------------------')


def sendMail(subject, msg):
    sender, password, server, port = 'snekredditbot@gmail.com', 'pythonbot', 'smtp.gmail.com', 465

    server = smtplib.SMTP_SSL(server, port)
    server.login(sender, password)

    message = MIMEMultipart()
    message['From'], message['To'], message['Subject'] = sender, 'snekredditbot@gmail.com', subject

    message.attach(MIMEText(msg, 'plain'))
    server.send_message(message)



main()