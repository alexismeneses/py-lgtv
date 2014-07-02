#!/usr/bin/env python
"""
PYTHON Driver for LG TVs using manufacturer's RS232C protocol
"""

import sys, os, serial

LG_CMD_ONOFF = "ka"
LG_CMD_SOURCE = "kb"
LG_CMD_MUTE  = "ke"
LG_CMD_SOUND = "kf"

LG_SOURCE_DTV = 0
LG_SOURCE_TV = 1
LG_SOURCE_AV1 = 2
LG_SOURCE_AV2 = 3
LG_SOURCE_AV3 = 4
LG_SOURCE_COMP = 5
LG_SOURCE_RGB = 6
LG_SOURCE_HDMI1 = 7
LG_SOURCE_HDMI2 = 8
LG_SOURCE_HDMI3 = 9

LG_MAP_SOURCES = {
	"dtv": LG_SOURCE_DTV,
	"tv": LG_SOURCE_TV,
	"av1": LG_SOURCE_AV1,
	"av2": LG_SOURCE_AV2,
	"av3": LG_SOURCE_AV3,
	"component": LG_SOURCE_COMP,
	"rgb": LG_SOURCE_RGB,
	"hdmi1": LG_SOURCE_HDMI1,
	"hdmi2": LG_SOURCE_HDMI2,
	"hdmi3": LG_SOURCE_HDMI3,
} 

LG_MAP_SOURCES_INV = {v:k for k,v in LG_MAP_SOURCES.items()}

class LGTV:
	def __init__(self, device, tvid=0):
		self.serial = serial.Serial(device, 9600, timeout=15)
		self.tvid = tvid


	def reset(self):
		self.serial.write(".\n")


	def cmd(self, command, value):
		hvalue = hex(int(value))[2:].upper()
		retry = 3
		errormsg = ""
		while retry > 0:
			try:
        			self.serial.write(command + " " + str(self.tvid) + " " + hvalue + "\n")
        			line = self.serial.readline()
				status = line[5:7]
				data = int(line[7:line.index('x')], 16)
				if status == 'OK':
					return data
				elif status == 'NG' and data == 3:
					time.sleep(2)
					errormsg = "TV ask to wait indefinitely"
				elif status == 'NG':
					errormsg = "Command not supported"
					retry = 0
				else:
					errormsg = "Incorrect response format"
					self.reset()
			except:
				errormsg = "Incorrect or empty response"
				self.reset()
			retry -= 1
		raise Exception('unable to communicate with LGTV: ' + errormsg)


	def status(self, command):
		return self.cmd(command, 255)


	def on(self):
		"""
		Power ON the television
		"""

		self.cmd(LG_CMD_ONOFF, 1)


	def off(self):
		"""
		Power OFF the television
		"""
		self.cmd(LG_CMD_ONOFF, 0)


	def ispowered(self):
		"""
		Returns True if the television is currently powered on
		"""

		return bool(self.status(LG_CMD_ONOFF))


	def mute(self):
		"""
		Mute the sound
		"""

		# despite what is written in LG docs, mute is activated using "0"
		self.cmd(LG_CMD_MUTE, 0)


	def unmute(self):
		"""
		Unmuted the sound
		"""

		self.cmd(LG_CMD_MUTE, 1)

	def ismuted(self):
		"""
		Returns True if the sound is muted
		"""

		# warning: command seems buggy on some models as it toggles the mute status
		return not bool(self.status(LG_CMD_MUTE))


	def setsource(self, input_source):
		"""
		Change the source (aka Input) of the TV
		The argument must be on of LG_SOURCE_XXX constants
		"""

		if isinstance(input_source, str):
			str_source = input_source.lower()
			if str_source in LG_MAP_SOURCES:
				srcnum = LG_MAP_SOURCES[str_source]
			else:
				raise Exception('Unsupported input: ' + str_source)
		else:
			srcnum = input_source

		self.cmd(LG_CMD_SOURCE, srcnum)


	def getsource(self):
		"""
		Returns the current source of the TV
		"""

		return LG_MAP_SOURCES_INV[self.status(LG_CMD_SOURCE)]


	def setsound(self, value):
		"""
		Set the sound volume. Value must be between 0 and 100
		"""

		self.cmd(LG_CMD_SOUND, value)


	def soundup(self):
		"""
		Increase sound volume by 1
		"""

		value = self.getsound()
		if value < 100:
			value += 1
		self.setsound(value)


	def sounddown(self):
		"""
		Decrease sound volume by 1
		"""

		value = self.getsound()
		if value > 0:
			value -= 1
		self.setsound(value)


	def getsound(self):
		"""
		Returns the sound volume. Value will be between 0 and 100
		"""
		
		return self.status(LG_CMD_SOUND)

