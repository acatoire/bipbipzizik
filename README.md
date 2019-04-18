# Music Cards

Click the image below to see a video of it being used

[![RFID Jukebox with Google Home](https://img.youtube.com/vi/AvCseOQidSw/0.jpg)](https://www.youtube.com/watch?v=AvCseOQidSw)

## Requires
### software:
- python evdev. To install:
```bash
wget http://dl.piwall.co.uk/python-evdev_0.4.1-1_armhf.deb

dpkg -i python-evdev_0.4.1-1_armhf.deb
```

### hardware:
- [Raspberry Pi Zero (Don't forget micro sd card and power supply)](http://www.microcenter.com/product/486575/Zero_W)
- [USB OTG Hub](https://www.amazon.com/gp/product/B01HYJLZH6/ref=oh_aui_detailpage_o08_s00?ie=UTF8&psc=1)
- [RFID 125Khz Reader](https://www.amazon.com/gp/product/B018C8C162/ref=oh_aui_detailpage_o03_s01?ie=UTF8&psc=1)
- [125Khz Cards](https://www.amazon.com/gp/product/B01MQY5Y7U/ref=ox_sc_act_title_1?smid=A1GYMVIZIMSYWM&psc=1)
- [RFID Card Inkjet Tray to print in your printer (Note this is the model needed for my Canon MX922 Printer)](https://www.amazon.com/gp/product/B00P25H0BA/ref=oh_aui_detailpage_o03_s01?ie=UTF8&psc=1)

Please note that Raspberry Pi Zero is insufficient to run both the Home Assistant and Music Cards concurrently. I recommend you use a Raspberry Pi 3 if you intend to run both at the same time.

## Steps to Configure and/or Run once if you dont want Music Cards to AutoStart

1. Run `python config.py` to select the reader from the inputs
2. Run `python add_card.py` to scan cards and enter your Google Play Music Playlist Name
3. Make .sh scrypts executables : chmod +x sonosplay.sh
4. Run `python box.py` to start the application and verify that it is reading your cards and csv list properly

## Install Service to AutoStart

- Change directory to music-cards/
```bash
cd music-cards/
```
- Copy the musiccards.service file to systemd
```bash
sudo cp musiccards.service /etc/systemd/system/musiccards.service
```
- Reload the Daemon
```bash
sudo systemctl daemon-reload
```
- Start the musiccards.service
```bash
sudo systemctl start musiccards.service
```
- Check if musiccards.service is running 
```bash
sudo systemctl status musiccards.service
```

## HomeAssistant Setup for Google Music

1. Place the files under homeassistant_files in the config directory of your [Homeassistant](https://www.home-assistant.io/) machine.
2. You will need to create custom_components/switch directory in your config directory and place [`gmusic.py`](https://github.com/mf-social/Home-Assistant/blob/master/custom_components/switch/gmusic.py) in there.
3. Follow [this forum post](https://community.home-assistant.io/t/google-music-in-ha/10976) to install gmusicapi, find your device id, and set up the component.
