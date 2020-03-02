import requests
from bs4 import BeautifulSoup
import time
from twilio.rest import Client
import os
import tweepy as tw
import json
from subprocess import call

# I'm aware that this code is BAD. It's okay, it was quick and dirty and never meant
# to be shared. Originally written by TylerCode and released under the MIT license. 

json_settings_name = "config.json"
watch_url = ""
twilio_account_sid = ""
twilio_auth_token = ""
twilio_phone_number = ""
target_phone_number = ""
twitter_check = ""
twitter_consumer_key = ""
twitter_consumer_secret = ""
twitter_access_token = "" # I considered getting these programatically but if I don't have an index in
twitter_access_token_secret = "" # 60 days when it expires I'll have already gone insane


def setup():
    with open(json_settings_name) as jsonDataFile:
        jsonData = json.load(jsonDataFile)
    
    # I've never used global before cause I usually pass everything
    # around in functions. If there's a cleaner way PLEASE tell me or
    # make a PR (Doesn't help I only use python for lambda usually)
    global watch_url
    global twilio_account_sid
    global twilio_auth_token
    global twilio_phone_number
    global target_phone_number
    global twitter_check
    global twitter_consumer_key
    global twitter_consumer_secret
    global twitter_access_token
    global twitter_access_token_secret

    watch_url = jsonData["watchUrl"]
    twilio_account_sid = jsonData["twilioAccountSID"]
    twilio_auth_token = jsonData["twilioAccountToken"]
    twilio_phone_number = jsonData["twilioPhoneNumber"]
    target_phone_number = jsonData["yourPhoneNumber"]
    twitter_check = jsonData["checkValveTwitter"]
    twitter_consumer_key = jsonData["twitterConsumerKey"]
    twitter_consumer_secret = jsonData["twitterConsumerSecret"]
    twitter_access_token = jsonData["twitterAccessToken"]
    twitter_access_token_secret = jsonData["twitterAccessSecret"]

# Responsible for sending a text message. 
def send_text(message_text):
    twilio_client = Client(twilio_account_sid, twilio_auth_token) 
    twilio_client.messages.create(to=target_phone_number, from_=twilio_phone_number, body=message_text)

def main():
    setup()
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    instances_found = 0 # I want to know every time the instances of "Notify Me" changes on the site (1, I'm lazy, 2, I don't know bs4 all that well)
    last_tweet = ""

    if twitter_check == "1":
        auth = tw.OAuthHandler(twitter_consumer_key, twitter_consumer_secret)
        auth.set_access_token(twitter_access_token, twitter_access_token_secret)
        api = tw.API(auth, wait_on_rate_limit=True)

    while True:
        print("URL: " + watch_url)
        response = requests.get(watch_url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        if twitter_check == "1":
            new_tweet = api.user_timeline(id = "1141417774201184257", count = 1)[0]

        if new_tweet.text != last_tweet and twitter_check == "1":
            message_text = "NEW VALVE TWEET: " + new_tweet.text
            call(["play synth.mp3"])
            send_text(message_text)
            last_tweet = new_tweet.text
            print(message_text)

        if str(soup).find("Notify Me") != instances_found:
            message_text = "Notify me changed from " + str(instances_found) + " to " + str(str(soup).find("Notify Me")) + ". Dont get your hopes up, but it might be time..."
            call(["play valve.mp3"])
            send_text(message_text)
            instances_found = str(soup).find("Notify Me")
            print(message_text)

        time.sleep(300)

main()
