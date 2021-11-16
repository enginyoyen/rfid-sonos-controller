#!/usr/bin/env python
import sys
import signal
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from soco import SoCo
import configparser

reader = SimpleMFRC522()
config = configparser.ConfigParser()

config.read('props.ini')
speakerIP = config['speaker']['ip']
look_up_table = config['look-up-table']

speaker = SoCo(speakerIP)

def sigterm_handler(_signo, _stack_frame):
    # Raises SystemExit(0) so it could exit gracefully 
    # This makes sure that GPIO will be cleaned 
    sys.exit(0)

if sys.argv[1] == "handle_signal":
    signal.signal(signal.SIGTERM, sigterm_handler)

while True:
    try:
        id, text = reader.read()
        uri = look_up_table[str(id)]
        speaker.clear_queue()
        speaker.add_uri_to_queue(uri)
        speaker.play_from_queue(0)
    finally:
        GPIO.cleanup()
    