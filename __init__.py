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

class AmbassadorSkill(MycroftSkill):
		def __init__(self):
				super(AmbassadorSkill, self).__init__(name="AmbassadorSkill")

		def initialize(self):
				fun_fact_villanova_intent = IntentBuilder("FunFactVillanovaIntent"). \
						require("FunFactVillanovaKeyword").build()
				self.register_intent(fun_fact_villanova_intent, self.handle_fun_fact_villanova_intent)

				# ---------------------------------------------------------------------------------

				college_majors_intent = IntentBuilder("CollegeMajorsIntent"). \
						require("CollegeMajorsKeyword").build()
				self.register_intent(college_majors_intent, self.handle_college_majors_intent)

				# ---------------------------------------------------------------------------------

				college_minors_intent = IntentBuilder("CollegeMinorsIntent"). \
						require("CollegeMinorsKeyword").build()
				self.register_intent(college_minors_intent, self.handle_college_minors_intent)

				# ---------------------------------------------------------------------------------

				engineering_synopsis_intent = IntentBuilder("EngineeringSynopsisIntent"). \
						require("EngineeringSynopsisKeyword").build()
				self.register_intent(engineering_synopsis_intent, self.handle_engineering_synopsis_intent)

		def handle_fun_fact_villanova_intent(self, message):
				GPIO.set("GPIO1","Off")
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				self.speak_dialog("fun.fact.villanova")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO2","On")
				GPIO.set("GPIO3","Off")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(5)
				except:
					time.sleep(5)

				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO4","On")

		def handle_college_majors_intent(self, message):
				GPIO.set("GPIO1","Off")
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				self.speak_dialog("college.majors")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO4","On")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(8)
				except:
					time.sleep(8)

				GPIO.set("GPIO3","Off")

		def handle_college_minors_intent(self, message):
				GPIO.set("GPIO1","Off")
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				self.speak_dialog("college.minors")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO4","On")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(8)
				except:
					time.sleep(8)

				GPIO.set("GPIO3","Off")

		def handle_engineering_synopsis_intent(self, message):
				GPIO.set("GPIO1","Off")
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				self.speak_dialog("engineering.synopsis")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO4","On")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(8)
				except:
					time.sleep(8)

				GPIO.set("GPIO3","Off")
				
		def stop(self):
				pass

def create_skill():
		return AmbassadorSkill()
