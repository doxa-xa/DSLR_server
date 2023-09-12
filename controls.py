try:
	import gphoto2 as gp
	from snap import capture
except ImportError as err:
	print('Working on windows no Gphoto2')
import os, datetime as time


#enums for the different settings
iso_auto_hi_limit = 5
flash_shutter_speed =12
f_number = 21
shutter_speed = 35
shutter_speed2 =36
exposure_compensation = 16

#addresses the DSLR getting: name, current setting & range of the setting

class CaptureSettings:
	menu = 4
	camera = gp.Camera()
	context = gp.Context()

	def __init__(self,option):
		self.option = option
	
	#helper method for listing the range of the setting	
	def get_choices(self,value):
		choices = value.count_choices()
		lst = []
		for i in range(choices):
			lst.append(value.get_choice(i))
		return lst
	
	def get_value_info(self):
		master = self.camera.get_config(self.context)
		capture_settings = master.get_child(self.menu)
		menu_item = capture_settings.get_child(self.option)
		menu_item_range = self.get_choices(menu_item)
		return {
			"name" : menu_item.get_label(),
			"value" : menu_item.get_value(),
			"range:" : menu_item_range
		}
	def set_value(self,value):
		master = self.camera.get_config(self.context)
		capture_settings = master.get_child(self.menu)
		menu_item = capture_settings.get_child(self.option)
		menu_item_range = self.get_choices(menu_item)
		for item in menu_item_range:
			if value == item:
				menu_item.set_value(value)
				self.camera.set_config(master)
				self.camera.exit()
		return {"name" : menu_item.get_label(), "value":menu_item.get_value()}

def capture_image():
	capture()

#capt_set = CaptureSettings(f_number)

#print(capt_set.get_value_info())
