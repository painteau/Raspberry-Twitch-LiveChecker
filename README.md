# LiveChecker

## Requirements

LiveChecker is a quick code that I wrote in Python. The goal was to light a LED throught Raspberry Pi GPIO pin when my favorite Twitch streamer was live. 

![RaspberryPINcode](https://grab.painteau.com/raspberry-pi-zero.jpg)

I connect a 5V LED between the pin 3 (which is GND) and 18.

This tutorial is made for beginners to help them build it from scratch.

## Requirements

- A Raspberry Pi (with Wireless capabilities like Zero or 3B)
- A SD Card (4GB or more)
- A lighting system running on 5V, ready to be connected to a Raspberry's GPIO.

## Prepare your SD Card

- Install balenaEtcher. You can get the last version here : https://www.balena.io/etcher/
- Download the latest "Raspbian Lite" distribution  from https://www.raspberrypi.org/downloads/raspbian/
- Unzip it to get the .img
- Flash the IMG to the SD card with balenaEtcher.
- Copy the blank ssh file to the root folder of your SD card
- Edit the "wpa_supplicant.conf" with your Wifi SSID and Password
- Copy the modified "wpa_supplicant.conf" file to the root folder of your SD card
- Put the SD card in your Raspberry and turn it on. It should connect to your Wifi automatically.
- Connect to your router or scan the network to get your Raspberry IP adress.

## Prepare your Raspberry

- Connect throught SSH with the login "pi" :

> ssh pi@MY.IP.ADRE.SS

- The default password is 'raspberry', so please change it by running :

> passwd 

- Type your old password (raspberry) and then 2 times your new password when asked.

- Let's make some update :

> sudo apt update

- And upgrade the Raspberry :

> sudo apt upgrade

- Let's install python3 and pip

> sudo apt install python3 python3-pip

Check python3 version

> python3 -V

- It should respond you with a Python Version number.

- Then install RPi.gpio

> sudo apt install rpi.gpio

- Install Twitch API with pip

> sudo pip3 install python-twitch-client

- Install GIT and VIM (I like vim but you can use nano if you prefer)

> sudo apt install git vim

- Let's go on our home directory :

> cd /home/pi/

- Then clone that repository from git hub

> git clone https://github.com/painteau/LiveChecker

- Change the details in your config file with your Twitch API Client ID and the channel you want to monitor.

> vim /home/pi/LiveChecker/config.py

- Type "a" Key to enter "Insertion mode" and modify your file.

- Exit by typing the "ESC" key, then write ":wq" and press enter to save and quit.

- Now, the script should be working. Try it :

> sudo /usr/bin/python3 /home/pi/LiveChecker/LiveChecker.py

- The script is working, so let's make a cron task so that it can be run automatically every minute.

> sudo crontab -e

- Select VIM as the default editor of crontab

- Type "a" Key to enter "Insertion mode" and insert this line at the end of the file

> */1 * * * * /usr/bin/python3 /home/pi/LiveChecker/LiveChecker.py

- Exit by typing the "ESC" key, then write ":wq" and press enter to save and quit.

- Check that crontab is updated by typing :

> sudo crontab -l

- Restart crontab if everything is ok :

> sudo /etc/init.d/cron restart

- You can shutdown your raspberry for now, connect your lighting system and restart your Raspberry.


## Prepare your Lighting system

- The LED is set to be placed on pin 18 of the GPIO.
- You can change the PIN in the code if you want.







