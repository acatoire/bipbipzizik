# RFID Cards Trigger

This project is a fork of Music Card from [hoveeman/music-cards](https://github.com/hoveeman/music-cards) forked from [fsahli/music-cards](https://github.com/fsahli/music-cards).

It has been updated to be able to trig actions on others servers on rfid swipe. 
List of actions:
- sonos Api [node-sonos-http-api](https://github.com/jishi/node-sonos-http-api)
- home assistant (todo, change from hoveeman/music-cards)


## Requires

### Hardware:
- [Raspberry Pi Zero](http://www.microcenter.com/product/486575/Zero_W)
- Don't forget micro sd card and power supply
- [USB OTG Hub](https://www.amazon.com/gp/product/B01HYJLZH6/ref=oh_aui_detailpage_o08_s00?ie=UTF8&psc=1)
- [RFID 125Khz Reader](https://www.amazon.com/gp/product/B018C8C162/ref=oh_aui_detailpage_o03_s01?ie=UTF8&psc=1)
- [125Khz Cards](https://www.amazon.com/gp/product/B01MQY5Y7U/ref=ox_sc_act_title_1?smid=A1GYMVIZIMSYWM&psc=1)

Remark : see on original project [https://github.com/hoveeman/music-cards](hoveeman/music-cards) for printable rfid cards

### Raspberry basis:
- Download and flash the las lite version of Raspbian
- Enable SSH by creating an empty "ssh" named file at the root of the boot partition (visible on windows)
- Configure your wifi using the wpa_supplicant.conf template in the tools folder [Config the wifi on boot partition](https://www.raspberrypi-spy.co.uk/2017/04/manually-setting-up-pi-wifi-using-wpa_supplicant-conf/)

### Linux basic
Update your distrib to be up to date
```bash
sudo apt-get update
sudo apt-get upgrade -y
```

### software setup:
- You need git to clone the project repository
```bash
sudo apt install git-all
git clone https://github.com/acatoire/music-cards music-cards
```
TODO procedure without git (wget?)

- You need python pip
- Then all python packages needed can be installed from requirements file
```bash
sudo apt-get install python3-pip
sudo pip3 install -r requirements.txt
```

```--default-timeout=1000``` for pip helps if the raspberry or the connection is too slow

### Start the application
#### Configure your database
1. TODO Procedure create configuration for a new pi application
- Get your raspberry unique ID (16 numbers ex:0000XXXXXXXXXXXX) with the command ```cat /proc/cpuinfo```
2. TODO procedure to add new cards

#### Configure the rfid reader
Run `python3 modules/rfid_reader/setup_reader.py` to select the reader from the detected inputs inputs

#### Steps to Run without AutoStart
Simply run the application with python 3
```bash 
python3 box.py
```
This will loop reading rfid cards.
But the application will not automatically restart.
See the following procedure to setup the auto-start.


#### Install Service to AutoStart
- Change directory to music-cards/
- Copy the musiccards.service file to systemd
- Reload the Daemon
- Enable the musiccards.service
- Start the musiccards.service
```bash
cd music-cards/
sudo cp /home/pi/music-cards/musiccards.service /etc/systemd/system/musiccards.service
sudo systemctl daemon-reload
sudo systemctl enable musiccards.service
sudo systemctl start musiccards.service
```

##### Manage Running Service
- Check if musiccards.service is running 
```bash
sudo systemctl status musiccards.service
```
- Watch the full log of musiccards.service 
```bash
sudo journalctl -u musiccards.service
```
- Restart service after file update 
```bash
sudo systemctl restart musiccards.service
```

#### Install node-sonos-http-api
The sonos Api [node-sonos-http-api](https://github.com/jishi/node-sonos-http-api) can be setup on a dedicated server. 

##### Locally setup
[install node](https://www.instructables.com/id/Install-Nodejs-and-Npm-on-Raspberry-Pi/)
- Install nodejs
- Clone the repo
- Enter in the folder
- install the package and start it
```bash
sudo apt-get install nodejs
sudo apt-get install npm
git clone https://github.com/jishi/node-sonos-http-api node-sonos-http-api
cd node-sonos-http-api
npm install --production
npm start
```

TODO auto start

##### Docker




##Possibles Errors and solution
### Missing your app token in database
```bash
Exception: The config for 0000XXXXXXXXXXXX is not present in the bipbipzizik database. 
           Did you create it?
```
You didn't register your raspberry unique ID (16 numbers ex:0000XXXXXXXXXXXX) in the database.
Execute the procedure as described above.

### Missing your card in database
```bash
Read card:  XXXXXXXXX
Card not found in database
```
You didn't register the card passed on the reader.
Execute the procedure as described above.


System has not been booted with systemd as init system (PID 1). Can't operate.
Failed to connect to bus: Host is down

### urllib3
```
Firebase_Admin Error TypeError: __init__() got an unexpected keyword argument 'status'
```
try:
```
python3 -m pip install --upgrade urllib3
```


###Raspberry Limitaion
####node-sonos-http-api
Test has to be done with [node-sonos-http-api](https://github.com/jishi/node-sonos-http-api) and rfid scanner, they should run together on all raspberry.

####Home Assistant
Please note that Raspberry Pi Zero is insufficient to run both the Home Assistant and and the rfid scanner. 
It is recommend you use a Raspberry Pi 3 if you intend to run both at the same time.



## HomeAssistant Setup for Google Music
TO BE CHECKED
1. Add the configs from homeassistant_files in the config of your [Homeassistant](https://www.home-assistant.io/).
2. You will need to create custom_components/switch directory in your config directory and place [`gmusic.py`](https://github.com/mf-social/Home-Assistant/blob/master/custom_components/switch/gmusic.py) in there.
3. Follow [this forum post](https://community.home-assistant.io/t/google-music-in-ha/10976) to install gmusicapi, find your device id, and set up the component.

## For Dev
### Unit test

#### Run all unit test of the project
```
python -m unittest discover -p "*_test.py"
```

#### Run unit test with coverage on it

Specific file:
```
coverage run xxx_Test.py
```

All unit test:
```
coverage run -m unittest discover -p "*_test.py"
```

#### Generate coverage report
```
coverage erase
coverage run -m unittest discover -p "*_test.py"
coverage report --omit "*_test.py"
coverage html --omit "*_test.py"
```