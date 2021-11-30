#!/usr/bin/env python
import sys
import signal
import RPi.GPIO as GPIO
from soco import SoCo
import configparser
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
config = configparser.ConfigParser()
config.read('/home/pi/app/props.ini')

speakerIP = config['speaker']['ip']
look_up_table = config['look-up-table']
speaker = SoCo(speakerIP)
continue_reading = True

def sigterm_handler(_signo, _stack_frame):
    # Raises SystemExit(0) so it could exit gracefully 
    # This makes sure that GPIO will be cleaned 
    continue_reading = False
    GPIO.cleanup()
    sys.exit(0)

signal.signal(signal.SIGTERM, sigterm_handler)
    
 
while continue_reading:
    try:
        id, text = reader.read()
        uri = look_up_table[str(id)]
        speaker.clear_queue()
        speaker.add_uri_to_queue(uri)
        speaker.play_from_queue(0)
    except Exception:
        pass