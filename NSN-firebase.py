import RPi.GPIO as GPIO
from time import sleep
import datetime
from firebase import firebase

import urllib2, urllib, httplib
import json
import os 
from functools import partial
firebase = firebase.FirebaseApplication('INSERT YOUR FIREBASE HERE', None)


def update_firebase():

	i = 1
	while i < 6:
	 firebase.post('/TEST',i)
	 i += 1

while True:
		update_firebase()
		
        #sleepTime = int(sleepTime)
		sleep(5)
	








