# Near-field communication (NFC) to Control Sonos Speaker
This is a project aimed at easing music&audio streaming for kids. In nutshell, it allows playing a audio by swipe of an NFC cards. Each NFC cards is associated with song or audiobook, so it can be identified easily. 

Behind the scene:

* Raspberry Pi is wired with RFID kit(RC522) connected to local network
* There is a sonos speaker in local network 
* A python based srocess is running on Raspberry Pi which contains the logic of reading NFC tag and queing a song in sonos speaker to play it immediately
* When a NFC cards is neared RFID kit, it reads the data and triggering queing and playing logic 

This ansible project containts everything that is needed to run it:

* Setups SPI on Raspberry Pi and reboots(if neccessary)
* Install neccessary software, python packages 
* It deploys the python code and adds it as a supervisord process


## How to use this code
Install required roles with the following command 

```
./extensions/setup/role_update.sh
```
This command will delete all external roles and download everything from scratch. It is a good practice, as this will not allow you to make changes in the roles.


Change the raspberry-pi IP in the `development.ini` file

````
[RaspberryPi]
pi@192.168.86.130 
````


Change the sonos IP address as well as mapping, based on RFID cards as well as media URI's, in `props.ini` under `../roles/deploy/files/props.ini`

To execute the ansible playbook, go to `plays` folder and:

```
ansible-playbook -i ../development.ini raspberry.yml
```

# License
MIT License.
