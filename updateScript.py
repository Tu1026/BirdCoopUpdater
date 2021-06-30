"""Monitors the given course and send update when a spot frees up

    Usage: change the url to the course, chagne the word looking for to however, many people is registered in the class
    , subscribe to the printed website to recieve notification
"""


from bs4 import BeautifulSoup
import time
import ctypes
import smtplib
from dotenv import load_dotenv
import os
import discord
import datetime
import gc
import requests
import re
import lxml
import webbrowser


load_dotenv()
name = input('Who is registering for the gym: ')
def send_discord_message(word):
    TOKEN = os.getenv('DISCORD_TOKEN')
    client = discord.Client()

    @client.event
    async def on_ready():
        await client.get_channel(736117723322646528).send(f'{name} register for {word} here {url} RIGHT NOW!!!!!!!!!!!')
        await client.get_channel(736117723322646528).send(f'{name} Register for {word} here {url} RIGHT NOW!!!!!!!!!!!')
        await client.get_channel(736117723322646528).send(f'{name} Register for {word} here {url} RIGHT NOW!!!!!!!!!!!')
        await client.get_channel(736117723322646528).send(f'{name} Register for {word} here {url} RIGHT NOW!!!!!!!!!!!')
        await client.get_channel(736117723322646528).send(f'{name} Register for {word} here {url} RIGHT NOW!!!!!!!!!!!')
        await client.close()
       

    client.run(TOKEN)


#Reference from https://stackabuse.com/how-to-send-emails-with-gmail-using-python/
def send_email(username, password):
    """send email to the person who wishes to recieve notification
    """
    sent_from = username
    to = [noti_email]
    subject = 'Course registeration for ' + session
    body = 'The course you want has a seat open!!'
    message ='Subject: {}\n\n{}'.format(subject, body)

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(username, password)
    server.sendmail(sent_from, to, message)
    server.close()

def update_loop():
## Keeps looping through the website until a spot is open
    while True:
        try:
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, "lxml")
            soup = str(soup)
            find = re.findall('"Spots":"Full"', soup)
            # if the amount of people registered has not changed keep looping
        except:
            time.sleep(10)
            update_loop()
           
        if (len(find)):
            # wait 10 seconds,
            print("No seats avaliable yet updating in 10 seconds")
            time.sleep(10)
            # continue with the script,
            del response, soup, find
            gc.collect()
            continue
            
        # if the amout of people registered has changed do a pop up and send a notificaiton on the website
        else:
            # notify.send("register for " + course + " NOW")
            try:
                # log into server account to send message
                # config = ConfigParser()
                # config.read('config.ini')
                username = os.getenv("username1")
                password = os.getenv("password")
                # username = config.get("email", "username")
                # password = config.get("email", "password")
                # send_fb_message("register for " + course + "NOWWWWWWW")
                send_discord_message(session)
                send_email(username, password)
                print("email notificaiton sent")
                webbrowser.open_new(url)

            except:
                print("something went wrong with emailing stuff or FB stuff")
            if platform == "win32" or platform == 'win64':
                ctypes.windll.user32.MessageBoxW(0, session, 'Spot is now open for', session)
            break

#get information from user
from sys import argv, exit, platform
noti_email = "s31302@gmail.com"
session = "gym"
url = input("What is the session that you want to get in: ")
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
exit(update_loop())
