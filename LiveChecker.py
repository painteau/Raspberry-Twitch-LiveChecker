from twitch import TwitchClient
from config import * 
import RPi.GPIO as GPIO
import time

#starting session
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
print ("LED off")
GPIO.output(18,GPIO.HIGH)

client = TwitchClient(client_id)

#FINDING ID of twitch channel
users = client.users.translate_usernames_to_ids(channel_name)

for user in users:
	Current_ID = user.id
	Current_Name = user.display_name

# TREATING DATA
channel = client.streams.get_stream_by_user(Current_ID)

if channel is None:
	print(Current_Name + ' is not live')
	GPIO.output(18,GPIO.HIGH)
else:
	print(Current_Name + ' is live')
	GPIO.output(18,GPIO.LOW)