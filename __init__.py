# Copyright 2017 David Lewis
# This file is part of the Villanova tour guide mrcroft skill
from os.path import dirname

import mycroft.util
import time
import requests
import json
import threading
import sys
from os.path import abspath, dirname
sys.path.append(abspath(dirname(__file__)))
import GPIO

from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'dlew'

LOGGER = getLogger(__name__)

class Test2Skill(MycroftSkill):
		def __init__(self):
				super(Test2Skill, self).__init__(name="Test2Skill")

		def initialize(self):
				blueberry_intent = IntentBuilder("BlueberryIntent"). \
						require("BlueberryKeyword").build()
				self.register_intent(blueberry_intent, self.handle_blueberry_intent)

				# ---------------------------------------------------------------------------------

		def handle_blueberry_intent(self, message):
				GPIO.set("GPIO1","Off")
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				self.speak_dialog("blueberry")
				time.sleep(1) 									#I put the V eyes here
				#GPIO.set("GPIO1","Off")
				GPIO.set("GPIO2","On")
				GPIO.set("GPIO3","Off")
				#GPIO.set("GPIO4","Off")

				try:
					mycroft.util.wait_while_speaking()
				except:
					time.sleep(5)

				GPIO.set("GPIO1","Off")
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","Off")
				GPIO.set("GPIO4","On")
				
		def stop(self):
				pass

def create_skill():
		return Test2Skill()
