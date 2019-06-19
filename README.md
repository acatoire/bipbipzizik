# RFID Cards Trigger

This project is a fork of Music Card from [hoveeman/music-cards](https://github.com/hoveeman/music-cards) forked from [fsahli/music-cards](https://github.com/fsahli/music-cards).

It has been updated to be able to trig actions on others servers on rfid swipe. 
List of actions:
- sonos Api [node-sonos-http-api](https://github.com/jishi/node-sonos-http-api)
- home assistant (todo, change from hoveeman/music-cards)


## Requires
### software:
- python pip. To install:
```bash
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install python3-pip

```

- python evdev. To install:
```bash
sudo pip3 --default-timeout=1000 install evdev
```

```--default-timeout=1000``` helps if the raspberry is too slow

### hardware:
- [Raspberry Pi Zero (Don't forget micro sd card and power supply)](http://www.microcenter.com/product/486575/Zero_W)
- [USB OTG Hub](https://www.amazon.com/gp/product/B01HYJLZH6/ref=oh_aui_detailpage_o08_s00?ie=UTF8&psc=1)
- [RFID 125Khz Reader](https://www.amazon.com/gp/product/B018C8C162/ref=oh_aui_detailpage_o03_s01?ie=UTF8&psc=1)
- [125Khz Cards](https://www.amazon.com/gp/product/B01MQY5Y7U/ref=ox_sc_act_title_1?smid=A1GYMVIZIMSYWM&psc=1)

Remark : see on original project [https://github.com/hoveeman/music-cards](hoveeman/music-cards) for printable rfid cards

####Raspberry Limitaion
Please note that Raspberry Pi Zero is insufficient to run both the Home Assistant and and the rfid scanner. 
It is recommend you use a Raspberry Pi 3 if you intend to run both at the same time.

Test has to be done with [node-sonos-http-api](https://github.com/jishi/node-sonos-http-api) and rfid scanner, they should run together on all raspberry.

#####Raspberry Config
[Config the wifi on boot partition](https://www.raspberrypi-spy.co.uk/2017/04/manually-setting-up-pi-wifi-using-wpa_supplicant-conf/)

## Steps to Configure and/or Run once without AutoStart
0. Copy/Downloar/Clone the project in home/pi
1. Run `python3 setup_reader.py` to select the reader from the inputs
2. Run `python3 add_card.py` to scan cards and enter your Google Play Music Playlist Name
3. Make .sh scrypts executables : `chmod +x sonosplay.sh`
4. Run `python3 box.py` to start the application and verify that it is reading your cards and csv list properly

## Install Service to AutoStart

- Change directory to music-cards/
```bash
cd music-cards/
```
- Copy the musiccards.service file to systemd
```bash
sudo cp /home/pi/music-cards/musiccards.service /etc/systemd/system/musiccards.service
```
- Reload the Daemon
```bash
sudo systemctl daemon-reload
```
- Start the musiccards.service
```bash
sudo systemctl enable  musiccards.service
sudo systemctl start musiccards.service
```
- Check if musiccards.service is running 
```bash
sudo systemctl status musiccards.service
```

## HomeAssistant Setup for Google Music
TO BE CHECKED
1. Add the configs from homeassistant_files in the config of your [Homeassistant](https://www.home-assistant.io/).
2. You will need to create custom_components/switch directory in your config directory and place [`gmusic.py`](https://github.com/mf-social/Home-Assistant/blob/master/custom_components/switch/gmusic.py) in there.
3. Follow [this forum post](https://community.home-assistant.io/t/google-music-in-ha/10976) to install gmusicapi, find your device id, and set up the component.


