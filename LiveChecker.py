from twitch import TwitchClient
import RPi.GPIO as GPIO
import time
from config import * 

# Starting session
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

# Turning off LED
GPIO.output(18,GPIO.HIGH)
print ("LED off")


# Preparing Twitch check
client = TwitchClient(client_id)
# FINDING ID of that twitch channel
users = client.users.translate_usernames_to_ids(channel_name)

for user in users:
	Current_ID = user.id
	Current_Name = user.display_name

# HANDLING DATA
channel = client.streams.get_stream_by_user(Current_ID)

if channel is None:
	print(Current_Name + ' is not live')
	GPIO.output(18,GPIO.HIGH)
else:
	print(Current_Name + ' is live')
	GPIO.output(18,GPIO.LOW)